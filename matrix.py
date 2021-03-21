l = [[10, 20, 30], 
	[40, 50, 60], 
	[70, 80, 90]]
print(l)

print()
for i in l:
	print(i)

print()	
for i in range(len(l)):
	for j in range(len(l)):
		print(l[i][j], end = ' ')
	print()

print()	
for i in range(len(l)):
	for j in range(len(l[i])):
		if i == j:
			print(l[i][j], end = ' ')
		else:
			print(end = '   ')
	print()

print()
# Transpose of a matrix
l = [[10, 20, 30], 
	[40, 50, 60], 
	[70, 80, 90]]
	
for i in range(len(l)):
	for j in range(len(l[i])):
		print(l[j][i], end = ' ')
	print()
 