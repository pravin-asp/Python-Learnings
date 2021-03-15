s = 'python is easy'

print(s.upper()) # upper case
print(s.lower()) # lower case
print(s.swapcase()) # upper to lower and vice versa
print(s.title()) # capitalize 1st letter in each word
print(s.capitalize()) # capitalize 1st letter of the 1st word of the sentence

print(s[0].upper() + s[1:])
print(s[:-1] + s[-1].upper())

# numbers --> Iterations
# Iterations --> looping
# looping --> while, for
# condition
# length

mailid = input('Enter your mail id:')
i = 0
while i < len(mailid):
	if mailid[i] >= '0' and mailid[i] <= '9':
		print(mailid[i], end = '')
	i += 1
print()
for x in mailid:
	if x >= '0' and x <= '9':
		print(x, end = '')
		
print()
print()

for x in mailid:
	if not (x >= '0' and x <= '9') and not (x >= 'a' and x <= 'z'):
		print(x, end = '')

