n = int(input())
reverse = 0
temp = n
while temp:
	reverse = reverse * 10 + temp % 10
	temp //= 10
if n == reverse:
	print("%d is Palindrome"%n)
else:
	print("%d is not Palindrome"%n)