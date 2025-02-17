#!/usr/bin/env python3
import sys

# Lire chaque ligne de l'entrée standard
for line in sys.stdin:
    words = line.strip().lower().split()
    for word in words:
        print(f"{word}\t1")  # Afficher chaque mot suivi de "1"
