n = int(input('Enter a nuber in binary format:'))
ans = 0
power = 0
while n:
	ans += (n % 10) * (2 ** power)
	power += 1
	n //= 10
else:
	print(ans)
	
import math
n = int(input('Enter a nuber in binary format:'))
ans = 0
power = 0
while n:
	ans += (n % 10) * int(math.pow(2, power))
	power += 1
	n //= 10
else:
	print(ans)