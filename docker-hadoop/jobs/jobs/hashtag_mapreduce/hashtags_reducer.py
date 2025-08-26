#!/usr/bin/env python3
import sys
from collections import defaultdict

counts = defaultdict(int)

for line in sys.stdin:
    ym, tag = line.strip().split("\t")
    counts[(ym, tag)] += 1

# Regrouper par mois
from itertools import groupby
for ym, group in groupby(sorted(counts.items()), key=lambda x: x[0][0]):
    hashtags = [(tag, count) for (_, tag), count in group]
    top10 = sorted(hashtags, key=lambda x: x[1], reverse=True)[:10]
    for tag, count in top10:
        print(f"{ym}\t{tag}\t{count}")
