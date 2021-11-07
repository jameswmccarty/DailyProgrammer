"""

https://www.reddit.com/r/dailyprogrammer/comments/76qk58/20171016_challenge_336_easy_cannibal_numbers/

[2017-10-16] Challenge #336 [Easy] Cannibal numbers
Description

Imagine a given set of numbers wherein some are cannibals. We define a cannibal as a larger number can eat a smaller number and increase its value by 1. There are no restrictions on how many numbers any given number can consume. A number which has been consumed is no longer available.

Your task is to determine the number of numbers which can have a value equal to or greater than a specified value.
Input Description

You'll be given two integers, i and j, on the first line. i indicates how many values you'll be given, and j indicates the number of queries.

Example:

 7 2     
 21 9 5 8 10 1 3
 10 15   

Based on the above description, 7 is number of values that you will be given. 2 is the number of queries.

That means -

    Query 1 - How many numbers can have the value of at least 10

    Query 2 - How many numbers can have the value of at least 15

Output Description

Your program should calculate and show the number of numbers which are equal to or greater than the desired number. For the sample input given, this will be -

 4 2  

Explanation

For Query 1 -

The number 9 can consume the numbers 5 to raise its value to 10

The number 8 can consume the numbers 1 and 3 to raise its value to 10.

So including 21 and 10, we can get four numbers which have a value of at least 10.

For Query 2 -

The number 10 can consume the numbers 9,8,5,3, and 1 to raise its value to 15.

So including 21, we can get two numbers which have a value of at least 15.
Credit

This challenge was suggested by user /u/Lemvig42, many thanks! If you have a challenge idea, please share it in r/dailyprogrammer_ideas and there's a good chance we'll use it

"""

def run_query(numbers, hival):
	matches = 0
	numbers = sorted(numbers, reverse=True)
	print(numbers)
	while numbers[0] >= hival:
		numbers = numbers[1:]
		matches += 1
	while len(numbers) > 0:
		print(numbers)
		if numbers[0] >= hival:
			numbers = numbers[1:]
			matches += 1
		elif len(numbers) > 1 and numbers[0] > numbers[-1]:
			numbers[0] += 1
			numbers = numbers[0:-1]
		else:
			return matches
	return matches

def run_query2(numbers, hival):
	if len(numbers) == 0:
		return 0
	matches = 0
	numbers = sorted(numbers, reverse=True)
	while numbers[0] >= hival:
		numbers = numbers[1:]
		matches += 1
	while len(numbers) > 0:
		if numbers[0] >= hival:
			numbers = numbers[1:]
			matches += 1
		elif len(numbers) > 2:
			best = 0
			for idx in range(1,len(numbers)):
				if numbers[0] > numbers[idx]:
					best = max(best, run_query2([numbers[0]+1] + numbers[1:idx] + numbers[idx+1:],hival))
			return best + matches
		elif len(numbers) > 1:
			if numbers[0] > numbers[1]:
				numbers[0] += 1
				numbers = numbers[0:-1]
		else:
			return matches
	return matches

input1 = "7 2"
input2 = "21 9 5 8 10 1 3"
input3 = "10 15"

input1 = "9 1"
input2 = "3 3 3 2 2 2 1 1 1"
input3 = "4"

input1 = "5 1"
input2 = "5 2 2 1 1"
input3 = "5"

starting_nums = sorted([ int(x) for x in input2.split(" ") ], reverse=True)

for trial in [ int(x) for x in input3.split(" ") ]:
	print(run_query2(starting_nums, trial))

