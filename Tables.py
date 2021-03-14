#Tables
n = 13#int(input('Enter a number:'))
i = 1
while i < 11:
	print('{} * {} = {}'.format(i, n, i * n))
	i += 1

# Tables
n = 43#int(input('Enter a number:'))
i = 1
while i < 11:
	print('%d * %d = %d'%(i, n, i * n))
	i += 1
	
# Total
subjects = int(input("Enter no. of subjects:"))
total = 0
subject = subjects
while subjects > 0:
	mark = int(input('Enter mark:'))
	total += mark 
	subjects -= 1
print('total is ', total)
print('Percentage is ', round(total/subject, 3))
