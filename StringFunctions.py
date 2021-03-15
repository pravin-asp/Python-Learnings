s = 'python is very very easy'

# Find functions

print(s.find('y'))#gives the 1st index of the letter or word

print(s.rfind('y')) #gives last index of the letter or word
				#inclusive exclusive
print(s.find('y', 	5, 		30)) #gives the index of the letter or word between the range
 
position = -1
length = len(s)


# Find all letter or word that is present in the given sentence
position = s.find('y', 0, length)
print(position)
position = s.find('y', 2, length)
print(position)
position = s.find('y', 14, length)
print(position)

position = -1
# Using Loop
while True:
	position = s.find('y', position + 1, length)
	if position == -1:
		break
	print('y is present at ',position)
	
	
	