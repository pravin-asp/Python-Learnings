'''
- - - - - 5
- - - - 4 4
- - - 3 3 3
- - 2 2 2 2
- 1 1 1 1 1
'''
row = 5
while row >= 1:
	col = 1
	while col <= row:
		print('-', end = ' ')
		col += 1
	col = 5
	while col >= row:
		print(row, end = ' ')
		col -= 1
	print()
	row -= 1
print()
print()
'''
        5
      4 4
    3 3 3
  2 2 2 2
1 1 1 1 1
'''
row = 5
while row >= 1:
	col = 1
	while col < row:
		print(' ', end = ' ')
		col += 1
	col = 5
	while col >= row:
		print(row, end = ' ')
		col -= 1
	print()
	row -= 1
print()
print()
'''
        5
      4   4
    3   3   3
  2   2   2   2
1   1   1   1   1
'''
row = 5
while row >= 1:
	col = 1
	while col < row:
		print(' ', end = ' ')
		col += 1
	col = 5
	while col >= row:
		print(row, ' ', end = ' ')
		col -= 1
	print()
	row -= 1
print()
print()	
'''
        5
      5   4
    5   4   3
  5   4   3   2
5   4   3   2   1
'''
row = 5
while row >= 1:
	col = 1
	while col < row:
		print(' ', end = ' ')
		col += 1
	col = 5
	while col >= row:
		print(col, ' ', end = ' ')
		col -= 1
	print()
	row -= 1
print()
print()	
'''
        5
    3   3   3
1   1   1   1   1
'''
row = 5
while row >= 1:
	col = 1
	while col < row:
		print(' ', end = ' ')
		col += 1
	col = 5
	while col >= row:
		print(row, ' ', end = ' ')
		col -= 1
	print()
	row -= 2
	
print()
print()	
'''
        1
      1   2
    1   2   3
  1   2   3   4
1   2   3   4   5
'''
row = 5
while row >= 1:
	col = 1
	while col < row:
		print(' ', end = ' ')
		col += 1
	col = 5
	val = 1
	while col >= row:
		print(val, ' ', end = ' ')
		col -= 1
		val += 1
	print()
	row -= 1
print()
print()	
'''
        1
      1   2
    1   2   3
  1   2   3   4
1   2   3   4   5
'''
row = 5
val = 1
while row >= 1:
	col = 1
	while col < row:
		print(' ', end = ' ')
		col += 1
	col = 5
	while col >= row:
		print(val, ' ', end = ' ')
		col -= 1
	val += 1
	print()
	row -= 1
	
print()
print()