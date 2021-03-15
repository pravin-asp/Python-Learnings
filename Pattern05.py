'''
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
'''

row = 5
while row >= 1:
	col = 5
	while col >= row:
		print(col, end = ' ')
		col -= 1
	print()
	row -= 1
	
'''
5
4 4
3 3 3
2 2 2 2
1 1 1 1 1
'''

row = 5
while row >= 1:
	col = 5
	while col >= row:
		print(row, end = ' ')
		col -= 1
	print()
	row -= 1
	