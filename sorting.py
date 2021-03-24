l = [10, 5, 8, 3]

# 3 5 8 10
# 10 8 5 3

print('Before Sorting ', l)
i = 0
while i < len(l) - 1:
	if l[i] > l[i + 1]:
		l[i], l[i + 1] = l[i + 1], l[i]
	i += 1

print('After First Sorting ', l)
i = 0
while i < len(l) - 2:
	if l[i] > l[i + 1]:
		l[i], l[i + 1] = l[i + 1], l[i]
	i += 1
print('After Second Sorting ', l)
i = 0
while i < len(l) - 3:
	if l[i] > l[i + 1]:
		l[i], l[i + 1] = l[i + 1], l[i]
	i += 1
print('After Third Sorting ', l)

# Bubble Sorting 
# While loop

l = [100, 300, 2, 90, 4, 200, 999, 1, 20]
print('Before Sorting ', l)
i = 1
while i < len(l):
	j = 0
	while j < len(l) - i:
		if l[j] > l[j + 1]:
			l[j], l[j + 1] = l[j + 1], l[j]
		j += 1
	i += 1
print('After Sorting ', l)

# For loop
l = [100, 300, 2, 90, 4, 200, 999, 1, 20]
print('Before Sorting ', l)
for i in range(1, len(l)):
	for j in range(len(l) - i):
		if l[j] > l[j + 1]:
			l[j], l[j + 1] = l[j + 1], l[j]
print('After Sorting ', l)