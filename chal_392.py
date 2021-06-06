"""

[2021-05-31] Challenge #392 [Intermediate] Pancake sort

https://www.reddit.com/r/dailyprogrammer/comments/np3sio/20210531_challenge_392_intermediate_pancake_sort/

Warmup

Implement the flipfront function. Given an array of integers and a number n between 2 and the length of the array (inclusive), return the array with the order of the first n elements reversed.

flipfront([0, 1, 2, 3, 4], 2) => [1, 0, 2, 3, 4]
flipfront([0, 1, 2, 3, 4], 3) => [2, 1, 0, 3, 4]
flipfront([0, 1, 2, 3, 4], 5) => [4, 3, 2, 1, 0]
flipfront([1, 2, 2, 2], 3) => [2, 2, 1, 2]

Optionally, as an optimization, modify the array in-place (in which case you don't need to return it). It's also fine to have the array be a global variable or member variable, in which case you only need to pass in the argument n.
Challenge

Given an array of integers, sort the array (smallest to largest) using the flipfront function on the entire array. For example, the array:

[3, 1, 2, 1]

may be sorted with three calls to flipfront:

flipfront([3, 1, 2, 1], 4) => [1, 2, 1, 3]
flipfront([1, 2, 1, 3], 2) => [2, 1, 1, 3]
flipfront([2, 1, 1, 3], 3) => [1, 1, 2, 3]

Make sure you correctly handle elements that appear more than once in the array!

You may not modify the array by any other means, but you may examine it however you want. You can even make a copy of the array and manipulate the copy, including sorting it using some other algorithm.
Optional bonus (hard!)

Try to minimize the number of times you call flipfront while sorting. Note that this is different from minimizing the runtime of your program.

How many flipfront calls do you require to sort this list of 10,000 integers? My record is 11,930. Can you do better?

(This is a repost of Challenge #63 [intermediate], originally posted by u/oskar_s in June 2012.)

"""

def flipfront(arr, n):
	if n < 2 or n > len(arr):
		return None
	return arr[0:n][::-1] + arr[n:]

print(flipfront([0, 1, 2, 3, 4], 2)) # => [1, 0, 2, 3, 4]
print(flipfront([0, 1, 2, 3, 4], 3)) #=> [2, 1, 0, 3, 4]
print(flipfront([0, 1, 2, 3, 4], 5)) #=> [4, 3, 2, 1, 0]
print(flipfront([1, 2, 2, 2], 3)) #=> [2, 2, 1, 2]

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
	print(tuple(arr) == tuple(target))
	return count

"""
print(flipfront([3, 1, 2, 1], 4))# => [1, 2, 1, 3]
print(flipfront([1, 2, 1, 3], 2))# => [2, 1, 1, 3]
print(flipfront([2, 1, 1, 3], 3))# => [1, 1, 2, 3]
"""

with open("gistfile1.txt","r") as infile:
	to_solve = [ int(x) for x in infile.readlines() ]

print(flipsort([3, 1, 2, 1]))
print(flipsort(to_solve))
