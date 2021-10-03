
"""

[2016-02-01] Challenge #252 [Easy] Sailors and monkeys and coconuts, oh my!

This exercise is inspired by a Numberphile video (no need to watch past 2:00).
Description

A number of sailors (let's call it N) are stranded on an island with a huge pile of coconuts and a monkey. During the night, each sailor (in turn) does the following without the others knowing:

    He takes one N'th (e.g. if N=5, one fifth) of the coconuts in the pile and hides them

    The division leaves one coconut left over, which is given to the monkey.

In the morning, they split the remaining coconuts between them. This time the split is even. There's nothing left over for the monkey.

Your task: Given the number of sailors (N), how many coconuts were in the pile to begin with (lowest possible number)?
Formal inputs/outputs
Input

The input is a single number: N, the number of sailors. This number is a whole number that is greater than or equal to 2.
Output

The output is a single number: the number of coconuts in the original pile.
Sample input/output

Input:

5

Output:

3121

Sample solution for 5 sailors: https://jsfiddle.net/722gjnze/8/
Credit

This challenge was originally suggested on r/dailyprogrammer_ideas by /u/TinyLebowski (prior to some changes by me). Have a cool challenge idea? Hop on over to r/dailyprogrammer_ideas to tell everyone about it!

"""

def solve(N):
	trial = 0
	while True:
		trial += 1
		coconuts = trial
		solved = True
		for step in range(N):
			if coconuts % N != 1:
				solved = False
				break
			coconuts -= (coconuts//N) + 1
		if solved and coconuts % N == 0:
			return trial

print(solve(5))
