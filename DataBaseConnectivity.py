'''
Python --> DB SQL

import sqlite3 # comes default for sqlite data base 

import cx_Oracle # have to install cx_Oracle module for using Oracle Data Base 

con = cx_Oracle.connect(credentials) # connects with the database
					if exits

	# connect function returns the connection object

CRUD Operations:
Create, update, delete, insert

cursor = con.cursor() 

cursor.execute

commit --> confirm the action.

Steps:
1. Import statement
2. Establishing connection between python and database connect() --> connection object
3. Creating cursor object --> cursor()
4. Executing SQL Query --> execute() executemany()
5. commit()
'''

import sqlite3 # module
connection = sqlite3.connect('C:\\Users\\Admin\\Desktop\\Langscape Python\\TestDB.db')
cursor = connection.cursor()
# Creating and adding a row in data base
'''sql_command = """
				CREATE TABLE Student(
				RollNo INTEGER PRIMARY KEY,
				Sname VARCHAR(20),
				Grade CHAR(1),
				Gender CHAR(1),
				Average DECIMAL(5, 2),
				DOB DATE);
			  """
			  
cursor.execute(sql_command)
try:
	sql_command = """
					INSERT INTO students(
					RollNo, Sname, Grade, Gender, Average, DOB)
					VALUES(null, "Python", 'B', 'F', "87.8", "1999-08-21");
				  """
	cursor.execute(sql_command)
	connection.commit()
	print('Student Table Created')
except:
	connection.rollback()
	print('Seems the DB is wrong')'''
	
	
# Adding Multiple datas to the data base
'''	
student_data = [('Thiru', 'C', 'M', '75.2', '1999-05-17'),
				('Raja', 'A', 'M', '75.2', '1999-04-17'),
				('Bala', 'B', 'F', '75.2', '1999-03-17'),
				('Kannan', 'A', 'M', '75.2', '1999-05-17')
				]
for p in student_data:
	format_str = """ INSERT INTO Student(Rollno, Sname, Grade, Gender, Average, DOB)
					VALUES(Null, "{name}", "{Grd}", "{Gend}", "{Avg}", "{dob}");"""
	sql_command = format_str.format(name = p[0], Grd = p[1], Gend = p[2], Avg = p[3], dob = p[4])
	cursor.execute(sql_command)
connection.commit()
connection.close()
print("Records Added")'''

# DML - Data Manipulation Language
# DDL - Data Definition Language

# fetching the data from the data base
#fetchall()
cursor.execute("SELECT * FROM Student") # * - every column value gets printed
ans = cursor.fetchall()
for i in ans:
	print(i)
print()

#fetchone()
cursor.execute("SELECT * FROM Student") # * - every column value gets printed
ans = cursor.fetchone()
for i in ans:
	print(i)
print()

#fetchone()
cursor.execute("SELECT * FROM Student") # * - every column value gets printed
ans = cursor.fetchone()
while ans is not None:
	print(ans)
	ans = cursor.fetchone()
print()

#fetchmany(record count)
cursor.execute("SELECT * FROM Student") # * - every column value gets printed
ans = cursor.fetchmany(3)
for i in ans:
	print(i)
print()
	
# distinct + fetchall
cursor.execute("SELECT DISTINCT(grade) from Student")
ans = cursor.fetchall()
for i in ans:
	print(i)
print()

# Count
cursor.execute("SELECT COUNT(*) from Student")
ans = cursor.fetchall()
print(ans)
print()

# WHERE
cursor.execute("SELECT Rollno, Sname from Student WHERE Grade <> 'A' and Grade <> 'C'")
res = cursor.fetchall()
print(*res, sep = '\n')
print()

# DELETE
cursor.execute("DELETE from Student where Rollno = '2'")
connection.commit()
print('Total no of rows deleted:', connection.total_changes)
connection.close()

# update --> for updating the wrong values in the db