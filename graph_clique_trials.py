#!/usr/bin/python

import random

edges = set()
vertices = list()
degrees = list()
vertex_count = 20

def find_k_clique(k):
	if k == 1: # nodes by themselves
		return set(vertices)
	if k == 2: # we already have this
		return edges
	# nodes in a k-clique must have at least degree k-1
	search_vert = { v for idx,v in enumerate(vertices) if degrees[idx] >= k-1 }
	# only keep edges between vertices of high enough degree
	n_edges = [ e for e in edges if e[0] in search_vert and e[1] in search_vert ]
	for i in range(3,k+1):
		next_edges = set() # build the 'i' sized clique
		while len(n_edges) > 0:
			e = n_edges.pop()
			for v in search_vert:
				if all( tuple(sorted([v,e[j]])) in edges for j in range(i-1) ):
					next_edges.add(tuple(sorted(list(e)+[v])))
		print("Done with size:",i)
		n_edges = list(next_edges)
	return n_edges

def find_max_clique():
	search_vert = set(vertices)
	n_edges = list(edges)
	for i in range(3,max(degrees)+2):
		last_set = set(n_edges)
		next_edges = set() # build the 'i' sized clique
		search_vert = { v for idx,v in enumerate(vertices) if degrees[idx] >= i-1 }
		while len(n_edges) > 0:
			e = n_edges.pop()
			for v in search_vert:
				if all( tuple(sorted([v,e[j]])) in edges for j in range(i-1) ):
					next_edges.add(tuple(sorted(list(e)+[v])))
		print("Done with size:",i)
		n_edges = list(next_edges)
		if len(n_edges) == 0:
			return last_set
	return n_edges

edges = set()
for i in range(vertex_count):
	vertices.append(i)
	degree = 0
	for j in range(i+1,vertex_count):
		if random.choice([True,False]):
			edges.add(tuple(sorted([i,j])))

for i in range(vertex_count):
	degree = 0
	for j in range(vertex_count):
		if tuple(sorted([i,j])) in edges:
			degree += 1
	degrees.append(degree)

print(edges)
sol = find_max_clique()
print(sol)
