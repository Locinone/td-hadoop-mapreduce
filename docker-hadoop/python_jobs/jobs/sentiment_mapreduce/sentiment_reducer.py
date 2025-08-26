#!/usr/bin/env python3
import sys
from collections import defaultdict

daily_scores = defaultdict(list)

for line in sys.stdin:
    date, score = line.strip().split("\t")
    daily_scores[date].append(float(score))

for date, scores in daily_scores.items():
    avg = sum(scores) / len(scores)
    print(f"{date}\t{avg:.4f}")
