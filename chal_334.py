#!/usr/bin/python

"""

https://www.reddit.com/r/dailyprogrammer/comments/748ba7/20171004_challenge_334_intermediate_carpet/

Description

A Sierpinski carpet is a fractal generated by subdividing a shape into smaller copies of itself.

For this challenge we will generalize the process to generate carpet fractals based on a set of rules. Each pixel expands to 9 other pixels depending on its current color. There's a set of rules that defines those 9 new pixels for each color. For example, the ruleset for the Sierpinski carpet looks like this:

https://i.imgur.com/5Rf14GH.png

The process starts with a single white pixel. After one iteration it's 3x3 with one black pixel in the middle. After four iterations it looks like this:

https://i.imgur.com/7mX9xbR.png
Input:

To define a ruleset for your program, each of the possible colors will have one line defining its 9 next colors. Before listing these rules, there will be one line defining the number of colors and the number of iterations to produce:

<ncolors> <niterations>
<ncolors lines of rules>

For example, the input to produce a Sierpinski carpet at 4 iterations (as in the image above):

2 4
0 0 0 0 1 0 0 0 0
1 1 1 1 1 1 1 1 1

The number of colors may be greater than two.
Output:

Your program should output the given fractal using whatever means is convenient. You may want to consider using a Netpbm PGM (P2/P5), with maxval set to the number of colors in the fractal.
Challenge Input:

3 4
2 0 2 0 1 0 2 0 2
1 1 1 1 2 1 1 1 1
2 1 2 0 0 0 2 1 2

Challenge Output:

https://i.imgur.com/1piawqY.png
Bonus Input:

The bonus output will contain a secret message.

32 4
30 31 5 4 13 11 22 26 21
0 0 0 0 0 0 21 24 19
31 28 26 30 31 31 31 30 30
18 14 2 1 2 3 1 3 3
28 16 10 3 23 31 9 6 2
30 15 17 7 13 13 30 20 30
17 30 30 2 30 30 2 14 25
8 23 3 12 20 18 30 17 9
1 20 29 2 2 17 4 3 3
31 1 8 29 9 6 30 9 8
17 28 24 18 18 20 20 30 30
26 28 16 27 25 28 12 30 4
16 13 2 31 30 30 30 30 30
20 20 20 15 30 14 23 30 25
30 30 30 29 31 28 14 24 18
2 2 30 25 17 17 1 16 4
2 2 2 3 4 14 12 16 8
31 30 30 30 31 30 27 30 30
0 0 0 5 0 0 0 13 31
2 20 1 17 30 17 23 23 23
1 1 1 17 30 30 31 31 29
30 14 23 28 23 30 30 30 30
25 27 30 30 25 16 30 30 30
3 26 30 1 2 17 2 2 2
18 18 1 15 17 2 6 2 2
31 26 23 30 31 24 30 29 2
15 6 14 19 20 8 2 20 12
30 30 17 22 30 30 15 6 17
30 17 15 27 28 3 24 18 6
30 30 31 30 30 30 30 27 27
30 30 30 30 30 30 30 30 30
30 30 27 30 31 24 29 28 27


"""

from PIL import Image

# contains (color, xpos, ypos)
pixels = {(0,0,0)}
rules   = dict()
num_ittr = None

with open('334_rules.txt','r') as infile:
	header = infile.readline()
	cols, num_ittr = header.split(' ')
	num_ittr = int(num_ittr)
	index = 0
	for line in infile.readlines():
		line = [int(x) for x in line.strip().split(' ')]
		rules[index] = line
		index += 1

for _ in range(num_ittr):
	pixels = { (color,x*3,y*3) for color,x,y in pixels }
	next_pixels = set()
	for pixel in pixels:
		color, x, y = pixel
		index = 0
		for i in (-1,0,1):
			for j in (-1,0,1):
				next_pixels.add((rules[color][index],x+i,y+j))
				index += 1
	pixels = next_pixels

#rebase to zero
min_x = min([ x for color,x,y in pixels ])
min_y = min([ y for color,x,y in pixels ])
pixels = { (color,x-min_x,y-min_y) for color,x,y in pixels }
max_x = max([ x for color,x,y in pixels ])
max_y = max([ y for color,x,y in pixels ])

picture = Image.new('L',(max_x+1,max_y+1),0)
picture_data = picture.load()
for pixel in pixels:
	color, x, y = pixel
	picture_data[y,x] = 0 if color == 0 else 255//color
picture.show()

# Slow text based output
"""
for j in range(max_y):
	for i in range(max_x):
		for pixel in pixels:
			color,x,y = pixel
			if j == y and x == i:
				print(color%10,end='')
	print()
"""
