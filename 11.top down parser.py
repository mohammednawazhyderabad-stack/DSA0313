w = []; i = 0

def m(x):
    global i
    if i < len(w) and w[i] == x:
        i += 1; return True
    return False

def S(): return m('the') and m('dog') and m('chased') and m('the') and m('dog')

w = "the dog chased the dog".split()
print("Valid" if S() and i == len(w) else "Invalid")
