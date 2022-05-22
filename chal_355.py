"""
[2018-03-28] Challenge #355 [Intermediate] Possible Number of Pies
Description

It's Thanksgiving eve and you're expecting guests over for dinner tomorrow. Unfortunately, you were browsing memes all day and cannot go outside to buy the ingredients needed to make your famous pies. You find some spare ingredients, and make do with what you have. You know only two pie recipes, and they are as follows:
Pumpkin Pie

    1 scoop of synthetic pumpkin flavouring (Hey you're a programmer not a cook)

    3 eggs

    4 cups of milk

    3 cups of sugar

Apple Pie

    1 apple

    4 eggs

    3 cups of milk

    2 cups of sugar

Your guests have no preference of one pie over another, and you want to make the maximum number of (any kind) of pies possible with what you have. You cannot bake fractions of a pie, and cannot use fractions of an ingredient (So no 1/2 cup of sugar or anything like that)
Input Format

You will be given a string of 4 numbers separated by a comma, such as 10,14,10,42,24. Each number is a non-negative integer. The numbers represent the number of synthetic pumpkin flavouring, apples, eggs, milk and sugar you have (In the units represented in the recipes).

For instance, in the example input 10,14,10,42,24, it would mean that you have

    10 scoops of synthetic pumpkin flavouring

    14 apples

    10 eggs

    42 cups of milk

    24 cups of sugar

Output Format

Display the number of each type of pie you will need to bake. For the example input, an output would be

3 pumpkin pies and 0 apple pies

Challenge Inputs

10,14,10,42,24
12,4,40,30,40
12,14,20,42,24

Challenge Outputs

3 pumpkin pies and 0 apple pies
5 pumpkin pies and 3 apple pies
5 pumpkin pies and 1 apple pies

"""

# all factors (eggs, milk, sugar) except apples or pumpkin pie mix, since those are both '1' for each case

pump_pie = (3,4,3)
appl_pie = (4,3,2)

puzzle = "10,14,10,42,24"
puzzle = "12,4,40,30,40"
#puzzle = "12,14,20,42,24"

max_pump,max_appl,eggs,milk,sugar = map(int,puzzle.split(","))

res_max_pump = 0
res_max_appl = 0
for i in range(max_pump+1):
	for j in range(max_appl+1):
		curr_eggs = i*pump_pie[0] + j*appl_pie[0]
		curr_milk = i*pump_pie[1] + j*appl_pie[1]
		curr_sugr = i*pump_pie[2] + j*appl_pie[2]
		if curr_eggs <= eggs and curr_milk <= milk and curr_sugr <= sugar:
			if (i+j) > (res_max_pump + res_max_appl):
				res_max_pump = i
				res_max_appl = j
print(res_max_pump,"pumpkin pies and",res_max_appl,"apple pies")
