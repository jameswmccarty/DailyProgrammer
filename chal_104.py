"""

https://www.reddit.com/r/dailyprogrammer/comments/11paok/10182012_challenge_104_easy_powerplant_simulation/

[10/18/2012] Challenge #104 [Easy] (Powerplant Simulation)

Description:

A powerplant for the city of Redmond goes offline every third day because of local demands. Ontop of this, the powerplant has to go offline for maintenance every 100 days. Keeping things complicated, on every 14th day, the powerplant is turned off for refueling. Your goal is to write a function which returns the number of days the powerplant is operational given a number of days to simulate.

Formal Inputs & Outputs:

Input Description:

Integer days - the number of days we want to simulate the powerplant

Output Description:

Return the number of days the powerplant is operational.

Sample Inputs & Outputs:

The function, given 10, should return 7 (3 days removed because of maintenance every third day).

"""

def num_days(n):
	return sum([True for i in range(1,n+1) if (i%3 != 0 and i%14 != 0 and i%100 != 0)])

print(num_days(10))
print(num_days(1000))
print(num_days(10000))
