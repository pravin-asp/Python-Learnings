n = int(input())
n1 = n
mul = 1
count = 0
while n // mul:
	count += 1
	mul *= 10
amstrong = 0
while n1:
	amstrong += (n1 % 10) ** count
	n1 //= 10
if n == amstrong:
	print('Amstrong Number')
else:
	print('Not Amstrong Number')