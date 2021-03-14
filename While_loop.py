# While Loop

# Print 1 to 5
print(1)
print(2)
print(3)
print(4)
print(5)

# Print 1 five times 
print()
count = 0
print(1)
count += 1
print(1)
count += 1
print(1)
count += 1
print(1)
count += 1
print(1)


print()
count = 0
if count < 5:
	print(1)
count += 1
if count < 5:
	print(1)
count += 1
if count < 5:
	print(1)
count += 1
if count < 5:
	print(1)
count += 1
if count < 5:
	print(1)
	
# Print 1 five times	
print()	
count = 0
while count < 5:
	print(1)
	count += 1

	
# Print from 1 to 5
print()	
count = 1
while count <= 5:
	print(count)
	count += 1
	
	
# What should be printed
# What is the initial value ?
# What pattern you are observing
# What is the final value	
	
	
# Print from 5 to 1
print()	
count = 5
while count >= 1:
	print(count)
	count -= 1
	
	
# Print Even number from 10 to 1
print()	
count = 10
while count >= 1:
	print(count)
	count -= 2
	

# Print Even number from 1 to 10
print()	
count = 2
while count <= 10:
	print(count)
	count += 2


# Print Odd number from 1 to 10
print()	
count = 1
while count <= 10:
	print(count, sep = '-')
	count += 2

# Print Multiples of three
print()
count = 3
maxNo = int(input('Enter a maximum Number : '))
while count <= maxNo:
	print(count, end = ' ')
	count += 3
	

# Print Power of three 
print()
count = 3
maxNo = int(input('Enter a maximum Number : '))
while count <= maxNo:
	print(count, end = ' ')
	count *= 3
	
	

	
# Multiples of three from a start and end point are given
start = int(input())
end = int(input())
while start <= end:
	if start % 3 == 0:
		print(start)
	start += 1
	
	
# Multiples of two and three from a start and end point are given
start = int(input())
end = int(input())
while start <= end:
	if start % 3 == 0 and start % 2 == 0:
		print(start)
	start += 1

	
# Multiples of two or three from a start and end point are given
start = int(input())
end = int(input())
while start <= end:
	if start % 3 == 0 or start % 2 == 0:
		print(start)
	start += 1