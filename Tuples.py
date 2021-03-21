# Tuples

# List is mutable --> True 
# Tuple is immutable

# Insertion order is maintained
# Duplicate values are allowed

# List --> []
# Tuples --> ()

t = (10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10) # tuples
a = (10) # not tuple python will consider it as integer because for some arithmetic operations we will use (10 * 2) + 30 this will not consider as tuple 
print(type(t))
print(type(a))
a = (10, ) # now it is tuple
print(type(a))

print(t[0])
print(t[-1])
print(t[2:])
print(t[::2])

#t[1] = 123 --> shows type error 

t1 = (10, 20, 30)
t2 = (5, 10, 15)
t3 = t1 + t2 
print(t3)

t4 = t1 * 2
print(t4)

print(t4.count(10))
print(len(t4))

print(t3.index(10))

t5 = sorted(t3)
print(t5)

t5 = sorted(t3, reverse = True)
print(t5)

print(min(t5))
print(max(t5))
print(sum(t5))

# Tupel Packing and Unpacking

# Packing
a, b, c, d = 10, 20, 30, 40
t = a, b, c, d 
print(t)

# Unpacking 
p, q, r, s = t 
print(p, q, r, s)


# Tuple Comprehension --> we will get generator

t = (val for val in range(20))
print(type(t)) 
print(t)
for val in t:
	print(val)
	
t = eval(input())
print(t)