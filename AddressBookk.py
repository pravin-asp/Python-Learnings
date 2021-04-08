import sqlite3
class AddressBook:
	def __init__(self):
		self.contactName = ''
		self.emailId = ''
		self.address = ''
	
	def giveContactDetails(self):
		self.contactName = input('Enter Person Name:')
		self.emailId = input('Enter Email ID:')
		self.address = input('Enter your Address:')
		return self.contactName, self.emailId, self.address
		
	def display(self):
		print('Name : {}\nEmail : {}\nAddress : {}'.format(self.contactName, self.emailId, self.address))
		#print()
		
#contactList = []
choice = 'y'
'''connection = sqlite3.connect('C:\\Users\\Admin\\Desktop\\Langscape Python\\AddressBookDB.db')
cursor = connection.cursor()
sql_command = """
				CREATE TABLE Address_Book(
				ID INTEGER PRIMARY KEY,
				Name VARCHAR(20),
				Email_Id VARCHAR(30),
				Address VARCHAR(30));
		      """
cursor.execute(sql_command)
connection.commit()'''
print('Database created successfully with rows')
while choice == 'y':
	print('1. Add New Contact\n2. Display Contacts')
	response = int(input('Enter your Choice:'))
	
	if response == 1:
		contact = AddressBook()
		(name, emailID, address) = contact.giveContactDetails()
		#contactList.append(contact)
		with sqlite3.connect('C:\\Users\\Admin\\Desktop\\Langscape Python\\AddressBookDB.db') as connection:
			cursor = connection.cursor()
			cursor.execute("INSERT INTO Address_Book(ID, Name, Email_Id, Address) VALUES(Null, ?, ?, ?)", (name, emailID, address))
			connection.commit()
			print('Inserted into database successfully!')
	elif response == 2:
		#for x in contactList:
			#x.display()
		connection = sqlite3.connect('C:\\Users\\Admin\\Desktop\\Langscape Python\\AddressBookDB.db')
		cursor = connection.cursor()
		cursor.execute('SELECT * from Address_Book')
		result = cursor.fetchall()
		for i in result:
			print(i)
		connection.commit()
	else:
		print('Please check your response')
		
	choice = input('Press \'y\' to continue:')
#print(contactList)
			