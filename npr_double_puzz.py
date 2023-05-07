"""
On-air challenge: I'm going to give you some six-letter words. For each one add the same letter of the alphabet twice — without rearranging any of the other letters — to make a common eight-letter word.

Ex. STURDY — A --> SATURDAY
1. RESENT — C

2. COLLIE — D

3. LATISH — F

4. SEATED — H

5. FESTER — I

6. ASSORT — P

7. WANGLE — R

8. MALLET — S

9. HEDGER — A

10. REARED — P

11. TREBLE — U (hyphenated)
"""

anagram_dict = dict()

def normalize(word):
	return ''.join(sorted([ x for x in word.lower() ]))

with open('enable1.txt','r') as infile:
	words = { word.strip() for word in infile }

for word in words:
	key = normalize(word)
	if key in anagram_dict:
		anagram_dict[key] |= { word }
	else:
		anagram_dict[key] = { word }

print(anagram_dict[normalize('RESENT'+'CC')])
print(anagram_dict[normalize('COLLIE'+'DD')])
print(anagram_dict[normalize('LATISH'+'FF')])
print(anagram_dict[normalize('SEATED'+'HH')])
print(anagram_dict[normalize('FESTER'+'II')])
print(anagram_dict[normalize('ASSORT'+'PP')])
print(anagram_dict[normalize('WANGLE'+'RR')])
print(anagram_dict[normalize('MALLET'+'SS')])
print(anagram_dict[normalize('HEDGER'+'AA')])
print(anagram_dict[normalize('REARED'+'PP')])
print(anagram_dict[normalize('TREBLE'+'UU')])
