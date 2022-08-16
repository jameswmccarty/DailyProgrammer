#!/usr/bin/python
"""
Puzzle:

Try to find 5 five-letter words, that between them use 25 letters of the alphabet.

Approach:
Starting with a word list, take only words with 5 unique letters.
Normalize words and remove anagrams (keep only one anagram).
Treat words as nodes (vertices) of a graph, and add edges between nodes that have 0 letters in common.
Search graph for a 5-clique.
"""

edges = set()
vertices = list()
degrees = list()

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
		#print("Done with size:",i)
		n_edges = next_edges
	return n_edges

def normalize(word):
	return ''.join(sorted(word))

# isolate 5 letter words with unique letters
word_list = set()
with open("enable2.txt","r") as infile:
		word_list = { line.strip().lower() for line in infile.readlines() if len((line.strip())) == 5 and len(set(line.strip())) == 5 }

print(len(word_list))
# remove anagrams
anagrams = dict()
for word in word_list:
	norm_word = normalize(word)
	if norm_word in anagrams:
		anagrams[norm_word].append(word)
	else:
		anagrams[norm_word] = [word]
print(len(anagrams))

anagram_words = sorted([ v[0] for v in anagrams.values() ])
print(anagram_words)

edges = set()
for i,w1 in enumerate(anagram_words):
	vertices.append(i)
	degree = 0
	for j in range(i,len(anagram_words)):
		if len(set(w1+anagram_words[j])) == 10:
			edges.add(tuple(sorted([i,j])))
			degree += 1
	degrees.append(degree)

sol = find_k_clique(5)
print(sol)
for s in sol:
	print(','.join([ anagram_words[idx] for idx in s ]))

# Test code block
"""
vertices = [1,2,3,4,5,6,7]
n_edges = [[1,2],[1,3],[1,4],[2,1],[2,3],[2,4],[2,6],[3,1],[3,2],[3,4],[3,5],[4,1],[4,2],[4,3],[4,5],[5,3],[5,4],[6,2],[6,7],[7,6]]
degrees = [3,4,4,4,2,2,1]
edges = set()
for e in n_edges:
	edges.add(tuple(sorted(e)))
print(find_k_clique(4))
"""
