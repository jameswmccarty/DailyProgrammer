"""

https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/

[2021-07-19] Challenge #399 [Easy] Letter value sum
Challenge

Assign every lowercase letter a value, from 1 for a to 26 for z. Given a string of lowercase letters, find the sum of the values of the letters in the string.

lettersum("") => 0
lettersum("a") => 1
lettersum("z") => 26
lettersum("cab") => 6
lettersum("excellent") => 100
lettersum("microspectrophotometries") => 317

Optional bonus challenges

Use the enable1 word list for the optional bonus challenges.

    microspectrophotometries is the only word with a letter sum of 317. Find the only word with a letter sum of 319.

    How many words have an odd letter sum?

    There are 1921 words with a letter sum of 100, making it the second most common letter sum. What letter sum is most common, and how many words have it?

    zyzzyva and biodegradabilities have the same letter sum as each other (151), and their lengths differ by 11 letters. Find the other pair of words with the same letter sum whose lengths differ by 11 letters.

    cytotoxicity and unreservedness have the same letter sum as each other (188), and they have no letters in common. Find a pair of words that have no letters in common, and that have the same letter sum, which is larger than 188. (There are two such pairs, and one word appears in both pairs.)

    The list of word { geographically, eavesdropper, woodworker, oxymorons } contains 4 words. Each word in the list has both a different number of letters, and a different letter sum. The list is sorted both in descending order of word length, and ascending order of letter sum. What's the longest such list you can find?

(This challenge is a repost of Challenge #52 [easy], originally posted by u/rya11111 in May 2012.)

It's been fun getting a little activity going in here these last 13 weeks. However, this will be my last post to this subreddit for the time being. Here's hoping another moderator will post some challenges soon!

"""

def lettersum(word):
	word = ''.join([ char for char in word.lower() if (ord(char) >= 97 and ord(char) <= 122) ])
	if len(word) == 0:
		return 0
	return sum([ ord(char)-96 for char in word ])

print(lettersum(""))# => 0
print(lettersum("a"))# => 1
print(lettersum("z"))# => 26
print(lettersum("cab"))# => 6
print(lettersum("excellent"))# => 100
print(lettersum("microspectrophotometries"))# => 317

all_words = []

with open("enable1.txt", "r") as infile:
	all_words = [ line.strip() for line in infile.readlines() ]

# bonus 1
for word in all_words:
	if lettersum(word) == 319:
		print(word)
		break

# bonus 2
print(len([ word for word in all_words if lettersum(word)%2==1]))

# bonus 3
sums = dict()
for word in all_words:
	total = lettersum(word)
	if total in sums:
		sums[total] += 1
	else:
		sums[total] = 1
print(sorted(sums.items(), key=lambda x:x[1], reverse=True)[0])

# bonus 4

len_sums = dict()

for word in all_words:
	total = lettersum(word)
	size  = len(word)
	if size not in len_sums:
		len_sums[size] = [ (word,total) ]
	else:
		len_sums[size].append((word,total))

searching = True
small_length = 1
while searching:
	if small_length in len_sums and small_length + 11 in len_sums:
		smalls = { x[1] for x in len_sums[small_length] }
		bigs   = { x[1] for x in len_sums[small_length+11] }
		overlap = smalls.intersection(bigs)
		if len(overlap) > 0:
			found_size = list(overlap)[0]
			if found_size != 151:
				small_word = [ x[0] for x in len_sums[small_length]    if x[1] == found_size ]
				big_word =   [ x[0] for x in len_sums[small_length+11] if x[1] == found_size ]
				print(small_word, big_word, found_size)
				searching = False
				break
	small_length += 1

# bonus 5

len_sums = dict()
sols = set()
for word in all_words:
	total = lettersum(word)
	if total > 188:
		if total not in len_sums:
			len_sums[total] = [word]
		else:
			len_sums[total].append(word)
for key in len_sums.keys():
	for word in len_sums[key]:
		word_set = set(word)
		for trial in len_sums[key]:
			if len(set(trial).intersection(word_set)) == 0:
				sols.add(word)
				sols.add(trial)
print(sols)









