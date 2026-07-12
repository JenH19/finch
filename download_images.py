#!/usr/bin/env python3
"""
Bright Finch Coaching — Image Downloader
Downloads all images currently used on brightfinchcoaching.com (Squarespace)
and saves them with the correct names for the new static site.

Run from inside the brightfinch/ folder:
    python3 download_images.py

Requirements: Python 3 (built-in libraries only)
"""

import urllib.request
import urllib.error
import os
import sys

# ── Image targets ────────────────────────────────────────────────────────────
# Format: (save_as, url, description)
IMAGES = [
    (
        "images/hero.jpg",
        "https://images.squarespace-cdn.com/content/v1/683103b3e875307a3a8112f6/a3ebdd1a-7989-41f5-b6ef-87ecc276b41d/Maison+M+retreat-211.jpeg",
        "Hero — Maison M retreat"
    ),
    (
        "images/event-perch.jpg",
        "https://images.squarespace-cdn.com/content/v1/683103b3e875307a3a8112f6/1782169843869-EYHI65UZECY27L2S1QAM/unsplash-image-nF8xhLMmg0c.jpg",
        "Event — The Perch Gathering"
    ),
    (
        "images/event-clarity-uncorked.jpg",
        "https://images.squarespace-cdn.com/content/v1/683103b3e875307a3a8112f6/1763227830861-WIJLKWX5B7541D99F2KM/unsplash-image-qT515JdZNy8.jpg",
        "Clarity Uncorked — retreat banner"
    ),
    (
        "images/jen.jpg",
        "https://images.squarespace-cdn.com/content/v1/683103b3e875307a3a8112f6/e46072ac-fd1e-4a86-a7dd-7cc5403fb61c/IMG_0878.jpeg",
        "Jen's headshot (About page)"
    ),
    (
        "images/offering-1.jpg",
        "https://images.squarespace-cdn.com/content/v1/683103b3e875307a3a8112f6/1748049659940-MSIZUEFRXCNKI4MHEVP7/unsplash-image-eLC1Bd3PLu4.jpg",
        "Offering 1 — 1:1 Clarity Coaching Session"
    ),
    (
        "images/offering-2.jpg",
        "https://images.squarespace-cdn.com/content/v1/683103b3e875307a3a8112f6/1748049789783-M3EYQEK8CIJ54QQZUGGS/unsplash-image--YTfSdXKFec.jpg",
        "Offering 2 — Rise & Realign"
    ),
    (
        "images/offering-3.jpg",
        "https://images.squarespace-cdn.com/content/v1/683103b3e875307a3a8112f6/1748051069393-HKSU71VT6UT78T3GINDT/unsplash-image-V72Hk6LjjjI.jpg",
        "Offering 3 — Reset & Reconnect"
    ),
]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# ─────────────────────────────────────────────────────────────────────────────

def progress_bar(downloaded, total):
    if total <= 0:
        return ""
    pct = downloaded / total
    filled = int(pct * 30)
    bar = "█" * filled + "░" * (30 - filled)
    mb = downloaded / 1_048_576
    total_mb = total / 1_048_576
    return f"  [{bar}] {pct*100:.0f}%  {mb:.1f}/{total_mb:.1f} MB"


def download(save_as, url, description):
    os.makedirs(os.path.dirname(save_as), exist_ok=True)

    print(f"\n→ {description}")
    print(f"  Saving to: {save_as}")

    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            total = int(resp.getheader("Content-Length", 0))
            downloaded = 0
            chunk = 65536  # 64 KB

            with open(save_as, "wb") as f:
                while True:
                    data = resp.read(chunk)
                    if not data:
                        break
                    f.write(data)
                    downloaded += len(data)
                    print(f"\r{progress_bar(downloaded, total)}", end="", flush=True)

        size_kb = os.path.getsize(save_as) / 1024
        print(f"\r  ✓ Done — {size_kb:.0f} KB saved" + " " * 20)
        return True

    except urllib.error.HTTPError as e:
        print(f"\r  ✗ HTTP {e.code}: {e.reason}")
        return False
    except urllib.error.URLError as e:
        print(f"\r  ✗ Network error: {e.reason}")
        return False
    except Exception as e:
        print(f"\r  ✗ Error: {e}")
        return False


def main():
    print("=" * 55)
    print("  Bright Finch Coaching — Image Downloader")
    print("=" * 55)
    print(f"  Downloading {len(IMAGES)} images...\n")

    ok, fail = 0, 0
    for save_as, url, desc in IMAGES:
        if download(save_as, url, desc):
            ok += 1
        else:
            fail += 1

    print("\n" + "=" * 55)
    print(f"  Complete: {ok} downloaded, {fail} failed")
    if fail:
        print("  ⚠️  Some images failed. Check URLs or try again.")
        print("     You may need to manually save them from the old site.")
    else:
        print("  🎉 All images ready! They're already in images/ —")
        print("     just push the whole brightfinch/ folder to GitHub.")
    print("=" * 55 + "\n")

    sys.exit(0 if fail == 0 else 1)


if __name__ == "__main__":
    main()
