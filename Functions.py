# Python --> Everything is Object 100%

# Functions --> set of instructions

# print()
# id()
# round()
# input()
# keys()
# values()
# items()

# predefined functions --> Built in functions

# User defined functions --> done by the user

# function --> method

# procedure

# sub routines


# def fun(apple, water,...) --> apple, water are arguments or parameters or inputs

# def --> keyword

# def function_name(): --> how to declare a function

# for writing a function def is mandotory

def wish(greeting):# greeting --> formal arguments
	print(greeting)

wish('Happy Morning') # function calling statement

# function name : wish
# actual argument : Happy Morning

# function --> code reusability
def calculator(n1, n2):
	add = n1 + n2
	sub = n1 - n2
	mul = n1 * n2
	div = n1 // n2
	return add, sub, mul, div

a, b, c, d = calculator(100, 50)
print(a, b, c, d)
print(type(calculator(100, 50)))