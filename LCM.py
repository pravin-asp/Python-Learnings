# Least Common Multiple LCM of given two nuber

n1 = int(input('Enter number 1:'))
n2 = int(input('Enter number 2:'))

big = n1 if n1 > n2 else n2

while True:
	if big % n1 == 0 and big % n2 == 0:
		print('Least Common Multiple is ', big)
		break 
	big += 1
	
print()

# Least Common Multiple LCM of given two number upto 5 multiples

n1 = int(input('Enter number 1:'))
n2 = int(input('Enter number 2:'))

big = n1 if n1 > n2 else n2
count = 1
while True:
	if big % n1 == 0 and big % n2 == 0:
		print('Least Common Multiple is ', big)
		if count == 5:
			break
		count += 1
	big += 1
	
print()