"""
[2020-03-09] Challenge #383 [Easy] Necklace matching

https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/

Challenge

Imagine a necklace with lettered beads that can slide along the string. Here's an example image. In this example, you could take the N off NICOLE and slide it around to the other end to make ICOLEN. Do it again to get COLENI, and so on. For the purpose of today's challenge, we'll say that the strings "nicole", "icolen", and "coleni" describe the same necklace.

Generally, two strings describe the same necklace if you can remove some number of letters from the beginning of one, attach them to the end in their original ordering, and get the other string. Reordering the letters in some other way does not, in general, produce a string that describes the same necklace.

Write a function that returns whether two strings describe the same necklace.
Examples

same_necklace("nicole", "icolen") => true
same_necklace("nicole", "lenico") => true
same_necklace("nicole", "coneli") => false
same_necklace("aabaaaaabaab", "aabaabaabaaa") => true
same_necklace("abc", "cba") => false
same_necklace("xxyyy", "xxxyy") => false
same_necklace("xyxxz", "xxyxz") => false
same_necklace("x", "x") => true
same_necklace("x", "xx") => false
same_necklace("x", "") => false
same_necklace("", "") => true

Optional Bonus 1

If you have a string of N letters and you move each letter one at a time from the start to the end, you'll eventually get back to the string you started with, after N steps. Sometimes, you'll see the same string you started with before N steps. For instance, if you start with "abcabcabc", you'll see the same string ("abcabcabc") 3 times over the course of moving a letter 9 times.

Write a function that returns the number of times you encounter the same starting string if you move each letter in the string from the start to the end, one at a time.

repeats("abc") => 1
repeats("abcabcabc") => 3
repeats("abcabcabcx") => 1
repeats("aaaaaa") => 6
repeats("a") => 1
repeats("") => 1

Optional Bonus 2

There is exactly one set of four words in the enable1 word list that all describe the same necklace. Find the four words.

"""

all_words = dict()
matches   = dict()

def same_necklace(a, b):
	if len(a) != len(b):
		return False
	return True if a in 2*b else False

def repeats(a):
	if len(a) == 0:
		return 1
	count = 0
	b = a[1:]+a[0]
	for _ in range(len(a)):
		if a == b:
			count += 1
		b = b[1:]+b[0]
	return count

print(same_necklace("nicole", "icolen"))# => true
print(same_necklace("nicole", "lenico"))#  => true
print(same_necklace("nicole", "coneli"))#  => false
print(same_necklace("aabaaaaabaab", "aabaabaabaaa"))#  => true
print(same_necklace("abc", "cba"))#  => false
print(same_necklace("xxyyy", "xxxyy"))#  => false
print(same_necklace("xyxxz", "xxyxz"))#  => false
print(same_necklace("x", "x"))#  => true
print(same_necklace("x", "xx"))#  => false
print(same_necklace("x", ""))#  => false
print(same_necklace("", ""))#  => true

print(repeats("abc"))# => 1
print(repeats("abcabcabc"))# => 3
print(repeats("abcabcabcx"))# => 1
print(repeats("aaaaaa"))# => 6
print(repeats("a"))# => 1
print(repeats(""))# => 1

with open("./enable1.txt") as infile:
	for line in infile.readlines():
		size = len(line.strip())
		if size >= 4:
			if size not in all_words:
				all_words[size] = [ line.strip() ]
			else:
				all_words[size].append(line.strip())

for size, words in all_words.items():
	for index, word in enumerate(words):
		for z in range(index+1,len(words)):
			if same_necklace(word, words[z]):
				if word in matches:
					matches[word].append(words[z])
				else:
					matches[word] = [words[z]]
	for entry in matches:
		if len(matches[entry]) == 3:
			print(entry, ' '.join(matches[entry]))
			exit()
	matches = dict()

