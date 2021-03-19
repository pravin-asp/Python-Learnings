#remove()
#pop()

l = [10, 20, 30, 40, 50, 60]
print(l)
l.remove(20)
print(l)

l.pop() # removes the last element in the list

print(l)

l.pop(2) # removes the element present in the index 

print(l)

# reverse() --> reverse the element in the list

l = ['a', 'b', 'c', 'd', 'e']
l.reverse() 
print(l)

l = ['a', 'b', 'c', 'd', 'e']
l1 = []
i = len(l) - 1
while i >= 0:
	l1.append(l[i])
	i -= 1
print(l1)


user = input()
l = []
l.extend(user)
l1 = []
i = len(l) - 1
while i >= 0:
	l1.append(l[i])
	i -= 1
print(l1)