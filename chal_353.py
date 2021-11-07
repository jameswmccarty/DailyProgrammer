"""

https://www.reddit.com/r/dailyprogrammer/comments/82pt3h/20180307_challenge_353_intermediate/

[2018-03-07] Challenge #353 [Intermediate]
Description

I work as a waiter at a local breakfast establishment. The chef at the pancake house is sloppier than I like, and when I deliver the pancakes I want them to be sorted biggest on bottom and smallest on top. Problem is, all I have is a spatula. I can grab substacks of pancakes and flip them over to sort them, but I can't otherwise move them from the middle to the top.

How can I achieve this efficiently?

This is a well known problem called the pancake sorting problem. Bill Gates once wrote a paper on this that established the best known upper bound for 30 years.

This particular challenge is two-fold: implement the algorithm, and challenge one another for efficiency.
Input Description

You'll be given a pair of lines per input. The first line tells you how many numbers to read in the next line. The second line tells you the pancake sizes as unsigned integers. Read them in order and imagine them describing pancakes of given sizens from the top of the plate to the bottom. Example:

3
3 1 2

Output Description

Your program should emit the number of spatula flips it took to sort the pancakes from smallest to largest. Optionally show the intermediate steps. Remember, all you have is a spatula that can grab the pancakes from the 0th to the _n_th position and flip them. Example:

2 flips: 312 -> 213 -> 123

Challenge Input

8
7 6 4 2 6 7 8 7
----
8
11 5 12 3 10 3 2 5
----
10
3 12 8 12 4 7 10 3 8 10

Bonus

In a variation called the burnt pancake problem, the bottom of each pancake in the pile is burnt, and the sort must be completed with the burnt side of every pancake down. It is a signed permutation.


"""

def flipfront(arr, n):
	if n < 2 or n > len(arr):
		return None
	return arr[0:n][::-1] + arr[n:]

def flipsort(arr):
	target = sorted(arr)
	count = 0
	soft_end = len(arr)
	while arr != target:
		biggest = max(arr[:soft_end])
		if arr[soft_end-1] != biggest:
			pivot = soft_end-arr[:soft_end][::-1].index(biggest)
			if pivot > 1:
				arr = flipfront(arr,pivot)
				count += 1
			arr = flipfront(arr,soft_end)
			count += 1
		soft_end -= 1
	return count


print(flipsort([ int(x) for x in "7 6 4 2 6 7 8 7".split(" ")]))
print(flipsort([ int(x) for x in "11 5 12 3 10 3 2 5".split(" ")]))
print(flipsort([ int(x) for x in "3 12 8 12 4 7 10 3 8 10".split(" ")]))

