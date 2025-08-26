#!/usr/bin/env python3
import sys, json
from datetime import datetime

for line in sys.stdin:
    try:
        tweet = json.loads(line)
        ts = datetime.strptime(tweet['timestamp'], '%Y-%m-%d %H:%M:%S')
        year_month = f"{ts.year}-{ts.month:02d}"
        for tag in tweet.get('hashtags', []):
            print(f"{year_month}\t{tag}")
    except:
        continue
