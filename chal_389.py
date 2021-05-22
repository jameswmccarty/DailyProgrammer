#!/usr/bin/python

"""

https://www.reddit.com/r/dailyprogrammer/comments/n94io8/20210510_challenge_389_easy_the_monty_hall_problem/

[2021-05-10] Challenge #389 [Easy] The Monty Hall problem
Background

For the purpose of today's challenge, the Monty Hall scenario goes like this:

    There are three closed doors, labeled #1, #2, and #3. Monty Hall randomly selects one of the three doors and puts a prize behind it. The other two doors hide nothing.

    A contestant, who does not know where the prize is, selects one of the three doors. This door is not opened yet.

    Monty chooses one of the three doors and opens it. The door that Monty opens (a) does not hide the prize, and (b) is not the door that the contestant selected. There may be one or two such doors. If there are two, Monty randomly selects one or the other.

    There are now two closed doors, the one the contestant selected in step 2, and one they didn't select. The contestant decides whether to keep their original choice, or to switch to the other closed door.

    The contestant wins if the door they selected in step 4 is the same as the one Monty put a prize behind in step 1.

Challenge

A contestant's strategy is given by their choices in steps 2 and 4. Write a program to determine the success rate of a contestant's strategy by simulating the game 1000 times and calculating the fraction of the times the contestant wins. Determine the success rate for these two contestants:

Alice chooses door #1 in step 2, and always sticks with door #1 in step 4.

Bob chooses door #1 in step 2, and always switches to the other closed door in step 4.
Optional bonus

Find success rates for these other contestants:

Carol chooses randomly from the available options in both step 2 and step 4.

Dave chooses randomly in step 2, and always sticks with his door in step 4.

Erin chooses randomly in step 2, and always switches in step 4.

Frank chooses door #1 in step 2, and switches to door #2 if available in step 4. If door #2 is not available because it was opened, then he stays with door #1.

Gina always uses either Alice's or Bob's strategy. She remembers whether her previous strategy worked and changes it accordingly. On her first game, she uses Alice's strategy. Thereafter, if she won the previous game, then she sticks with the same strategy as the previous game. If she lost the previous game, then she switches (Alice to Bob or Bob to Alice).

It's possible to calculate all of these probabilities without doing any simulation, of course, but today's challenge is to find the fractions through simulation.

(This is a repost of Challenge #49 [easy], originally posted by u/oskar_s in May 2012.)

"""

import random

def game(holds):
	wins = 0
	for i in range(1000):
		winner = random.choice([1,2,3])
		guess  = 1
		if holds and (guess == winner):
			wins += 1
		elif not holds:
			monty = random.choice([ x for x in range(1,4) if (x != winner and x != guess)])
			doors = {1,2,3}
			doors.discard(monty)
			doors.discard(guess)
			if list(doors)[0] == winner:
				wins += 1
	return wins/1000

alice = game(True)
bob   = game(False)

print("Alice: ", alice, "Bob: ", bob)


