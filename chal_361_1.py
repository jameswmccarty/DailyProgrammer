"""
https://www.reddit.com/r/dailyprogrammer/comments/8jcffg/20180514_challenge_361_easy_tally_program/

[2018-05-14] Challenge #361 [Easy] Tally Program
Description

5 Friends (let's call them a, b, c, d and e) are playing a game and need to keep track of the scores. Each time someone scores a point, the letter of his name is typed in lowercase. If someone loses a point, the letter of his name is typed in uppercase. Give the resulting score from highest to lowest.
Input Description

A series of characters indicating who scored a point. Examples:

abcde
dbbaCEDbdAacCEAadcB

Output Description

The score of every player, sorted from highest to lowest. Examples:

a:1, b:1, c:1, d:1, e:1
b:2, d:2, a:1, c:0, e:-2

Challenge Input

EbAAdbBEaBaaBBdAccbeebaec

Credit

This challenge was suggested by user /u/TheMsDosNerd, many thanks! If you have any challenge ideas, please share them in r/dailyprogrammer_ideas and there's a good chance we'll use them.

"""

def score(line):
	scores = dict()
	out = ''
	for char in line:
		if ord(char) >= 97 and ord(char) <= 122:
			if char in scores:
				scores[char] += 1
			else:
				scores[char] = 1
		elif ord(char) >= 65 and ord(char) <= 90:
			char = chr(ord(char)+32)
			if char in scores:
				scores[char] -= 1
			else:
				scores[char] = -1
	if len(scores) == 0:
		return out
	for k,v in sorted(scores.items(), key=lambda x : x[1], reverse=True):
		out += k+":"+str(v)+", "
	return out[:-2]

print(score("abcde"))
print(score("dbbaCEDbdAacCEAadcB"))
print(score("EbAAdbBEaBaaBBdAccbeebaec"))
