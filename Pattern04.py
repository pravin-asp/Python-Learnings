'''
6 7 8 9 10
5 6 7 8
4 5 6
3 4
2
'''

row = 5
while row >= 1:
	col = 1
	while col <= row:
		print(row + col, end = ' ')
		col += 1
	print()
	row -= 1
	
'''
5 6 7 8 9 
4 5 6 7 
3 4 5 
2 3 
1 
'''
row = 5
while row >= 1:
	col = 0
	while col < row:
		print(row + col, end = ' ')
		col += 1
	print()
	row -= 1