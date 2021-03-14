#Iterative Statements

#re-iterate

#for	- 	in python
#while 	- 	in python 
#do..while 	- not in python 

# While loop
mind = 43
guess = 0

while guess != mind:
	guess = int(input('Tell me your guess : '))
	if guess == mind:
		print('Wow, Super')
	elif guess > mind:
		print('No, your guess is greater')
	else:
		print('No, too little')
