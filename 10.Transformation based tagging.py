def tbl(sentence):
    w = sentence.lower().split()
    t = ['NN'] * len(w)      # initial tags

    for i in range(len(w)):
        if w[i] in ['a','an','the']:
            t[i] = 'DT'
        elif w[i].endswith('ing'):
            t[i] = 'VB'

    print(list(zip(w, t)))

tbl("The boy is running")
