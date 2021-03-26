'''
User have to give 4 inputs to find the 4 numers that the computer had kept in the memory 
'''

from random import choice
answer = []
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(4):
	a = choice(l)
	answer.append(a)
	l.remove(a)
guess = ['X', 'X', 'X', 'X']
correct = ['C', 'C', 'C', 'C']

while guess != correct:
	a, b, c, d = map(int, input('Enter four values:\n').split())
	if a in answer:
		if answer.index(a) == 0:
			guess[0] = 'C'
		else:
			guess[0] = 'P'
	else:
		guess[0] = 'X'
	if b in answer:
		if answer.index(b) == 1:
			guess[1] = 'C'
		else:
			guess[1] = 'P'
	else:
		guess[1] = 'X'
	if c in answer:
		if answer.index(c) == 2:
			guess[2] = 'C'
		else:
			guess[2] = 'P'
	else:
		guess[2] = 'X'
	if d in answer:
		if answer.index(d) == 3:
			guess[3] = 'C'
		else:
			guess[3] = 'P'
	else:
		guess[3] = 'X'
	print(*guess)
	print()
else:	
	print('Hurrey! You have found the number I have kept in my mind')