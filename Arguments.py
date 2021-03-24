# Types of Arguments

# 1. Positional Arguments
# 2. Keyword Arguments
# 3. Default Arguments
# 4. Variable length Arguments

# Positional Arguments
def add(n1, n2):
	print(n1 + n2)
	
add(10, 20)

# Keyword Arguments

def wish(name, msg):
	print('Hi', name, msg)
	
wish(msg = 'Welcom', name = 'Python')
wish(name = 'Welcom', msg = 'Python')
wish('Welcom', msg = 'Python')
#wish(name = 'Welcom', 'Python') # Show an error

# Default Arguments
def wish(a, n, name = 'Admin'):
	print('Hi', name, n, a)

wish(20, 10, name = 'Python')
wish(10, 20)

# Variable Length Arguments

def CalculateTot(*n):
	total = 0
	for subject in n:
		total += subject
	print(total)

CalculateTot(90)
CalculateTot(100, 39, 4)
CalculateTot(123, 49, 99, 49, 49)
CalculateTot()


# Keyword Variable Length Arguments
def CalculateTot(**n):#key word arguments --> dictionary
	for sub, mark in n.items():
		print(sub, 'scored', mark)

CalculateTot(tamil = 90)
CalculateTot(tamil = 100, english = 39, maths = 4)
#CalculateTot()


# Function --> set or group of instructions with a name

# Module --> Set or group of functions saved to a file

# Library --> set or group of modules
