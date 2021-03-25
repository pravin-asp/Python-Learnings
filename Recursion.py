# Recursion

# looping --> block of statements repeated
#		iteration

# Recursion --> function itself repeated
#		A function calling itself 

# Function --> named set of instructions

# For example : Login information

def getUserNamePassword(username, password):
	if username != 'abcd':
		print('Incorrect Username')
		username = input('Enter your username:')
		password = input('Enter your password:')
		getUserNamePassword(username, password)
	elif password != 'abcd':
		print('Incorrect password')
		username = input('Enter your username:')
		password = input('Enter your password:')
		getUserNamePassword(username, password)
	

username = input('Enter your usernam:')
password = input('Enter your password:')
getUserNamePassword(username, password)