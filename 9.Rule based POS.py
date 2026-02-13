import re

rules = [
    (r'^\d+$', 'CD'),
    (r'^(i|you|he|she|we|they)$', 'PRP'),
    (r'^(a|an|the)$', 'DT'),
    (r'.*ing$', 'VB'),
    (r'.*ly$', 'RB'),
    (r'.*', 'NN')
]

def pos_tag(sentence):
    words = sentence.lower().split()
    for word in words:
        for pattern, tag in rules:
            if re.match(pattern, word):
                print(word, "->", tag)
                break

pos_tag("She is running quickly")
