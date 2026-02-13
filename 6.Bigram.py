import random

text = "I like tea I like coffee I like milk"
words = text.split()

# Build bigram model
bg = {}
for i in range(len(words) - 1):
    bg.setdefault(words[i], []).append(words[i + 1])

word = "I"
print(word, end=" ")

for _ in range(6):
    if word not in bg:
        break
    word = random.choice(bg[word])
    print(word, end=" ")
