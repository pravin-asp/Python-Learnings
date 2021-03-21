# List Comprehension

l = [i ** i for i in range(1, 6)]
print(l)

ll = [val for val in l if val % 2 == 0]
print(ll)

n1 = [100, 200, 300, 400]
n2 = [300, 400, 500, 600]

n3 = [val for val in n1 if val in n2]
print(n3)