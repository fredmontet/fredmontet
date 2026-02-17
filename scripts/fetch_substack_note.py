#!/usr/bin/env python3
"""Fetch latest Substack note for inclusion in the site build."""

import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SUBSTACK_USER_ID = 186540262
SUBSTACK_HANDLE = "fredmontet"
API_URL = (
    f"https://substack.com/api/v1/reader/feed/profile/{SUBSTACK_USER_ID}?limit=1"
)
OUTPUT = Path(__file__).resolve().parent.parent / "_generated" / "latest_note.qmd"


def fetch_latest_note():
    req = urllib.request.Request(API_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    items = data.get("items", [])
    if not items:
        return None

    item = items[0]
    comment = item.get("comment", {})
    body = comment.get("body", "")
    date_str = item.get("context", {}).get("timestamp", "")
    note_id = item.get("entity_key", "")

    return {"body": body, "date": date_str, "note_id": note_id}


def main():
    OUTPUT.parent.mkdir(exist_ok=True)

    try:
        note = fetch_latest_note()
        if note and note["body"]:
            try:
                dt = datetime.fromisoformat(note["date"].replace("Z", "+00:00"))
                date_fmt = dt.strftime("%B %d, %Y")
            except (ValueError, AttributeError):
                date_fmt = ""

            note_url = f"https://substack.com/@{SUBSTACK_HANDLE}/note/{note['note_id']}"
            date_suffix = f" · {date_fmt}" if date_fmt else ""

            content = f"""::: {{.thought}}
{note["body"]}

— [Substack Notes]({note_url}){date_suffix}
:::
"""
        else:
            content = ""
    except Exception as e:
        print(f"Warning: Could not fetch Substack note: {e}")
        content = ""

    OUTPUT.write_text(content)
    if content:
        print(f"Fetched latest Substack note: {note['body'][:50]}...")
    else:
        print("No Substack note fetched.")


if __name__ == "__main__":
    main()
