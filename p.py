import sys
print('Inside the file p.py')
input = open('c://users//prasarav//desktop//input.txt', 'r')
output = open('c://users//prasarav//desktop//output.txt', 'w+')
output.write(input.read())
input.close()
output.close()
print('Outside the file p.py')
print(sys.argv)
