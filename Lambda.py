# Anonymous Functions --> functions without function name

# Lambda function are Anonymous Functions

# Function will be called only once druing the entire program

sqrareOfNumber = lambda num : num * num
print(sqrareOfNumber(5))

bigOfTwo = lambda n1, n2 : n1 if n1 > n2 else n2
print(bigOfTwo(1, 2))

addition = lambda n1, n2 : n1 + n2
print(addition(20, 30))


# lambda functions

# 1. filter()
# 2. map()
# 3. reduce()

# Nested Functions

def outer():
	print('I am in outer function')
	def inner():
		print('I am in inner function')
	print('Outer to Inner')
	inner()
	
outer()