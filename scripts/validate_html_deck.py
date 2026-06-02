#!/usr/bin/env python3
"""Lightweight validation for generated single-file HTML decks."""
from __future__ import annotations

import re
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_html_deck.py <deck.html>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"missing file: {path}", file=sys.stderr)
        return 1
    text = path.read_text(encoding="utf-8")
    checks = {
        "has html doctype": "<!DOCTYPE html" in text or "<!doctype html" in text.lower(),
        "has slide sections": len(re.findall(r'class=[\"\'][^\"\']*\bslide\b', text)) >= 3,
        "has keyboard navigation": "keydown" in text and ("ArrowRight" in text or "PageDown" in text),
        "has print css": "@media print" in text,
        "self contained style": "<style" in text and "</style>" in text,
        "self contained script": "<script" in text and "</script>" in text,
    }
    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        print("validation failed:")
        for item in failed:
            print(f"- {item}")
        return 1
    print(f"ok: {path} looks like a valid html slide deck")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
