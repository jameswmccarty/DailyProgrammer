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

Consider the numbers X in the range 1 to 10,000 inclusive. The sum of all X such that 10^19 + X is a practical number is 1,451,958. Find the sum of all X such that 10^20 + X is a practical number. I found the section Characterization of practical numbers in the Wikipedia article useful here. 

https://en.wikipedia.org/wiki/Practical_number
https://www.youtube.com/watch?v=IlZOLwf87gM

Bonus (offset=10^19) 1451958
Bonus (offset=10^20) 1493108
"""

import math

# return a list of a number's divisors (largest first)
def factor(num):
	return [ i for i in range(1,num//2+1) if num%i == 0 ][::-1]

# return a dictionary of { prime_factor : count }
def prime_factor(num):
	factors = dict()
	i = 2
	while num > 1:
		if num%i == 0:
			if i in factors:
				factors[i] += 1
			else:
				factors[i] = 1
			num //= i
		else:
			i += 1
	return factors

# return a dictionary of { prime_factor : count } | faster
def prime_factor2(num):
	factors = dict()
	if num % 2 == 0:
		factors[2] = 0
	while num % 2 == 0:
		factors[2] += 1
		num //= 2
	i = 3
	while i * i <= num:
		if num%i == 0:
			factors[i] = 0
			while num%i == 0:
				factors[i] += 1
				num //= i
		else:
			i += 2
	if num != 1:
		if num in factors:
			factors[num] += 1
		else:
			factors[num] = 1
	return factors

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
# Perform check by finding a valid summation
def practical(num):
	if num != 1 and num%2 == 1:
		return False
	if num > 2 and not (num%4 == 0 or num%6 == 0):
		return False
	factors = factor(num)
	return all( sums_to(i,factors,sum(factors)) for i in range(1,num) )

# p_n <= 1 + sigma(p_1*p_2*...*p_n-1)
# don't short circuit, but use memoization 
hit_map = dict()
def sigma_check_memo(p,p_last_sum):
	global hit_map
	if p_last_sum in hit_map:
		if p <= hit_map[p_last_sum]:
			return True
		else:
			return False
	total = 1
	for k in range(1,int(math.sqrt(p_last_sum)+1)):
		if p_last_sum%k == 0:
			if k == (p_last_sum/k):
				total += k
			else:
				total = total + k + (p_last_sum//k)
	hit_map[p_last_sum] = total
	if p <= total:
		return True
	return False

# p_n <= 1 + sigma(p_1*p_2*...*p_n-1)
# break as soon as possible
def sigma_check_short(p,p_last_sum):
	total = 1
	for k in range(1,int(math.sqrt(p_last_sum)+1)):
		if p_last_sum%k == 0:
			if k == (p_last_sum/k):
				total += k
			else:
				total = total + k + (p_last_sum//k)
			if p <= total:
				return True
	return False

# p_n <= 1 + sigma(p_1*p_2*...*p_n-1)
# use memoization with short circuiting
sigma_done = dict() # { num : 1+sum_divisors }
sigma_prog = dict() # { num : (1+sum_so_far,last_k) }
def sigma_check(p,p_last_sum):
	global sigma_done,sigma_prog
	last_k = 0
	total  = 1
	if p_last_sum in sigma_done:
		if p <= sigma_done[p_last_sum]:
			return True
		return False
	if p_last_sum in sigma_prog:
		total,last_k = sigma_prog[p_last_sum]
		if p <= total:
			return True
	for k in range(last_k+1,int(math.sqrt(p_last_sum)+1)):
		if p_last_sum%k == 0:
			if k == (p_last_sum/k):
				total += k
			else:
				total = total + k + (p_last_sum//k)
			if p <= total:
				sigma_prog[p_last_sum] = (total,k)
				return True
	sigma_done[p_last_sum] = total
	return False

# return True if num is a practical number
# Use prime factorization rules
def practical2(num):
	if num != 1 and num%2 == 1:
		return False
	if num > 2 and not (num%4 == 0 or num%6 == 0):
		return False
	prime_count = prime_factor2(num)
	prime_factors = sorted(prime_count.keys())
	if len(prime_factors) == 1 and prime_factors[0] == 2:
		return True
	for i in range(1,len(prime_factors)):
		p_sum = 1
		for j in range(i):
			p_sum *= (prime_factors[j] ** prime_count[prime_factors[j]])
		if not sigma_check(prime_factors[i],p_sum):
			return False
	return True

# return True if num is a practical number
# Prime factorization can be slow...check as we go
def practical3(num):
	if num != 1 and num%2 == 1:
		return False
	if num > 2 and not (num%4 == 0 or num%6 == 0):
		return False
	factors = dict()
	p_sum = 1
	last_len = 0
	if num % 2 == 0:
		factors[2] = 0
		while num % 2 == 0:
			factors[2] += 1
			num //= 2
	if len(factors.keys()) > 0:
		last_len = 1
	i = 3
	while i * i <= num:
		if num%i == 0:
			factors[i] = 0
			while num%i == 0:
				factors[i] += 1
				num //= i
		if len(factors.keys()) > last_len:
			last_len += 1
			if last_len > 1:
				prime_factors = sorted(factors.keys())
				p_sum *= (prime_factors[-2] ** factors[prime_factors[-2]])
				if not sigma_check(prime_factors[-1],p_sum):
					return False
		i += 2
	if num != 1:
		if num in factors:
			factors[num] += 1
		else:
			factors[num] = 1
	if len(factors.keys()) > last_len:
		prime_factors = sorted(factors.keys())
		last_len += 1
		if last_len > 1:
			prime_factors = sorted(factors.keys())
			p_sum *= (prime_factors[-2] ** factors[prime_factors[-2]])
			if not sigma_check(prime_factors[-1],p_sum):
				return False
	return True


print(practical(1))
print(practical(2))
print(practical(3))
print(practical(10))
print(practical(12))
print()
print(practical2(1))
print(practical2(2))
print(practical2(3))
print(practical2(10))
print(practical2(12))
print()
print(practical3(1))
print(practical3(2))
print(practical3(3))
print(practical3(10))
print(practical3(12))

#print(prime_factor(100))
#print(prime_factor(429606))
#print(prime_factor(10000000000000000000))
#print(factor(18))

total = 0
for i in range(1,10001):
	if practical3(i):
		total += i
print(total)

offset = 10000000000000000000
total = 0
for i in range(1,10001):
	#print(i)
	if practical3(i+offset):
		total += i
print(total)

#print(sum([ i for i in range(1,10001) if practical3(i+offset) ]))
