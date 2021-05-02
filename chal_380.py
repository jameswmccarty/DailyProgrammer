#!/usr/bin/python

from collections import deque
import time

"""
[2019-08-05] Challenge #380 [Easy] Smooshed Morse Code 1

https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/

For the purpose of this challenge, Morse code represents every letter as a sequence of 1-4 characters, each of which is either . (dot) or - (dash). The code for the letter a is .-, for b is -..., etc. The codes for each letter a through z are:

.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...

Normally, you would indicate where one letter ends and the next begins, for instance with a space between the letters' codes, but for this challenge, just smoosh all the coded letters together into a single string consisting of only dashes and dots.
Examples

smorse("sos") => "...---..."
smorse("daily") => "-...-...-..-.--"
smorse("programmer") => ".--..-.-----..-..-----..-."
smorse("bits") => "-.....-..."
smorse("three") => "-.....-..."

An obvious problem with this system is that decoding is ambiguous. For instance, both bits and three encode to the same string, so you can't tell which one you would decode to without more information.

Optional bonus challenges

For these challenges, use the enable1 word list. It contains 172,823 words. If you encode them all, you would get a total of 2,499,157 dots and 1,565,081 dashes.

    The sequence -...-....-.--. is the code for four different words (needing, nervate, niding, tiling). Find the only sequence that's the code for 13 different words.

    autotomous encodes to .-..--------------..-..., which has 14 dashes in a row. Find the only word that has 15 dashes in a row.

    Call a word perfectly balanced if its code has the same number of dots as dashes. counterdemonstrations is one of two 21-letter words that's perfectly balanced. Find the other one.

    protectorate is 12 letters long and encodes to .--..-.----.-.-.----.-..--., which is a palindrome (i.e. the string is the same when reversed). Find the only 13-letter word that encodes to a palindrome.

    --.---.---.-- is one of five 13-character sequences that does not appear in the encoding of any word. Find the other four.

"""

def is_pal(word):
	if len(word) == 0 or len(word) == 1:
		return True
	if word[0] != word[-1]:
		return False
	return is_pal(word[1:-1])

morse_alpha = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'
morse_alpha = morse_alpha.split(' ')
morse_dict = dict()
for i in range(26):
	morse_dict[chr(65+i)] = morse_alpha[i]

def smorse(word):
	return ''.join(morse_dict[char.upper()] for char in word)

print(smorse("sos"))
print(smorse("daily"))
print(smorse("programmer"))
print(smorse("bits"))
print(smorse("three"))

all_words = set()
word_map  = dict()

with open("enable1.txt", "r") as infile:
	all_words = { line.strip().upper() for line in infile.readlines() }

# Bonus 1
for word in all_words:
	key = smorse(word)
	if key not in word_map:
		word_map[key] = 1
	else:
		word_map[key] += 1
for k in word_map.keys():
	if word_map[k] == 13:
		print(k)

# Bonus 2
for word in all_words:
	key = smorse(word)
	if '-'*15 in key:
		print(word)

# Bonus 3
for word in all_words:
	if len(word) == 21:
		if smorse(word).count('.') == smorse(word).count('-'):
			print(word)

# Bonus 4
for word in all_words:
	if len(word) == 13 and is_pal(smorse(word)):
		print(word)

# Bonus 5
all_13 = set()
not_incl = set()
q = ['']
while len(q) > 0:
	t = q.pop(0)
	if len(t) == 13:
		all_13.add(t)
	else:
		q.append(t+'.')
		q.append(t+'-')
for item in all_13:
	used = False
	for key in word_map:
		if item in key:
			used = True
			break
	if not used:
		not_incl.add(item)
print(not_incl)

"""

[2019-08-07] Challenge #380 [Intermediate] Smooshed Morse Code 2
https://www.reddit.com/r/dailyprogrammer/comments/cn6gz5/20190807_challenge_380_intermediate_smooshed/

Smooshed Morse code means Morse code with the spaces or other delimiters between encoded letters left out. See this week's Easy challenge for more detail.

A permutation of the alphabet is a 26-character string in which each of the letters a through z appears once.

Given a smooshed Morse code encoding of a permutation of the alphabet, find the permutation it encodes, or any other permutation that produces the same encoding (in general there will be more than one). It's not enough to write a program that will eventually finish after a very long period of time: run your code through to completion for at least one example.
Examples

smalpha(".--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----..")
    => "wirnbfzehatqlojpgcvusyxkmd"
smalpha(".----...---.-....--.-........-----....--.-..-.-..--.--...--..-.---.--..-.-...--..-")
    => "wzjlepdsvothqfxkbgrmyicuna"
smalpha("..-...-..-....--.---.---.---..-..--....-.....-..-.--.-.-.--.-..--.--..--.----..-..")
    => "uvfsqmjazxthbidyrkcwegponl"

Again, there's more than one valid output for these inputs.
Optional bonus 1

Here's a list of 1000 inputs. How fast can you find the output for all of them? A good time depends on your language of choice and setup, so there's no specific time to aim for.
Optional bonus 2

Typically, a valid input will have thousands of possible outputs. The object of this bonus challenge is to find a valid input with as few possible outputs as possible, while still having at least 1. The following encoded string has 41 decodings:

......-..--...---.-....---...--....--.-..---.....---.-.---..---.-....--.-.---.-.--

Can you do better? When this post is 7 days old, I'll award +1 gold medal flair to the submission with the fewest possible decodings. I'll break ties by taking the lexicographically first string. That is, I'll look at the first character where the two strings differ and award the one with a dash (-) in that position, since - is before . lexicographically.

"""

alpha_set = { chr(i) for i in range(65,65+26) }

# BFS
def find_perm(morse):
	q = deque()
	q.append(('',alpha_set,morse))
	while len(q) > 0:
		alpha_str, a_set, m_str = q.popleft()
		if len(alpha_str) == 26:
			return alpha_str
		for elem in a_set:
			if morse_dict[elem] == m_str[0:len(morse_dict[elem])]:
				new_alpha_set = a_set.copy()
				new_alpha_set.discard(elem)
				q.append((alpha_str+elem, new_alpha_set, m_str[len(morse_dict[elem]):]))
	return None

# DFS
def find_perm2(morse, alpha='',a_set=alpha_set):
	if len(morse) == 0:
		return alpha
	for char in a_set:
		if morse_dict[char] == morse[0:len(morse_dict[char])]:
			next_set = a_set.copy()
			next_set.discard(char)
			sol = find_perm2(morse[len(morse_dict[char]):], alpha+char, next_set)
			if sol != False:
				return sol
	return False

# trial
sol = find_perm2('.--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----..')
print(sol)
print(smorse(sol))
print(smorse("wirnbfzehatqlojpgcvusyxkmd".upper()))

print("Starting time trials")
start_time = time.time()
with open("smorse2-bonus1.in", "r") as infile:
	for line in infile.readlines():
		sub_time_start = time.time()
		sol = find_perm2(line.strip())
		if sol == None:
			print("Failed to find solution for: ", line)
			exit(0)
		else:
			sub_time_stop = time.time()
			print(line.strip(), sol, str(sub_time_stop-sub_time_start))
print("Total Time: ", str(time.time()-start_time))
