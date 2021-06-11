"""

[2019-02-01] Challenge #374 [Hard] Nonogram Solver
Description

A Nonogram (picross or griddlers) is a puzzle where you are given a grid with numbers indicating how many cells should be colored in that row/column. example. The more complex the grid is, the longer it can take to solve the puzzle.
Formal Inputs and Outputs
Inputs

num columns
num rows
columns
rows

Output

Draw the solved nonogram.
Example Input

5
5
"5","2,2","1,1","2,2","5"
"5","2,2","1,1","2,2","5"

Example Output

*****
** **
*   *
** **
*****

Bonus Challenge

Include color in your input (note: colors don't necessarily have a space between the numbers)


"""

h_rules = []
v_rules = []

def score_line(line):
	res = []
	c = 0
	for idx, val in enumerate(line):
		if val == 1:
			c += 1
		elif c > 0:
			res.append(c)
			c = 0
	if c > 0:
		res.append(c)
	return res

def score_row(grid, i):
	return score_line(grid[i])

def score_col(i):
	line = []
	for j in range(len(grid)):
		line.append(grid[j][i])
	return score_line(line)

def score_grid(grid):
	for i in range(len(grid)):
		if score_row(grid, i) != h_rules[i]:
			return False
	#for i in range(len(grid[0])):
	#	if score_col(i) != v_rules[i]:
	#		return False
	return True

def transpose(m):
	n = []
	for i in range(len(m)):
		n.append([ x[i] for x in m ])
	return n

def genlines(rules, length, prev=[]):
	if len(prev) == length and len(rules) == 0:
		yield prev
	if (len(prev) + sum(rules) + len(rules) - 1) <= length:
		for _ in genlines(rules, length, prev=prev+[0]):
			yield _
		if len(rules) > 0:
			m = 1 if len(rules) > 1 else 0
			for _ in genlines(rules[1:], length, prev=prev+[1]*rules[0]+[0]*m):
				yield _

def genboard(poss, res=[]):
	if len(poss) == 0:
		yield res
		return
	for x in poss[0]:
		for y in genboard(poss[1:], res=res+[x]):
			yield y

def find_unis(ruleset):
	flt = []
	for i in range(len(ruleset[0])):
		flt.append((i,set()))	
	for rule in ruleset:
		for i in range(len(flt)):
			flt[i][1].add(rule[i])
	flt = [ (x[0], tuple(x[1])) for x in flt if len(x[1]) == 1 ]
	return flt	


with open("374_input.txt", 'r') as infile:
	num_rows = int(infile.readline())
	num_cols = int(infile.readline())
	v_rules_t = infile.readline().strip().split('","')
	v_rules_t = [x.replace('"','').split(',') for x in v_rules_t]
	v_rules = []
	for rule in v_rules_t:
		v_rules.append([int(x) for x in rule])

	h_rules_t = infile.readline().strip().split('","')
	h_rules_t = [x.replace('"','').split(',') for x in h_rules_t]
	h_rules = []
	for rule in h_rules_t:
		h_rules.append([int(x) for x in rule])


#print(len(v_rules))

v = []
for rule in v_rules:
	v.append([tuple(line) for line in genlines(rule, len(v_rules))])

h = []
for rule in h_rules:
	h.append([tuple(line) for line in genlines(rule, len(h_rules))])

#for line in v:
#	print(len(line))

#for line in h:
#	print(len(line))

"""
# Brute Force Solution
for _ in genboard(v[:]):
	if score_grid(transpose(_)):
		for line in transpose(_):
			print(''.join([str(x) for x in line]).replace('1', 'X').replace('0', ' '))
"""

solved = False
h_last = -1
v_last = -1
while not solved:

	# v_idx[i] impacts hrules[i] at v_idx

	h_filter = [ (v_idx, find_unis(rule)) for v_idx, rule in enumerate(v) if len(find_unis(rule)) > 0 ]

	for v_idx, rules in h_filter:
		#print(v_idx, rules)
		for rule in rules:
			h[rule[0]] = [ x for x in h[rule[0]] if x[v_idx] == rule[1][0] ]				

	v_filter = [ (h_idx, find_unis(rule)) for h_idx, rule in enumerate(h) if len(find_unis(rule)) > 0 ]

	for h_idx, rules in v_filter:
		#print(h_idx, rules)
		for rule in rules:
			v[rule[0]] = [ x for x in v[rule[0]] if x[h_idx] == rule[1][0] ]
	if sum([ len(x) for x in v ]) == len(v) and sum([ len(x) for x in h ]) == len(h):
		solved = True
	if h_last == sum([ len(x) for x in h ]) and v_last == sum([ len(x) for x in v ]):
	# No progress, so try a brute force solution
		for _ in genboard(v[:]):
			if score_grid(transpose(_)):
				for line in transpose(_):
					print(''.join([str(x) for x in line]).replace('1', 'X').replace('0', ' '))
				exit()
	else:
		h_last = sum([ len(x) for x in h ])
		v_last = sum([ len(x) for x in v ])

for line in h:
	print(''.join([str(x) for x in line[0]]).replace('1', 'X').replace('0', ' '))


"""
                   XXX XX       
                  XXXXXXXX      
                 XXXXXXXXXX     
                 XXX   X  X     
                 XXXXX XX X     
                 XXXXX XX X     
                XXXX   X  X     
             XXXXXXXXXXXXXXX    
           XXXXXXXXXXXXXXXXXXX  
          XXXXXX XXXXXXXXXXXXXX 
         XXXXXX   X XXXXXXXXXXXX
         XXXXXX     X XXXXXXXXXX
        XXXXXXX   XX  X XXXXXXXX
        XXXXXX X X XX   X X X  X
        XXXXX   X  XXXX        X
        XXXXX XXXX X XXXX X X X 
        XXXXX   X X   XXXXXXXX  
         XXXXX XX  X   XXXXXXXX 
         XXXXXX  X  XX   X XXX  
          XXXXXX XXX  XX     X  
           XXXXXX   X   XXXXX   
X           XXXXXX  XXX         
XX           XXXXXXX   XX       
XXX  XXX   XXXXXXXXXX XXXX      
XXXXXXXXX XXXXXXXXXXXX    X     
XXXXXXXXXXXXXXXXXXXXXX    X     
 XXXXXXXXXXXXXXXXXXXXX XXXX     
  X  XXXXXXXXXXXXXXXXX    X     
   XX  XXXXXXXX XXXXX     X     
        XX     XX     XXXX      
          XXXXX  XX X   X       
                   XXXXX   
"""
# http://www.pythonchallenge.com/pc/rock/python.html
# Congrats! You made it through to the smiling python.

# "Free" as in "Free speech", not as in "free... 
# http://www.pythonchallenge.com/pc/rock/beer.html
