# Fibonacci Series

a, b = -1, 1
i = 0
while i < 20:
	print(a + b, end = ' ')
	a, b = b, a + b 
	i += 1


print()
# Nth Fibonacci number
# Binet's Formula

def fibo(n):
	#n = n - 1
	return int(((((1 + 5 ** (1 / 2)) / 2) ** n) - (((1 - 5 ** (1 / 2)) / 2) ** n)) / (5 ** (1 / 2)))
print(fibo(int(input())))