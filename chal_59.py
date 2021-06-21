
"""

https://www.reddit.com/r/dailyprogrammer/comments/uh03h/622012_challenge_59_intermediate/

[6/2/2012] Challenge #59 [intermediate]

Given a binary matrix like this:

0 1 1 1 1 0
1 0 0 1 1 1
1 0 1 1 1 1
1 1 1 1 1 1
0 1 1 1 1 0

Output the clues for a nonogram puzzle in the format of "top clues, empty line, bottom clues", with clues separated by spaces:

3
1 2
1 3
5
5
3

4
1 3
1 4
6
4

That is, count the contiguous groups of "1" bits and their sizes, first in columns, then in rows.

    Thanks to nooodl for suggesting this problem at r/dailyprogrammer_ideas! If you have a problem that you think would be good for us, why not head over there and post it!

"""

matrix = [[0,1,1,1,1,0],
		 [1,0,0,1,1,1],
		 [1,0,1,1,1,1],
		 [1,1,1,1,1,1],
		 [0,1,1,1,1,0]]

def nonogramrow(row):
	out = []
	count = 0
	for item in row:
		if item == 0 and count > 0:
			out.append(count)
			count = 0
		elif item == 1:
			count += 1
	if count > 0:
		out.append(count)
	return [ str(x) for x in out ]

def print_vert(matrix):
	for i in range(len(matrix[0])):
		col = []
		for j in range(len(matrix)):
			col.append(matrix[j][i])
		sol = nonogramrow(col)
		print(' '.join(sol).strip())

def print_horiz(matrix):
	for row in matrix:
		print(' '.join(nonogramrow(row)).strip())

print_vert(matrix)
print()
print_horiz(matrix)

