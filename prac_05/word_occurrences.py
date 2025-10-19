text = input("Text: ")
word_count = {}
words = text.split()
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

max_length = 0
for word in word_count:
    if len(word) > max_length:
        max_length = len(word)

print("\nWord counts: ")
for word in sorted(word_count.keys()):
    count = word_count[word]
    print(f"{word:{max_length}} : {count}")
