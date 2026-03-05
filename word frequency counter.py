
words = input("Please type a sentence: ")

counter = {}

for word in words.split():
    word = word.strip().lower()
    counter[word] = counter.get(word, 0) + 1

print(counter)