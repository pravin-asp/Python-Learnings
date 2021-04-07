# Generator Function

# Generates sequence of values

def test():
	yield 'a'
	yield 'b'
	yield 'c'
	yield 'd'
	
result = test()
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(type(result))
print()

def firstNnumbers(num):
	n = 1
	while n <= num:
		yield n 
		n += 1

values = firstNnumbers(10)
for i in values:
	print(i)
print(values)
print(type(values))
print()

import random
import time
names = ['Ganesh', 'Thas', 'Aravind', 'Vidya']
colors = ['red', 'blue', 'green', 'yellow']

def people_list(num_people):
	result = []
	for i in range(num_people):
		student = {'id' : i, 'name' : random.choice(names), 'team' : random.choice(colors)}
	result.append(student)
	return result
	
def student_generator(count):
	for i in range(count):
		student = {'id' : i, 'name' : random.choice(names), 'team' : random.choice(colors)}
		yield student
	
timer1 = time.perf_counter()
#p = people_list(10000000)
p = student_generator(10000000000000000000000000)
timer2 = time.perf_counter()

print('Time taken is {} - {} = {}'.format(timer2, timer1, timer2 - timer1))