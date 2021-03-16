# Input : A5
# Output : AAAAA

a = input()
output = ''
for i in range(0, len(a), 2):
	output += a[i] * int(a[i + 1])
print(output)