"""
[2015-10-19] Challenge #237 [Easy] Broken Keyboard
Description

Help! My keyboard is broken, only a few keys work any more. If I tell you what keys work, can you tell me what words I can write?

(You should use the trusty enable1.txt file, or /usr/share/dict/words to chose your valid English words from.)
Input Description

You'll be given a line with a single integer on it, telling you how many lines to read. Then you'll be given that many lines, each line a list of letters representing the keys that work on my keyboard. Example:

3
abcd
qwer
hjklo

Output Description

Your program should emit the longest valid English language word you can make for each keyboard configuration.

abcd = bacaba
qwer = ewerer
hjklo = kolokolo

Challenge Input

4
edcf
bnik
poil
vybu

Challenge Output

edcf = deedeed
bnik = bikini
poil = pililloo
vybu = bubby
"""

search_dict = dict()

with open("./enable1.txt","r") as infile:
	for line in infile.readlines():
		key = ''.join(sorted( { x for x in line.strip() } ))
		if key in search_dict and len(line.strip()) >= len(search_dict[key]):
			search_dict[key] = line.strip()
		elif key not in search_dict:
			search_dict[key] = line.strip()

for puzz in ['abcd','qwer','hjklo','edcf','bnik','poil','vybu']:
	max_word_len = 0
	solution = None
	for k,v in search_dict.items():
		if set(k).issubset(set(puzz)) and len(v) > max_word_len:
			solution = v
			max_word_len = len(v)
	print(puzz,' = ',solution)
