#!/usr/bin/env python3
import sys
from collections import defaultdict

current_location = None
word_counts = defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    location, word = line.split("\t", 1)
    
    if current_location and location != current_location:
        # afficher les 10 mots les plus fréquents pour la région
        top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        print(f"{current_location}\t{top_words}")
        word_counts.clear()
    
    current_location = location
    word_counts[word] += 1

# dernier bloc
if current_location:
    top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    print(f"{current_location}\t{top_words}")
