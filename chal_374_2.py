"""

https://www.reddit.com/r/dailyprogrammer/comments/aldexk/20190130_challenge_374_intermediate_the_game_of/

[2019-01-30] Challenge #374 [Intermediate] The Game of Blobs
Description

You are give a list of blobs, each having an initial position in an discrete grid, and a size. Blobs try to eat each other greedily and move around accordingly.

During each cycle, all blobs move one step (Moore neighborhood) towards another blob of smaller size (if any). This blob is chosen as the closest one, with a preference for larger ones, breaking ties as clockwise (11H < 12H > 01H).

At the end of each cycle, blobs merge (with summed size) if they are on the same location.

Return the final state of the blobs.
Example:

Given: [(0,2,1),(2,1,2)] as a list of (x,y and size)

..1    ..1    ..3
...    ..2    ...
.2.    ...    ...

Solution: [(0,2)]
Challenge

[(0,1,2),
 (10,0,2)]

[(4, 3, 4), 
 (4, 6, 2), 
 (8, 3, 2), 
 (2, 1, 3)]

[(-57, -16, 10),
 (-171, -158, 13),
 (-84, 245, 15),
 (-128, -61, 16),
 (65, 196, 4),
 (-221, 121, 8),
 (145, 157, 3),
 (-27, -75, 5)]

Bonus

Help the blobs break out of flatland.

Given: [(1,2),(4,2)]

.1..2    .1.2.    .12..    .3...

A solution: [(1,3)]

Given [(0,2,0,1),(1,2,1,2)]

..1    .21    ..3
...    ...    ...
/      /      /
...    ...    ...
2..    ...    ...

A solution [(0,2,0)]
Bonus 2

Mind that the distances can be long. Try to limit run times.
Bonus Challenges

[(6,3), 
 (-7,4), 
 (8,3), 
 (7,1)]

[(-7,-16,-16,4),
 (14,11,12,1),
 (7,-13,-13,4),
 (-9,-8,-11,3)]

.

[(-289429971, 243255720, 2),
 (2368968216, -4279093341, 3),
 (-2257551910, -3522058348, 2),
 (2873561846, -1004639306, 3)]
 
 Sorry for the confusion and late reaction. I was at an evening lecture. (Autoencoders as preprocessing for anomaly detection, cool stuff)

To clarify things:

    All blobs choose their destination at the same moment, move, and merge at the same moment.

    It's possible that you'll end up with more than 1 blob in the end.

    Larger blobs can merge, for example when moving towards a common goal.

    Often one will end up trailing another for some time.

    The clockwise rule in 2D means if you have 3 nodes at equal distance, and all equal size, say one at 1 o'clock, one at 5 and one at 11 o clock, you'll choose the one at 1.

    The clockwise rule in 3D.

    As blobs try to minimize the distance, their will be a preference for diagonal moves.

Example:

Given: [(2,0,1),(1,2,2)] as a list of (x,y and size)

A representation where x is horizontal, y is vertical. Each grid represents the state at the start of an iteration, or the final state.

..1    ..1    ..3
...    ..2    ...
.2.    ...    ...

Solution: [(0,2)] (coordinate) or [(0,2,3)] (including size)
Help the blobs break out of flatland.

Given: [(1,1),(4,2)] (x-coordinate and size)

.1..2    .1.2.    .12..    .3...

A solution: [(1)] or [(1,3)]

Given [(2,0,0,1),(0,1,1,2)] (x,y,z and size)

A representation where x is horizontal, y is vertical and z the second layer (or n others, just like a 3D array).

..1    .21    ..3
...    ...    ...
/      /      /
...    ...    ...
2..    ...    ...

A solution [(2,0,0)] or [(2,0,0,3)]
 

"""

import math

#blobs =  [(0,2,1),(2,1,2)]
blobs = [(4, 3, 4), (4, 6, 2), (8, 3, 2), (2, 1, 3)]
#blobs = [(-57, -16, 10), (-171, -158, 13), (-84, 245, 15), (-128, -61, 16), (65, 196, 4), (-221, 121, 8), (145, 157, 3), (-27, -75, 5)]

# convert a cartesian point
# to a polar form with respect
# to the origin.  Radius 'r' and
# Theta (in degrees)
def polar(x,y):
	r = math.sqrt(x*x+y*y)
	theta = int(math.atan2(y,x)*180/math.pi)
	theta = (theta + 0) % 360 #to shift the ref
	return (r,theta)	

# given index of a blob in the blobs
# list, return which one it will attempt
# to move toward, or 'None,' if there
# are no smaller blobs to target
def target_of(index):
	this_size = blobs[index][2]
	poss_targets = []
	"""
	next_smaller = None
	for i in range(index,0,-1):
		if blobs[i][3] < this_size and next_smaller == None:
			next_smaller = blobs[i][3]
			poss_targets.append(i)
		elif blobs[i][3] < this_size and blobs[i][3] == next_smaller:
			poss_targets.append(i)
	"""
	for i in range(index,-1,-1):
		if blobs[i][2] < this_size:
			poss_targets.append(i)
	if len(poss_targets) == 0:
		return None
	# convert to polar w.r.t. index of consideration
	measures = [ (x,polar(blobs[x][0]-blobs[index][0],blobs[x][1]-blobs[index][1])) for x in poss_targets ]
	# find minimum distance points
	nearest_range = min([ x[1][0] for x in measures ])
	measures = [ x for x in measures if x[1][0] == nearest_range ]
	measures = sorted(measures, key=lambda x:x[1][1]) # smallest angle
	return measures[0][0] # return index of best match

# Compute the direction that a blob will move
# if moving towards a target (provided as current index
# in the blobs list)
# solution is the delta in the X and Y direction
def move_delta(own_idx, target_idx):
	rel_x = blobs[target_idx][0] - blobs[own_idx][0]
	rel_y = blobs[target_idx][1] - blobs[own_idx][1]
	rel_x = 0 if rel_x == 0 else rel_x // abs(rel_x)
	rel_y = 0 if rel_y == 0 else rel_y // abs(rel_y)
	return (rel_x,rel_y)

while True:
	print(blobs)
	if len(blobs) == 1:
		break
	if len(set([x[2] for x in blobs])) == 1:
		break
	blobs = sorted(blobs, key=lambda x:x[2])
	targets = [ target_of(i) for i in range(len(blobs)) ]
	next_blobs = []
	# move all blobs
	for own_index in range(len(blobs)):
		if targets[own_index] == None:
			next_blobs.append(blobs[own_index])
		else:
			x,y,size = blobs[own_index]
			dx,dy    = move_delta(own_index,targets[own_index])
			x += dx
			y += dy
			next_blobs.append((x,y,size))
	# merge blobs
	blobs = []
	for i in range(len(next_blobs)):
		x, y, size = next_blobs[i]
		for j in range(i+1,len(next_blobs)):
			if next_blobs[j][0] == x and next_blobs[j][1] == y:
				size += next_blobs[j][2]
				next_blobs[j] = (x,y,0)
		if size != 0:
			blobs.append((x,y,size))
print(blobs)
			
			



