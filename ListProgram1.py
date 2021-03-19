list = [10, 20, 30, 40, 50, 60, 50, 30]
print(list.count(10)) # count the number of element present
print(list.count(50))

print(list.index(30)) # displays the index of the element
#print(list.index(300)) # ValueError : not in the list

# Manipulation of List - Function

# append() --> adding the element in the list 
			# adds element in the last
			
list.append(500)
print(list)


n = []
for x in range(1, 11):
	n.append(x)
print(n)

n = []
for x in range(1, 11):
	if x % 2 == 0:
		n.append(x)
print(n)