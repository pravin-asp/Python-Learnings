# while loop 


# Addition of first n numbers
amount = 1
days = int(input('Enter the max range : '))
box = 0
while amount <= days:
	box += amount 
	amount += 1 
print(box)

# Print a string letter by letter 
name = input('What is your name : ')
length = len(name)
index = 0
while index < length:
	print(name[index])
	index += 1
	
	
# Print a particular letter in a string 
name = 'Praivn'
lenght = len(name)
index = 0
while index < length:
	if name[index] == 'a':
		print(name[index])
	index += 1
	
	
# Break and Continue
print()
n = 0
while n < 10:
	n += 1
	if n == 5:
		break
	print(n)

	
print()
n = 0
while n < 10:
	n += 1
	if n == 5:
		continue 
	print(n)
	
	
# Vowels count in a string 
name = input()
length = len(name) 

i = 0
while i < lenght:
	if name[i] == 'a' or name[i] == 'e' or name[i] == 'i' or name[i] == 'o' or name[i] == 'u':
		print(name[i])
	i += 1