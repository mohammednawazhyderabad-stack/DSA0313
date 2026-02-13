import nltk

words = ["I", "am", "learning", "Natural", "Language", "Processing"]

tags = nltk.pos_tag(words)
print(tags)
