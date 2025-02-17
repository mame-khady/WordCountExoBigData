from collections import Counter

with open("Senegal.txt", "r", encoding="utf-8") as f:
    text = f.read()

words = text.lower().split()


word_counts = Counter(words)

for word, count in word_counts.items():
    print(f"{word}: {count}")
