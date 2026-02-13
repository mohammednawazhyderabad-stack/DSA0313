import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'she' | 'he'
VP -> 'eats' | 'runs'
""")

parser = nltk.ChartParser(grammar)

def check_agreement(sent):
    try:
        next(parser.parse(sent.split()))
        return "Agreement Correct"
    except:
        return "Agreement Incorrect"

print(check_agreement("she eats"))
print(check_agreement("she run"))
