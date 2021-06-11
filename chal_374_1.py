"""

https://www.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/

[2019-01-28] Challenge #374 [Easy] Additive Persistence
Description

Inspired by this tweet, today's challenge is to calculate the additive persistence of a number, defined as how many loops you have to do summing its digits until you get a single digit number. Take an integer N:

    Add its digits

    Repeat until the result has 1 digit

The total number of iterations is the additive persistence of N.

Your challenge today is to implement a function that calculates the additive persistence of a number.
Examples

13 -> 1
1234 -> 2
9876 -> 2
199 -> 3

Bonus

The really easy solution manipulates the input to convert the number to a string and iterate over it. Try it without making the number a strong, decomposing it into digits while keeping it a number.

On some platforms and languages, if you try and find ever larger persistence values you'll quickly learn about your platform's big integer interfaces (e.g. 64 bit numbers).

"""

# easy way
def add_pers(n):
	c = 0
	while n > 9:
		n = sum([int(x) for x in str(n)])
		c += 1
	return c

def digit_sum(n):
	total = 0
	while n > 0:
		total += n % 10
		n = n//10
	return total

def add_pers2(n):
	c = 0
	while n > 9:
		n = digit_sum(n)
		c += 1
	return c

print(add_pers(13))
print(add_pers(1234))
print(add_pers(9876))
print(add_pers(199))
print(add_pers(2**39))

print(add_pers2(13))
print(add_pers2(1234))
print(add_pers2(9876))
print(add_pers2(199))
print(add_pers2(2**39))
