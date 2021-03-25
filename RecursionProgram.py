# 1. Recursion --> Function calling itself
# 2. No loops while or for
# 3. Condition must be given to stop the recursion if statement

# 1 2 3 4 5

# display from 1 to 5

def display(n):# formal arguments
	print(n)
	n += 1
	if n <= 5:
		display(n)
		
display(1) # actual arguments

# Factorial Program

def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)
	
print(fact(int(input('Enter a number:'))))

# Sum of numbers
def sum(n):
	if n == 1:
		return 1
	return n + sum(n - 1)
	
print(sum(int(input('Enter a number:'))))

def sumOfDigits(n):
	if n == 0:
		return 0
	return n % 10 + sumOfDigits(n // 10)
print(sumOfDigits(int(input('Enter a number:'))))

