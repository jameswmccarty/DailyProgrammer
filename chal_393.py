"""
https://www.reddit.com/r/dailyprogrammer/comments/nucsik/20210607_challenge_393_easy_making_change/

[2021-06-07] Challenge #393 [Easy] Making change

The country of Examplania has coins that are worth 1, 5, 10, 25, 100, and 500 currency units. At the Zeroth Bank of Examplania, you are trained to make various amounts of money by using as many ¤500 coins as possible, then as many ¤100 coins as possible, and so on down.

For instance, if you want to give someone ¤468, you would give them four ¤100 coins, two ¤25 coins, one ¤10 coin, one ¤5 coin, and three ¤1 coins, for a total of 11 coins.

Write a function to return the number of coins you use to make a given amount of change.

change(0) => 0
change(12) => 3
change(468) => 11
change(123456) => 254

"""

def change(n):
	coins = [500,100,25,10,5,1]
	used  = 0
	for coin in coins:
		used += n//coin
		n    %= coin
	return used

print(change(0)) # => 0
print(change(12)) # => 3
print(change(468)) # => 11
print(change(123456)) # => 254
