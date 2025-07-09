Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> open('c:\\users\\prasarav')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    open('c:\\users\\prasarav')
PermissionError: [Errno 13] Permission denied: 'c:\\users\\prasarav'

>>> open('c:\\users\\prasarav\\desktop\\p.py')
<_io.TextIOWrapper name='c:\\users\\prasarav\\desktop\\p.py' mode='r' encoding='cp1252'>
>>> hello = open('c:\\users\\prasarav\\desktop\\write.txt', '2')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    hello = open('c:\\users\\prasarav\\desktop\\write.txt', '2')
ValueError: invalid mode: '2'
>>> hello = open('c:\\users\\prasarav\\desktop\\write.txt', 'w')
>>> hello.write("Hello")
5
>>> hello.write('adfkdsa ksdfj sdifdsfk dsfd sjfklds klsdafk dsafk')
49
>>> hello.closer()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    hello.closer()
AttributeError: '_io.TextIOWrapper' object has no attribute 'closer'. Did you mean: 'close'?
>>> hello.close()
>>> import shelve
>>> shelfile = shelve.open('c:\\users\\prasarav\\desktop\\shelvedata')
>>> shelfile['cats'] = ['zophie', 'pooka', 'simon', 'fat-tall', 'cleo']
>>> shelfile.close()
>>> 
>>> shelfile = shelve.open('c:\\users\\prasarav\\desktop\\shelvedata')
>>> shelfile['cats']
['zophie', 'pooka', 'simon', 'fat-tall', 'cleo']
>>> shelfile.close()
>>> 
>>> 
>>> import shutil
>>> shutil.copy('c:\\users\\prasarav\\desktop\\shelvedata', 'c:\\users\\prasarav\\desktop\\python learning')
'c:\\users\\prasarav\\desktop\\python learning\\shelvedata'
