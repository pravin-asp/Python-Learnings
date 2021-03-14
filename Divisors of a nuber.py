#Divisors of a given number

# 100 --> 2, 5, 10, 20, 25, 50, 100

n = 100
i = n 
while i > 0:
	if n % i == 0:
		print(i)
	i -= 1
	
print()
	
n = 100
i = 1 
while i < n:
	if n % i == 0:
		print(i)
	i += 1
	
print()
	
n = 75
nn = 100
i = 1 
while i <= nn:
	if n % i == 0 and nn % i == 0:
		print(i)
	i += 1
	
	
# GCD of Two numbers
print()
n = int(input())
n1 = int(input())
if n < n1:
	small = n 
else:
	small = n1 
i = 1
while i <= small:
	if n % i == 0 and n1 % i == 0:
		print(i, end = ' ')
	i += 1