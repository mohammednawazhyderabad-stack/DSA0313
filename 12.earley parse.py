def earley(G,s,w):
 S=[set() for _ in range(len(w)+1)]
 S[0].add((s,0,tuple(G[s][0])))
 for i in range(len(w)+1):
  for A,d,b in list(S[i]):
   if b:
    X=b[0]
    if X in G:
     for r in G[X]: S[i].add((X,0,tuple(r)))
    elif i<len(w) and X==w[i]:
     S[i+1].add((A,d+1,b[1:]))
   else:
    if A==s and i==len(w): return True
 return False

G={'S':[['a','b']]}
print(earley(G,'S',['a','b']))
