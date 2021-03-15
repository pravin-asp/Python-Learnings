word = 'Python'#input()
print(word)
count = len(word)
for i in range(count - 1, -1, -1):
	print(word[i], end = '')
print