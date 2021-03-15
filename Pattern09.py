'''
- - - - - 1
- - - - 2
- - - 3
- - 4
- 5
'''
row = 5
add = 1
while row >= 1:
	col = 1
	while col <= row:
		print('-', end = ' ')
		col += 1
	print(add, end = ' ')
	add += 1
	print()
	row -= 1
	
'''
- - - - - 1
- - - - 2
- - - 3
- - 4
- 5
'''
row = 5
#add = 5
while row >= 1:
	col = 1
	while col <= row:
		print('-', end = ' ')
		col += 1
	print(row, end = ' ')
	#add -= 1
	print()
	row -= 1

