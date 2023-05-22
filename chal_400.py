#!/usr/bin/python

"""

https://www.reddit.com/r/dailyprogrammer/comments/13m4bz1/20230519_challenge_400_intermediate_practical/

[2023-05-19] Challenge #400 [Intermediate] Practical Numbers
Background

A practical number is a positive integer N such that all smaller positive integers can be represented as sums of distinct divisors of N. For example, 12 is a practical number because all the numbers from 1 to 11 can be expressed as sums of the divisors of 12, which are 1, 2, 3, 4, and 6. (Wikipedia.) However, 10 is not a practical number, because 4 and 9 cannot be expressed as a sum of 1, 2, and 5. For more detailed explanation and examples, see this recent Numberphile video.
Challenge

Write a function that returns whether a given positive integer is a practical number.

practical(1) => true
practical(2) => true
practical(3) => false
practical(10) => false
practical(12) => true

You should be able to handle numbers up to 10,000 efficiently. The sum of all practical numbers up to 10,000 inclusive is 6,804,107. Test your code by verifying this value.

Optional bonus challenge

Consider the numbers X in the range 1 to 10,000 inclusive. The sum of all X such that 1019 + X is a practical number is 1,451,958. Find the sum of all X such that 1020 + X is a practical number. I found the section Characterization of practical numbers in the Wikipedia article useful here. 

https://en.wikipedia.org/wiki/Practical_number
https://www.youtube.com/watch?v=IlZOLwf87gM


"""

# return a list of a number's factors (largest first)
def factor(num):
	return [ i for i in range(1,num//2+1) if num%i == 0 ][::-1]

# return True if val can be expressed as a sum of value in provided list num_list
def sums_to(val,num_list,cap):
	if val == 0 or val == cap:
		return True
	elif val > 0 and len(num_list) > 0 and cap > val:
		if sums_to(val-num_list[0],num_list[1:],cap-num_list[0]):
			return True
		elif sums_to(val,num_list[1:],cap-num_list[0]):
			return True
	return False

# return True if num is a practical number
def practical(num):
	if num != 1 and num%2 == 1:
		return False
	if num > 2 and not (num%4 == 0 or num%6 == 0):
		return False
	factors = factor(num)
	return all( [ sums_to(i,factors,sum(factors)) for i in range(1,num) ] )
	
print(practical(1))
print(practical(2))
print(practical(3))
print(practical(10))
print(practical(12))

total = 0
for i in range(1,10001):
	if practical(i):
		total += i
print(total)
