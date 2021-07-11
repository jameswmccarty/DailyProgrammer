"""

https://www.reddit.com/r/dailyprogrammer/comments/oe9qnb/20210705_challenge_397_easy_roman_numeral/

[2021-07-05] Challenge #397 [Easy] Roman numeral comparison

For the purpose of today's challenge, a Roman numeral is a non-empty string of the characters M, D, C, L, X, V, and I, each of which has the value 1000, 500, 100, 50, 10, 5, and 1. The characters are arranged in descending order, and the total value of the numeral is the sum of the values of its characters. For example, the numeral MDCCXXVIIII has the value 1000 + 500 + 2x100 + 2x10 + 5 + 4x1 = 1729.

This challenge uses only additive notation for roman numerals. There's also subtractive notation, where 9 would be written as IX. You don't need to handle subtractive notation (but you can if you want to, as an optional bonus).

Given two Roman numerals, return whether the first one is less than the second one:

numcompare("I", "I") => false
numcompare("I", "II") => true
numcompare("II", "I") => false
numcompare("V", "IIII") => false
numcompare("MDCLXV", "MDCLXVI") => true
numcompare("MM", "MDCCCCLXXXXVIIII") => false

You only need to correctly handle the case where there are at most 1 each of D, L, and V, and at most 4 each of C, X, and I. You don't need to validate the input, but you can if you want. Any behavior for invalid inputs like numcompare("V", "IIIIIIIIII") is fine - true, false, or error.

Try to complete the challenge without actually determining the numerical values of the inputs.

"""

def numcompare(a,b):
	lex = "MDCLXVI"
	was_less = False
	while len(a) > 0 and len(b) > 0:
		if lex.index(a[0]) < lex.index(b[0]):
			return False
		was_less = False if a[0] == b[0] else True
		a = a[1:]
		b = b[1:]
	if len(b) > 0 or (len(b) == 0 and was_less):
		return True
	return False

print(numcompare("I", "I")) #=> false
print(numcompare("I", "II")) #=> true
print(numcompare("II", "I")) #=> false
print(numcompare("V", "IIII")) #=> false
print(numcompare("MDCLXV", "MDCLXVI")) #=> true
print(numcompare("MM", "MDCCCCLXXXXVIIII")) #=> false
print(numcompare("V","I")) #=>false
print(numcompare("I","V")) #=>true
