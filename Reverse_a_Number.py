n = int(input())
rev = 0
while n:
	rev = rev * 10 + n % 10
	n //= 10
print(rev)

# Sum of Digits of a number
n = int(input())
sumOfDigits = 0
while n:
	sumOfDigits += n % 10
	n //= 10
print(sumOfDigits)