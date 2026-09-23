"""Email Buttondown subscribers about posts that just went live.

Runs after each deploy (push + the daily 06:00 rebuild). Reads the live RSS feed,
and for every post published on/after ANNOUNCE_SINCE that Buttondown hasn't
already sent an email for (matched by subject), sends one. No state is kept in
the repo: Buttondown's own sent list is the record, so reruns are safe.

Env: BUTTONDOWN_API_KEY (required), FEED_URL (required),
     ANNOUNCE_SINCE (YYYY-MM-DD, default below), DRY_RUN=1 to only print.
"""

import html
import json
import os
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime
from email.utils import parsedate_to_datetime

API = "https://api.buttondown.com/v1/emails"
# Posts before this date were already on the site when subscriptions started.
DEFAULT_SINCE = "2026-09-24"


def request(method, url, key, body=None):
    headers = {
        "Authorization": f"Token {key}",
        "X-API-Version": "2026-04-01",
        "Content-Type": "application/json",
        # Buttondown asks for this on an API key's first real send.
        "X-Buttondown-Live-Dangerously": "true",
    }
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read() or b"{}")


def sent_subjects(key):
    subjects, url = set(), API
    while url:
        page = request("GET", url, key)
        subjects.update(e.get("subject", "") for e in page.get("results", []))
        url = page.get("next")
    return subjects


def live_posts(feed_url):
    with urllib.request.urlopen(feed_url, timeout=30) as r:
        root = ET.fromstring(r.read())
    for item in root.iter("item"):
        yield {
            "title": item.findtext("title", "").strip(),
            "link": item.findtext("link", "").strip(),
            "date": parsedate_to_datetime(item.findtext("pubDate")).date(),
            "summary": re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html.unescape(item.findtext("description", "")))).strip(),
        }


def main():
    key = os.environ.get("BUTTONDOWN_API_KEY")
    if not key:
        print("BUTTONDOWN_API_KEY not set, skipping")
        return
    since = datetime.strptime(os.environ.get("ANNOUNCE_SINCE") or DEFAULT_SINCE, "%Y-%m-%d").date()
    dry = os.environ.get("DRY_RUN") == "1"

    fresh = [p for p in live_posts(os.environ["FEED_URL"]) if since <= p["date"] <= date.today()]
    if not fresh:
        print("no new posts")
        return

    already = sent_subjects(key)
    for p in sorted(fresh, key=lambda p: p["date"]):
        if p["title"] in already:
            print(f"already sent: {p['title']}")
            continue
        body = f"{p['summary']}\n\n[Read the whole thing]({p['link']})"
        if dry:
            print(f"would send: {p['title']}\n{body}\n")
            continue
        request("POST", API, key, {"subject": p["title"], "body": body, "status": "about_to_send"})
        print(f"sent: {p['title']}")


if __name__ == "__main__":
    try:
        main()
    except urllib.error.HTTPError as e:
        print(f"Buttondown error {e.code}: {e.read().decode(errors='replace')}")
        sys.exit(1)
