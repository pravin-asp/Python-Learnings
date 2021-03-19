# input --> wish you a very happy new year
# output --> wish a happy year

s = 'wish you a very happy new year'.split()
print(s)
print()
for i in range(0, len(s), 2):
	print(s[i], end = ' ')
	
print()
print()
for i in range(0, len(s), 2):
	print(s[i][::-1], end = ' ')
	if i + 1 < len(s):
		print(s[i+1], end = ' ')