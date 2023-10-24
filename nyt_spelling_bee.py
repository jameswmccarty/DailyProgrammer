# center letter first in string

puzz = 'tpudime'

with open('enable1.txt','r') as infile:
	words = { w.lower().strip() for w in infile if len(w) > 4 and puzz[0] in w.lower() and set(w.lower().strip()).issubset(set(puzz)) }

print(sorted(words))
