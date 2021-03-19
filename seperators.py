list = ['a', 'b', 'c', 'd', 'e']
output = ':'.join(list)
print(output)

# input --> Sun Mon Tues Wednes Thrus Fri Satur
# output --> Sunday Monday Tuesday Wednesday Thrusday Friday Saturday

input = 'Sun Mon Tues Wednes Thrus Fri Satur'
words = input.split()
words2 = []
for word in words:
	words2.append(word + 'day')
print(words2)

output = ' '.join(words2)
print(output)