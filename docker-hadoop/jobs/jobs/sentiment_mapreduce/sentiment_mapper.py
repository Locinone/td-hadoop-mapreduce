#!/usr/bin/env python3
import sys, json
from datetime import datetime
from textblob import TextBlob

for line in sys.stdin:
    try:
        tweet = json.loads(line)
        date = datetime.strptime(tweet['timestamp'], '%Y-%m-%d %H:%M:%S').date()
        score = TextBlob(tweet['tweet_text']).sentiment.polarity
        print(f"{date}\t{score}")
    except:
        continue
