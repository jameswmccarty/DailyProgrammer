"""

https://www.reddit.com/r/dailyprogrammer/comments/o9k0p0/20210628_challenge_395_intermediate_phone_drop/

[2021-06-28] Challenge #395 [Intermediate] Phone drop
Scenario

This is a pretty common problem. You may have seen it before.

You work for a mobile phone developer known for their robust design. The marketing division is working on a slogan for the latest model: "Able to survive a K-meter drop!". They just need to know the largest possible whole number value of K they can truthfully claim. Someone has already dropped one from 101 meters up and it broke, so they know the largest possible value is somewhere between 0 and 100 inclusive.

Here's where you come in. You must find the value of K such that a phone will not break if dropped from K meters, but will break if dropped from K+1 meters. For the purpose of this challenge, these tests are completely reliable, so a single test at both K and K+1 meters is enough to establish this. Also, as long as a phone survives the drop, it suffers no damage whatsoever and can be reused in subsequent tests. Also, dropping a phone that's already broken gives you no information.

Your boss gives you a prototype and tells you to go rent the 100-meter tower nearby and find K. The tower owner needs to know how long you'll be renting the tower for, and you rent by the minute, so assuming each trial takes the same amount of time, you need to know the maximum number of trials you'll need, without knowing the value of K. You realize you'll need to rent it long enough to conduct 100 trials, one for each floor. This is because you need to conduct one trial 1 meter up, then 2 meters up, and so on up to 100. If you skip any, then it's possible you won't know the exact value of K before the phone breaks. And then if K = 100, this strategy will require 100 trials.

You tell your boss, who says it's too expensive to rent the tower for 100 tests. Your boss asks, what's the maximum number of trials you'll need if you have two phone prototypes? After some work, you find the answer is 14. Can you see how to find this number? There are many explanations online that can help, like this one. Feel free to read up on this problem if you don't understand the general approach. (https://datagenetics.com/blog/july22012/index.html)

If you have three phones, you only need a maximum of 9 trials.
Challenge

Given N, the number of phone prototypes you have, and H, the maximum height that needs to be tested, determine the maximum number of trials required by an optimal strategy to determine K.

phonedrop(1, 100) => 100
phonedrop(2, 100) => 14
phonedrop(3, 100) => 9
phonedrop(1, 1) => 1
phonedrop(2, 456) => 30
phonedrop(3, 456) => 14
phonedrop(4, 456) => 11
phonedrop(2, 789) => 40
phonedrop(3, 789) => 17
phonedrop(4, 789) => 12

You should be able to at least handle values of H up to 999.
Optional bonus

With an unlimited number of phones (N = infinity), it takes a maximum of 27 trials to find K when H = 123456789. Find the smallest N such that phonedrop(N, 123456789) = 27.

"""

memo = dict()

def phonedrop(n, height):

	global memo

	# Maximum number of floors that can be tested
	# given a number of trials (drops) and a number
	# of phones.
	
	# Theory discussed on Youtube
	# https://www.youtube.com/watch?v=xsOCvSiSrSs
	
	def maxfloors(drops,phones):
		if drops == 1 or phones == 1:
			return drops
		if (drops,phones) in memo:
			return memo[(drops,phones)]
		memo[(drops,phones)] = 1+maxfloors(drops-1,phones-1)+maxfloors(drops-1,phones)
		return memo[(drops,phones)]
	
	trials = 1
	while True:
		for phone in range(1,n+1):
			solution = maxfloors(trials,phone)
			if solution >= height:
				return trials
		trials += 1

print(phonedrop(1, 100)) # => 100
print(phonedrop(2, 100)) # => 14
print(phonedrop(3, 100)) # => 9
print(phonedrop(1, 1))   # => 1
print(phonedrop(2, 456)) # => 30
print(phonedrop(3, 456)) # => 14
print(phonedrop(4, 456)) # => 11
print(phonedrop(2, 789)) # => 40
print(phonedrop(3, 789)) # => 17
print(phonedrop(4, 789)) # => 12

# bonus
trial = 1
while phonedrop(trial,123456789) != 27:
	trial += 1
print(trial, phonedrop(trial,123456789))
