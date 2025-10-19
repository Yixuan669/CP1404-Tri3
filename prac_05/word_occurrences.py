text = input("Text: ")

words = text.split()

word_counts = {}
for word in words:
    word = word.lower()
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

max_length = max(len(word) for word in word_counts)

for word in sorted(word_counts.keys()):
    print(f"{word:{max_length}} : {word_counts[word]}")