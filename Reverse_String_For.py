word = 'Python'#input()
print(word)
count = len(word)
for i in range(count - 1, -1, -1):
	print(word[i], end = '')
print()


# Slicing

# Step Operator
print()
word = 'amma'
word1 = word[::-1]
if word == word1:
	print('Palindrome')
else:
	print('Not Palindrome')