"""HTML link-discovery crawl used for the NITA SEO audit (Step 1 crawl baseline).

Follows internal <a href> links from a start URL with no depth limit, fetching
HTML pages only. Internal non-HTML resources (PDFs, images, documents) are
checked with HEAD; external links are recorded but not requested. Respects the
public robots.txt Disallow rules. Sequential requests with a fixed delay.

Usage: python3 -I link_discovery.py <start_url> <output_dir> [delay_seconds]
Outputs: pages.csv, links_resources.csv, links_external.csv, summary.txt
"""
import csv
import sys
import time
import urllib.error
import urllib.request
import urllib.robotparser
from collections import deque
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlsplit, urlunsplit

UA = "Mozilla/5.0 (compatible; seo-audit-link-discovery/1.0)"
RESOURCE_EXT = {
    ".pdf", ".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".doc", ".docx",
    ".xls", ".xlsx", ".ppt", ".pptx", ".zip", ".csv", ".mp4", ".mp3", ".txt",
}
MAX_PAGES = 4000


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


OPENER = urllib.request.build_opener(NoRedirect)


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.canonical, self.title, self._in_title = [], "", "", False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "a" and a.get("href"):
            self.links.append(a["href"].strip())
        elif tag == "link" and "canonical" in (a.get("rel") or "").lower():
            self.canonical = a.get("href", "")
        elif tag == "title":
            self._in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def request(url, method="GET"):
    req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
    try:
        with OPENER.open(req, timeout=30) as r:
            body = r.read() if method == "GET" else b""
            return r.status, r.headers, body
    except urllib.error.HTTPError as e:
        return e.code, e.headers, b""
    except Exception as e:  # network error
        return 0, {}, str(e).encode()


def main():
    start, out = sys.argv[1], Path(sys.argv[2])
    delay = float(sys.argv[3]) if len(sys.argv) > 3 else 0.4
    out.mkdir(parents=True, exist_ok=True)
    host = urlsplit(start).hostname

    robots = urllib.robotparser.RobotFileParser(f"https://{host}/robots.txt")
    robots.read()

    def norm(u):
        """Internal URLs are queued as HTTPS; the original scheme is recorded separately."""
        u = urldefrag(u)[0]
        p = urlsplit(u)
        return urlunsplit(("https", p.netloc.lower(), p.path or "/", p.query, ""))

    seen = {norm(start): (0, "", "https")}
    queue = deque([norm(start)])
    pages, resources, external = [], {}, {}
    while queue and len(pages) < MAX_PAGES:
        url = queue.popleft()
        depth, source, scheme = seen[url]
        if not robots.can_fetch(UA, url):
            pages.append([url, depth, source, scheme, "blocked-by-robots", "", "", "", ""])
            continue
        status, headers, body = request(url)
        ctype = headers.get("Content-Type", "") if headers else ""
        loc = headers.get("Location", "") if headers else ""
        canonical = title = ""
        if 300 <= status < 400 and loc:
            target = urljoin(url, loc)
            if urlsplit(target).hostname == host:
                n = norm(target)
                if n not in seen:
                    seen[n] = (depth + 1, url, urlsplit(target).scheme)
                    queue.append(n)
        elif status == 200 and "html" in ctype:
            p = LinkParser()
            p.feed(body.decode("utf-8", "replace"))
            canonical, title = p.canonical, " ".join(p.title.split())
            for href in p.links:
                if href.startswith(("mailto:", "tel:", "javascript:", "#")):
                    continue
                absu = urldefrag(urljoin(url, href))[0]
                sp = urlsplit(absu)
                if sp.scheme not in ("http", "https"):
                    continue
                if sp.hostname != host:
                    external.setdefault(absu, url)
                    continue
                ext = Path(sp.path).suffix.lower()
                if ext in RESOURCE_EXT:
                    resources.setdefault(absu, [url, sp.scheme])
                    continue
                n = norm(absu)
                if n not in seen:
                    seen[n] = (depth + 1, url, sp.scheme)
                    queue.append(n)
        pages.append([url, depth, source, scheme, status, ctype.split(";")[0], loc, canonical, title])
        time.sleep(delay)

    with open(out / "pages.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["url", "crawl_depth", "first_found_on", "link_scheme", "status", "content_type",
                    "location", "canonical", "title"])
        w.writerows(pages)

    with open(out / "links_resources.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["url", "first_found_on", "link_scheme", "status", "content_type", "location"])
        for u, (src, scheme) in resources.items():
            if not robots.can_fetch(UA, u):
                w.writerow([u, src, scheme, "blocked-by-robots", "", ""])
                continue
            status, headers, _ = request(u, "HEAD")
            w.writerow([u, src, scheme, status,
                        (headers.get("Content-Type", "") if headers else "").split(";")[0],
                        headers.get("Location", "") if headers else ""])
            time.sleep(delay)

    with open(out / "links_external.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["url", "first_found_on"])
        w.writerows(external.items())

    with open(out / "summary.txt", "w") as f:
        f.write(f"start={start}\nfinished={time.strftime('%Y-%m-%dT%H:%M:%S%z')}\n")
        f.write(f"pages_requested={len(pages)}\nqueue_remaining={len(queue)}\n")
        f.write(f"max_depth={max((p[1] for p in pages), default=0)}\n")
        f.write(f"internal_resources={len(resources)}\nexternal_links={len(external)}\n")
        f.write(f"delay_seconds={delay}\nuser_agent={UA}\nmax_pages={MAX_PAGES}\n")


if __name__ == "__main__":
    main()
