
def succ(n):
	'''
	Nodes adjacent to n are returned
	'''
	return set(G[n])

def enumerarCliques(C,V,I,cliques):
	'''
	Bron-Kerbosch Algorithm
	'''
	# check maximal clique:
	if (len(V) ==  0) and (len(I) == 0):
		cliques.append(C)	
	# exhaustive check of all nodes:
	else:
		for n in list(V):
			C2 = C.union({n}) # nodes checked
			V2 = V.intersection(succ(n)) # adjacent nodes to C not processed
			I2 = I.intersection(succ(n)) # nodes processed
			print("enumerarCliques({0},{1},{2})".format(C2,V2,I2))
			enumerarCliques(C2,V2,I2,cliques)
			V.remove(n)
			I.add(n)
	return cliques

