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

'''
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
'''
row = 5
while row >= 1:
	col = 1
	while col <= row:
		print(row, end = ' ')
		col += 1
	print()
	row -= 1
	
'''
5 10 15 20 25
4 8 12 16
3 6 9
2 4
1
'''
row = 5
while row >= 1:
	col = 1
	while col <= row:
		print(col * row, end = ' ')
		col += 1
	print()
	row -= 1
	