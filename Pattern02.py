'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

row = 5
while row >= 1:
	col = 1
	while col <= row:
		print(col, end = ' ')
		col += 1
	print()
	row -= 1