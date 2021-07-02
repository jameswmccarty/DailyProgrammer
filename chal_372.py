"""

https://www.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/

[2019-01-14] Challenge #372 [Easy] Perfectly balanced

Given a string containing only the characters x and y, find whether there are the same number of xs and ys.

balanced("xxxyyy") => true
balanced("yyyxxx") => true
balanced("xxxyyyy") => false
balanced("yyxyxxyxxyyyyxxxyxyx") => true
balanced("xyxxxxyyyxyxxyxxyy") => false
balanced("") => true
balanced("x") => false

Optional bonus

Given a string containing only lowercase letters, find whether every letter that appears in the string appears the same number of times. Don't forget to handle the empty string ("") correctly!

balanced_bonus("xxxyyyzzz") => true
balanced_bonus("abccbaabccba") => true
balanced_bonus("xxxyyyzzzz") => false
balanced_bonus("abcdefghijklmnopqrstuvwxyz") => true
balanced_bonus("pqq") => false
balanced_bonus("fdedfdeffeddefeeeefddf") => false
balanced_bonus("www") => true
balanced_bonus("x") => true
balanced_bonus("") => true

Note that balanced_bonus behaves differently than balanced for a few inputs, e.g. "x"


"""

def balanced(string):
	if string.count('x') == string.count('y'):
		return True
	return False

def balanced_bonus(string):
	count = len({ string.count(x) for x in set(string) })
	if count == 1 or count == 0:
		return True
	return False

print(balanced("xxxyyy"))# => true
print(balanced("yyyxxx"))# => true
print(balanced("xxxyyyy"))# => false
print(balanced("yyxyxxyxxyyyyxxxyxyx"))# => true
print(balanced("xyxxxxyyyxyxxyxxyy"))# => false
print(balanced(""))# => true
print(balanced("x"))# => false
print('-')
print(balanced_bonus("xxxyyyzzz"))# => true
print(balanced_bonus("abccbaabccba"))#  => true
print(balanced_bonus("xxxyyyzzzz"))# => false
print(balanced_bonus("abcdefghijklmnopqrstuvwxyz"))#  => true
print(balanced_bonus("pqq"))#  => false
print(balanced_bonus("fdedfdeffeddefeeeefddf"))#  => false
print(balanced_bonus("www"))#  => true
print(balanced_bonus("x"))#  => true
print(balanced_bonus(""))#  => true



