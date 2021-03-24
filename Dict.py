# Count of each letter in a sentence

name = input('Enter your name:')
dict = {}
for i in name:
	dict[i] = dict.get(i, 0) + 1

for key, value in dict.items():
	print(key,'occurs', value)

print()
for key, value in dict.items():
	if value == 1:
		print(key,'occurs', value)

print()
for key, value in dict.items():
	if value > 1:
		print(key,'occurs', value)

print()
for key, value in dict.items():
	if value == max(dict.values()):
		print(key,'occurs', value, 'times which is the highest')