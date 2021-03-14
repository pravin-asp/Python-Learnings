string = 'How are you? '
count = 1
i = 0
while i < len(string):
	if i + 1 < len(string) and string[i] == ' ':
		if string[i + 1] >= 'a' and string[i + 1] <= 'z':
			count += 1
	i += 1
print(count)


# in other languages else only for if 
# but in python else is used for if, for, while 

n = 1
while n < 10:
	print(n)
	n += 1
else:
	print("It is else part")
	
	
n = 1
while n < 10:
	print(n)
	if n == 3:
		break 
	n += 1
else:
	print("It is else part")
	
	
email = 'pravin.cs17@bitsathy.ac.in'
#print(email)
i = 0
lenght = len(email)
while i < lenght:
	if email[i] in ('0','1','2','3','4','5','6','7','8','9'):
		print(email[i], end = ' ')
	i += 1
	
print()
email = 'pravin.cs17@bitsathy.ac.in'
#print(email)
i = 0
lenght = len(email)
while i < lenght:
	if email[i] >= '0' and email[i] <= '9':
		print(email[i], end = ' ')
	i += 1
	
print()
email = 'pravin.cs17@bitsathy.ac.in'
#print(email)
i = 0
lenght = len(email)
while i < lenght:
	if email[i] >= 'a' and email[i] <= 'z':
		print(email[i], end = ' ')
	i += 1