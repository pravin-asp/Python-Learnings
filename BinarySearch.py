# Binary Search

# Suitable for sorted elements only

l = [x for x in range(1, 32)]
n = int(input())
min = 0
max = len(l) - 1 

while min <= max:
	avg = (min + max) // 2
	if l[avg] == n:
		print('The value is present at the index', avg)
		break
	elif l[avg] < n:
		min = avg + 1
	else:
		max = avg - 1
else:
	print('The given value not present in the list')

