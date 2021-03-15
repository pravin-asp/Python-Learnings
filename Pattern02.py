'''
1 1 1 1 1
1 1 1 1 
1 1 1 
1 1
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