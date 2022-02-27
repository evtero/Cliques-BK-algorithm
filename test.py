from maximal_cliques.py import *

G = {1:[2,3],2:[1,3,5],3:[1,2],4:[5,6],5:[2,4,6],6:[4,5]}

I = set()
C = set()
V = set(G.keys())

print("Grafo: ", G)
cliques = []
print(enumerarCliques(C,V,I,cliques))