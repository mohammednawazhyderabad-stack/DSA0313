# Simple stochastic POS tagger using probabilities

prob_model = {
    "I": {"PRP": 1.0},
    "am": {"VBP": 1.0},
    "learning": {"VBG": 0.8, "NN": 0.2},
    "Natural": {"NNP": 1.0},
    "Language": {"NNP": 0.9, "NN": 0.1},
    "Processing": {"NNP": 0.9, "NN": 0.1}
}

sentence = ["I", "am", "learning", "Natural", "Language", "Processing"]

# Assign tag with highest probability
tags = []
for word in sentence:
    tag = max(prob_model[word], key=prob_model[word].get)
    tags.append((word, tag))

print(tags)
