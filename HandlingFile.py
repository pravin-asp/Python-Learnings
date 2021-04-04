with open('c:/users/admin/desktop/links.txt', 'w') as file:
	file.write('Python is duck typing\n')
	file.write('Python')
	file.close()
	
import os, sys
fileName = input('Enter file name:')
if os.path.isfile(fileName):
	f = open(fileName, 'r')
	print('File is Present')
	lines, words, letters = 0, 0, 0
	for line in f.readlines():
		lines += 1
		word = line.split()
		words += len(word)
		letters += len(line)
		
	print(lines, words, letters)
	f.close()
else:
	print('File is not present')
	
	
# Binary data
inputfile = open('C:\\Users\\Admin\\Desktop\\Main Project\\171CS227.jpg', 'rb')
output = open('C:\\Users\\Admin\\Desktop\\Main Project\\Images\\image.jpg', 'wb')
byte = inputfile.read()
output.write(byte)


# CSV --> Comma Separated Values --> simply excel files

import csv
with open('student.csv', 'w', newline = '') as file:
	reynolds = csv.writer(file) # write object
	reynolds.writerow(['SID', 'SNAME', 'STUADDRESS'])
	count = int(input('Enter no.of Students:'))
	for i in range(count):
		sid = input('Enter Student ID:')
		sname = input('Enter student name:')
		saddress = input('Enter student address:')
		reynolds.writerow([sid, sname, saddress])
with open('student.csv', 'r', newline = '') as file:
	r = csv.reader(file)
	output = list(r)
	for line in output:
		for eachWord in line:
			print(eachWord, end = ' ')
		print()
		
os.mkdir('P') # mkdir - Create folder
os.makedirs('Pyt/python/learning') # makedirs - create folder inside folder

# rmdir - remove a single folder
# removedirs - removes folders
os.mkdir('Python')
os.rmdir('Python')
