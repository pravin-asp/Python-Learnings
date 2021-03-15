# For Loop

# in - key word in python

# Print letter by letter in a string 

name = 'Python' #input('Enter your name:')
for i in name:
	print(i)

print()

# range() --> gives the numbers upto given values - 1

for i in range(3):#gives value befor 3
	print(i)
	

print()
			# start value and end value
for i in range(100, 200):# starts from 100 and ends in 199
	print(i, end = ' ')

print()
	#start value, end value, increase by 5
for i in range(100, 200, 5):
	print(i, end = ' ')
else:
	print('abcd')
	
	
# Revese direction in for loop
print()
for i in range(50, 5, -5):
	print(i, end = ' ')