# Find multiples of twenty
# IRC - Internet Relay Chat
# Kaniyam Foundation
# FSFT - Free Software Foundation Tamil Nadu

l = list(range(10, 101, 10))
l2 = ['a', 'b', 'c']
l3 = l + l2 # Concatination is allowed in list
for i in l:
	if i % 20 == 0:
		print(i)
		
print(l3)

print()
print(l3 * 2)
print(type(l3))

# List is a datatype - True
# List can contaion heterogeneous objects - True
# List can contain any datatype - True
# List can contaion another list - True


l4 = [l, l2]
print(l4)
print(l4[0])
print(l4[1])
print()
print(l4[0][1])
print(l4[1][0])

outerlist = [l, l2]
for innerlist in outerlist:
	for element in innerlist:
		print(element, end = ' ')
	print()