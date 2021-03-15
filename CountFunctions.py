# Count function

s = 'python is very very easy'
count = 0
position = 0
for x in s:
	if x == 'y':
		count += 1
		print(position)
	position += 1
else:
	print(count)
	
print(s.count('y'))

print(s.count('y', 0, 30))