"""
[2018-07-11] Challenge #365 [Intermediate] Sales Commissions
Description

You're a regional manager for an office beverage sales company, and right now you're in charge of paying your sales team they're monthly commissions.

Sales people get paid using the following formula for the total commission: commission is 6.2% of profit, with no commission for any product to total less than zero.
Input Description

You'll be given two matrices showing the sales figure per salesperson for each product they sold, and the expenses by product per salesperson. Example:

Revenue 

        Frank   Jane
Tea       120    145
Coffee    243    265

Expenses

        Frank   Jane
Tea       130     59
Coffee    143    198

Output Description

Your program should calculate the commission for each salesperson for the month. Example:

                Frank   Jane
Commission       6.20   9.49

Challenge Input

Revenue

            Johnver Vanston Danbree Vansey  Mundyke
Tea             190     140    1926     14      143
Coffee          325      19     293   1491      162
Water           682      14     852     56      659
Milk            829     140     609    120       87

Expenses

            Johnver Vanston Danbree Vansey  Mundyke
Tea             120      65     890     54      430
Coffee          300      10      23    802      235
Water            50     299    1290     12      145
Milk             67     254      89    129       76

Challenge Output

            Johnver Vanston Danbree Vansey  Mundyke
Commission       92       5     113     45       32

Credit

I grabbed this challenge from Figure 3 of an APL/3000 overview in a 1977 issue of HP Journal. If you have an interest in either computer history or the APL family of languages (Dyalog APL, J, etc) this might be interesting to you.
"""

class Employee:

	def __init__(self,employee_name):
		self.employee_name = employee_name
		self.sales         = dict()
	
	def revenue(self,product,value):
		if product not in self.sales:
			self.sales[product] = value
		else:
			self.sales[product] += value
	
	def expense(self,product,value):
		self.revenue(product,-value)
	
	def commission(self):
		return (self.employee_name, int(0.062 * sum( [ v for k,v in self.sales.items() if v > 0 ] )))

with open("chal_365_input.txt","r") as infile:
	Employees = []
	processing_expenses = False
	for line in infile.readlines():
		if line.strip() == '':
			continue
		elif line.strip() == "Revenue":
			continue
		elif line.strip() == "Expenses":
			processing_expenses = True
		elif line[0] == ' ' and len(Employees) == 0: # Employee line
			line = line.strip().split(" ")
			line = [ x for x in line if x != '' ]
			Employees = [ Employee(x) for x in line ]
		elif line[0] != ' ': # Items line
			line = line.strip().split(" ")
			line = [ x for x in line if x != '' ]
			print(line)
			for entry in range(1,len(line)):
				if processing_expenses:
					Employees[entry-1].expense(line[0],int(line[entry]))
				else:
					Employees[entry-1].revenue(line[0],int(line[entry]))

for employee in Employees:
	print(employee.commission())
				
			


