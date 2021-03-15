'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
add = 1
row = 5
while row >= 1:
	col = 5
	while col >= row:
		print(add, end = ' ')
		col -= 1
		add += 1
	print()
	row -= 1
	