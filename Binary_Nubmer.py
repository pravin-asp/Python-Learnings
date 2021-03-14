# Binary number conversion

n = int(input())
bin_num = 0
mul = 1
while n >= 1:
	bin_num = bin_num + (n % 2) * mul
	n //= 2
	mul *= 10
print(bin_num)	