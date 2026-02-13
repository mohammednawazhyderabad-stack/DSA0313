import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'she'
VP -> 'eats'
""")

parser = nltk.ChartParser(grammar)

sentence = "she eats".split()

for tree in parser.parse(sentence):
    print(tree)
    tree.draw()
