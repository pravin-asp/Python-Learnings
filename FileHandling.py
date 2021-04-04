# File Handling

# text, file, pdf file 
# image, audio, video ---> Binary files

# r -> read
# w -> write
# a -> append(read, write)
# r+ -> read and write data
# w+ -> write and read data
# a+ -> appending
# x -> whether the file is present or not

file = open('C:\\Users\\Admin\\Desktop\\Links.txt', 'w')
print(file.name)
print(file.mode)
print('Readability',file.readable())
print('Writability',file.writable())
print('File opened or closed',file.closed)
file.close()
print('File opened or closed', file.closed)

file = open('C:\\Users\\Admin\\Desktop\\Links.txt', 'w')
ll = ['python ', 'c ', 'c++ ', 'java ', 'ruby ']
file.writelines(ll)
file.write('Learning\n')
file.write('My Learning')
file.close()

file = open('C:\\Users\\Admin\\Desktop\\New Text Document.txt', 'r')
content = file.readlines()#file.readline()#file.read(100)# file.read()
print(content)
print(type(content))
file.close()