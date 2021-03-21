# sort() --> arranges the values in the list in ascending order
# sort function accepts only the homogeneous functions

list = [10, 40, 20, 4]
print(list)
list.sort()
print(list)

l = ['kathir', 'mathi', 'nirai', 'anbu']
print(l)
l.sort()
print(l)

# Descending order
l = ['kathir', 'mathi', 'nirai', 'anbu']
print(l)
l.sort(reverse = True)
print(l)


# List Aliasing
# Assigning one list to another list 

l1 = [10, 20, 30, 40, 50]
l2 = l1

# l1 and l2 will point to the same memory 
# if we change one value in the l1 then the value in l2 will also be reflected

# List Cloning

# --> copy()

# l2 = l1.copy()
# l2 = l1[:]

a = ['kathir', 'mathi', 'nirai', 'anbu']
b = ['kathir', 'mathi', 'nirai', 'anbu']
print(a == b)
print(a is b)
print(a > b)

# clear() --> erases the values in the list a 
a.clear()
print(a)