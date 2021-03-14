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

print()

# Fibonacci series wihtout 3rd Variable

first = -1
second = 1
count = int(input())
i = 0
while i < count:
	second += first
	print(second, end = ' ')
	first = second - first
	i += 1