# Input : A5B6C7
# Output : ABC567

# Separate the strings

a = input()
alpha = ''
num = ''
for i in a:
	if i >= 'A' and i <= 'Z':
		alpha += i 
	if i >= '0' and i <= '9':
		num += i 
alpha += num
print(alpha)