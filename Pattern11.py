'''

'''
row = 5
while row >= 1:
	col = 1
	while col < row:
		print(' ', end = ' ')
		col += 1
	col = 5
	while col >= row:
		print('*', end = ' ')
		col -= 1
	print()
	row -= 1
row = 5
while row > 1:
	col = 5
	while col >= row:
		print(' ', end = ' ')
		col -= 1
	col = 2
	while col <= row:
		print('*', end = ' ')
		col += 1
	print()
	row -= 1