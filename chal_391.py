"""

https://www.reddit.com/r/dailyprogrammer/comments/njxq95/20210524_challenge_391_easy_the_abacaba_sequence/

[2021-05-24] Challenge #391 [Easy] The ABACABA sequence
Background

The ABACABA sequence is defined as follows: the first iteration is the first letter of the alphabet (a). To form the second iteration, you take the second letter (b) and put the first iteration (just a in this case) before and after it, to get aba. For each subsequent iteration, place a copy of the previous iteration on either side of the next letter of the alphabet.

Here are the first 5 iterations of the sequence:

a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba

The 26th and final iteration (i.e. the one that adds the z) is 67,108,863 characters long. If you use one byte for each character, this takes up just under 64 megabytes of space.
Challenge

Write a program to print the 26th iteration of the ABACABA sequence.

If it's easier for you, it's also fine to print one character per line, instead of all the characters on a single line.

Just printing the output can take a few minutes, depending on your setup. Feel free to test it out on something smaller instead, like the 20th iteration, which is only about 1 megabyte.
Optional bonus

Complete the challenge using O(n) memory, where n is the iteration number.

If you don't know what that means, here's another way to say it that's roughly equivalent in this case. You can have as many variables as you want, but they must each hold either a single number or character, or a structure (list, vector, dict, string, map, tree, etc.) whose size never gets much larger than 26. If a function calls itself recursively, the call stack must also be limited to a depth of about 26. (This is definitely an oversimplification, but that's the basic idea. Feel free to ask if you want to know about whether any particular approach uses O(n) memory.)

(This is a repost of Challenge #56 [easy], originally posted by u/oskar_s in May 2012.)
85 comments

"""

def abacaba(step=26):
	i = 97
	string = ''
	step = max(0,min(26,step))
	while i < (97+step):
		string = string + chr(i) + string
		yield string
		i += 1

def abacaba_rec(ascii=0):
	ascii += 97
	if ascii == 97:
		return chr(97)
	else:
		return abacaba_rec(ascii-98)+chr(ascii)+abacaba_rec(ascii-98)

#for seq in abacaba():
#	print(seq)

print(abacaba_rec(0))
print(abacaba_rec(1))
print(abacaba_rec(2))
print(abacaba_rec(3))
print(abacaba_rec(4))
print(abacaba_rec(5))
print(abacaba_rec(26))

