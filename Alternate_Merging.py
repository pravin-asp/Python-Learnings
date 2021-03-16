# input --> abc
#			def 
# output --> adbecf

# Merging Characters

a = input()
b = input()
length = len(a) if len(a) < len(b) else len(b)
if len(a) < len(b):
	ans = b 
else:
	ans = a 
i = 0
while i < length:
	print(a[i] + b[i], end = '')
	i += 1
print(ans[length:])


print()
output = ''
i, j = 0, 0
while i < len(a) or j < len(a):
	if i < len(a):
		output += a[i]
	if j < len(b):
		output += b[i]
	i += 1
	j += 1
print(output)