"""

[2018-04-30] Challenge #359 [Easy] Regular Paperfold Sequence Generator
Description

In mathematics the regular paperfolding sequence, also known as the dragon curve sequence, is an infinite automatic sequence of 0s and 1s. At each stage an alternating sequence of 1s and 0s is inserted between the terms of the previous sequence. The first few generations of the sequence look like this:

1
1 1 0
1 1 0 1 1 0 0
1 1 0 1 1 0 0 1 1 1 0 0 1 0 0

The sequence takes its name from the fact that it represents the sequence of left and right folds along a strip of paper that is folded repeatedly in half in the same direction. If each fold is then opened out to create a right-angled corner, the resulting shape approaches the dragon curve fractal.
Challenge Input

Your challenge today is to implement a regular paperfold sequence generator up to 8 cycles (it gets lengthy quickly).
Challenge Output

(With line breaks for readability)

110110011100100111011000110010011101100111001000110110001100100111011001110010
011101100011001000110110011100100011011000110010011101100111001001110110001100
100111011001110010001101100011001000110110011100100111011000110010001101100111
001000110110001100100111011001110010011101100011001001110110011100100011011000
110010011101100111001001110110001100100011011001110010001101100011001000110110
011100100111011000110010011101100111001000110110001100100011011001110010011101
1000110010001101100111001000110110001100100

"""

def fold():
	seq = '1'
	yield seq
	while True:
		old = seq
		seq += '1'
		old = old[::-1].replace('1','x').replace('0','1')
		old = old.replace('x','0')
		seq += old
		yield seq

folder = fold()
for _ in range(9):
	print(next(folder))

