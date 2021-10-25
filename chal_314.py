"""

https://www.reddit.com/r/dailyprogrammer/comments/6arlw4/20170512_chalenge_314_hard_finding_point_nemo/

[2017-05-12] Chalenge #314 [Hard] Finding Point Nemo
Description

What point on the world's oceans is furthest from any land? On Earth, it's slightly more than 1450 nautical miles from Ducie Island, Motu Nui, and Maher Island. The geographic coordinates of the real Point Nemo are: s48:52:31.748 w123:23:33.069. The point was named after Jules Verne’s submarine Captain Nemo, a Latin name that also happens to mean “no one.”

Your task today is given an ASCII art map, calculate the location of Point Nemo. The map will use ASCII symbols to shade land - mountains, grassland, desert, etc. The blank spaces are ocean. Find the spot in the ocean that is furthest away from any land.
Input Descripton

You'll be given a two integers on a line telling you how wide (in characters) the map is at its maximum and how many lines to read. Then you'll be given the ASCII art map with the land filled in. Assume the blank space is ocean. The world wraps around, too, just like a real map. Unlike the real world, however, assume this world is a cylinder - it makes the geometry a lot easier.
Output Description

Your progam should emit the location of Point Nemo as a grid coordinate in x-y (e.g. 40,25). Count the upper left corner as 0,0. Calculate the Euclidean distance and report the closest whole number position (e.g. round to the nearest x,y coordinate).
Challenge Input

80 25
 ## #     # #    #               #      #                       ## ###         
  ####   ###### ########   ######        ##### ######### #### #######
   ########## ## #####    ####    #          #####################
    #######################      ##            ### ##  #### ####  ##
	 ######### #########         ###            ##  #   ### ##   ##
#	  # #####   #######         ###                      #      #
	  #   ###       ##                          ####### 
	  #    ###                                 ###########     #
	        ###   ##                          ##############              #
#    		 ###                              ##############                #
			  ##                               #############
			#####                               ###########       ##
		  #########                             ##########      ##
		############                              #########     ##
	  ###############                              #######
	 ##############                                 #####           #########
	############### ##                               ###           ###########
	 ###############                                  #           ############
	  ############                                                ###   ####
	   #########      #                                
#	      #####
		  
		  ########                        ######               #######
		###################### ###########################  ##############
##############################################################################
"""
from collections import deque
import random

world = []
water_map = dict()
water_set = set()
width = None
height = None
move_dirs = []
for a in [-1,0,1]:
	for b in [-1,0,1]:
		move_dirs.append((a,b))
move_dirs.remove((0,0))

with open('nemo_map.txt', 'r') as infile:
	width, height = infile.readline().split(" ")
	width = int(width)
	height = int(height)
	map_part = infile.read().split('\n')
	for line in map_part:
		world.append(line + ' '*(width-len(line)))

for y, line in enumerate(world):
	for x, char in enumerate(line):
		if char == ' ':
			water_map[(x,y)] = None
			water_set.add((x,y))
world = []

for entry in water_map.keys():
	if water_map[entry] == None:
		q = deque()
		q.append(entry)
		seen = { entry }
		unroll = dict()
		while len(q) > 0:
			coord = q.popleft()
			x, y = coord
			if coord not in water_set:
				q = []
				last_coord = unroll[coord]
				step = 1
				while last_coord != entry:
					water_map[last_coord] = step
					last_coord = unroll[last_coord]
					step += 1
				water_map[entry] = step
				break
			for step in move_dirs:
				next_x, next_y = ((x+step[0])%width,y+step[1])
				if (next_x,next_y) not in seen and next_y >= 0 and next_y < height:
					seen.add((next_x, next_y))
					q.append((next_x,next_y))
					unroll[(next_x,next_y)] = coord

#for j in range(height):
#	for i in range(width):
#		if (i,j) not in water_map:
#			print('#',end='')
#		else:
#			print(water_map[(i,j)],end='')
#	print()

distance = max([ _ for _ in water_map.values() ])
print(distance, [ _ for _ in water_map.keys() if water_map[_] == distance ])
