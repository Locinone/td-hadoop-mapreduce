#!/usr/bin/env python3
import sys
import json
import re

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        tweet = json.loads(line)
        text = tweet.get("text", "").lower()
        location = tweet.get("user", {}).get("location", "Unknown").strip()
        # Normaliser la location (optionnel)
        location = location if location else "Unknown"

        # Tokenisation simple
        words = re.findall(r'\b\w+\b', text)
        for word in words:
            print(f"{location}\t{word}")
    except json.JSONDecodeError:
        continue
