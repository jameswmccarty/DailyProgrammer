"""

https://www.reddit.com/r/dailyprogrammer/comments/99d24u/20180822_challenge_366_intermediate_word_funnel_2/

[2018-08-22] Challenge #366 [Intermediate] Word funnel 2
Challenge

A word funnel is a series of words formed by removing one letter at a time from a starting word, keeping the remaining letters in order. For the purpose of this challenge, a word is defined as an entry in the enable1 word list. An example of a word funnel is:

gnash => gash => ash => ah

This word funnel has length 4, because there are 4 words in it.

Given a word, determine the length of the longest word funnel that it starts. You may optionally also return the funnel itself (or any funnel tied for the longest, in the case of a tie).
Examples

funnel2("gnash") => 4
funnel2("princesses") => 9
funnel2("turntables") => 5
funnel2("implosive") => 1
funnel2("programmer") => 2

Optional bonus 1

Find the one word in the word list that starts a funnel of length 10.
Optional bonus 2

For this bonus, you are allowed to remove more than one letter in a single step of the word funnel. For instance, you may step from sideboard to sidebar by removing the o and the final d in a single step. With this modified rule, it's possible to get a funnel of length 12:

preformationists =>
preformationist =>
preformations =>
reformations =>
reformation =>
formation =>
oration =>
ration =>
ratio =>
rato =>
rat =>
at

preformationists is one of six words that begin a modified funnel of length 12. Find the other five words.

"""
from collections import deque

all_words = set()

with open("./enable1.txt","r") as infile:
	all_words = {line.strip().lower() for line in infile.readlines() }

def funnel2(word):
	if word not in all_words:
		return 0
	else:
		longest = 1
		for i in range(len(word)):
			longest = max(longest, 1+funnel2(word[0:i]+word[i+1:]))
		return longest

def trim_set(word):
	sub_words = set()
	mask_set  = set()
	q = deque()
	q.append('1')
	q.append('0')
	while len(q) > 0:
		x = q.popleft()
		if len(x) == len(word):
			mask_set.add(x)
		else:
			q.append(x+'1')
			q.append(x+'0')
	for mask in mask_set:
		candidate = ''.join([word[idx] for idx, char in enumerate(mask) if char == '1'])
		if candidate in all_words:
			sub_words.add(candidate)
	sub_words.remove(word)
	return sub_words

def funnel2_bonus(word):
	if word not in all_words:
		return 0
	longest = 1
	for sub_word in trim_set(word):
		longest = max(longest, 1+funnel2_bonus(sub_word))
	return longest

print(funnel2("gnash"))
print(funnel2("princesses"))
print(funnel2("turntables"))
print(funnel2("implosive"))
print(funnel2("programmer"))

for word in all_words:
	if funnel2(word) == 10:
		print(word)
		break

print(funnel2_bonus("preformationists"))

search_set = { word for word in all_words if len(word) >= 13 }

for word in search_set:
	if funnel2_bonus(word) == 12:
		print(word)
