Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import re
regex = re.compile(r'(\d\d)-(\d\d\d\d\d\d\d\d\d\d)')
text = "My name is pravin. my phone numbers are 8610373818, 9443320203"
mo = regex.search(text)
mo.group()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    mo.group()
AttributeError: 'NoneType' object has no attribute 'group'
mo
print(mo)
None
text = "My name is pravin. my phone numbers are 91-8610373818, 91-9443320203"
mo = regex.search(text)
mo
<re.Match object; span=(40, 53), match='91-8610373818'>
print(mo)
<re.Match object; span=(40, 53), match='91-8610373818'>
mo.group()
'91-8610373818'
mo = regex.findall(text)
mo
[('91', '8610373818'), ('91', '9443320203')]
mo.group()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    mo.group()
AttributeError: 'list' object has no attribute 'group'
mo.group(1)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    mo.group(1)
AttributeError: 'list' object has no attribute 'group'
mo
[('91', '8610373818'), ('91', '9443320203')]
mo[1].group()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    mo[1].group()
AttributeError: 'tuple' object has no attribute 'group'
regex = re.compile(r'Bat(man|bag|cat|ball)')
test = "batman Batball, Batbag, Batcat"
mo = regex.search(test)
mo
<re.Match object; span=(7, 14), match='Batball'>
mo.group()
'Batball'
mo = regex.findall(test)
mo
['ball', 'bag', 'cat']
import re
batregex = re.compile(r'Bat(wo)man')
batregex = re.compile(r'Bat(wo)?man')
test = "batman batwoman"
mo = batregex.findall(test)
mo
[]
test = "Batman Batwoman"
mo = batregex.findall(test)
mo
['', 'wo']
mo.group()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    mo.group()
AttributeError: 'list' object has no attribute 'group'
mo = batregex.fullmatch(test)
mo
print(mo)
None
mo = batregex.search(test)
mo
<re.Match object; span=(0, 6), match='Batman'>
mo.group()
'Batman'
test = "batman Batwoman"
mo = batregex.search(test)
mo
<re.Match object; span=(7, 15), match='Batwoman'>
mo.group()
'Batwoman'
test = 'Batwowowowoman'
text = 'Batman'
reg1 = re.compile(r'Bat(wo)?man')
reg2 = re.compile(r'Bat(wo)*man')
reg3 = re.compile(r'Bat(wo)+man')
print(reg1.search(test))
None
print(reg2.search(test))
<re.Match object; span=(0, 14), match='Batwowowowoman'>
print(reg2.search(test).group())
Batwowowowoman
print(reg3.search(test).group())
Batwowowowoman
print(reg1.search(text).group())
Batman
print(reg2.search(text).group())
Batman
print(reg3.search(test).group())
Batwowowowoman
print(reg3.search(text).group())
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    print(reg3.search(text).group())
AttributeError: 'NoneType' object has no attribute 'group'
string = "my name is * comming from + where are you from ?"
r = re.compile(r'\*\+\?')
r.search(string)


a = r.search(string)
a
a.group()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.group()
AttributeError: 'NoneType' object has no attribute 'group'
print(a)
None
string = "my name is *+? comming from + where are you from ?"
r.search(string)
<re.Match object; span=(11, 14), match='*+?'>
phone = "my phone number is +91-8610373818"
pr = re.compile(r'(\+91-)?(\d){10}')
pr.search(phone).group()
'+91-8610373818'
email = "pravin-saravanabhavan@gmail.com"
reg = re.compile(r'[a-zA-Z0-9\.\-\_]\@\w\.\w{2,5}')
reg.findall(email)
[]
reg = re.compile(r'\w@\w.\w')
reg.findall(email)
['n@gma']
reg = re.compile(r'\w@\w\.\w')
reg.findall(email)
[]
reg = re.compile(r'\w+@\w+.(\w){2,3}')
reg.findall(email)
['m']
email = 'my email id is pravin@gmail.com'
reg.findall(email)
['m']
reg = re.compile(r'\w+\s\w+')
reg.findall(email)
['my email', 'id is']
reg = re.compile(r'[a-zA-Z0-9]+\@[a-zA-Z]+.[a-zA-z]{2,3}')
reg.findall(email)
['pravin@gmail.com']
reg = re.compile(r'[a-zA-Z0-9]+\@[a-zA-Z]+\.[a-zA-z]{2,3}')
reg.findall(email)
['pravin@gmail.com']
email = 'pravin@gmail.com, pravin-pravin@tcs.com, pravin.pravin@bostonharborconsulting.com'
reg.findall(email)
['pravin@gmail.com', 'pravin@tcs.com', 'pravin@bostonharborconsulting.com']
reg = re.compile(r'[a-zA-Z0-9\.\-\_]+\@[a-zA-Z]+\.[a-zA-z]{2,3}')
reg.findall(email)
['pravin@gmail.com', 'pravin-pravin@tcs.com', 'pravin.pravin@bostonharborconsulting.com']
reg = re.compile(r'[a-zA-Z0-9\.\-\_]\@[a-zA-Z]\.[a-zA-z]{2,3}')
reg.findall(email)
[]
reg = re.compile(r'[a-zA-Z0-9\.\-\_]*\@[a-zA-Z]*\.[a-zA-z]{2,3}')
reg.findall(email)
['pravin@gmail.com', 'pravin-pravin@tcs.com', 'pravin.pravin@bostonharborconsulting.com']
reg.search(email).group()
'pravin@gmail.com'
reg = re.compile(r'.in')
reg.findall(email)
['vin', 'vin', 'vin', 'vin', 'vin', 'tin']
KeyboardInterrupt
>>> reg = re.compile(r'.+in')
>>> reg.findall(email)
['pravin@gmail.com, pravin-pravin@tcs.com, pravin.pravin@bostonharborconsultin']
>>> reg = re.compile(r'.{1,6}in')
>>> reg.findall(email)
['pravin', ', pravin', '-pravin', ', pravin', '.pravin', 'onsultin']
>>> txt = '<pravin i am from > tiruchengode >'
>>> reg = re.compile(r'<(.*)>')
>>> reg.findall(txt)
['pravin i am from > tiruchengode ']
>>> reg = re.compile(r'<(.*?)>')
>>> reg.findall(txt)
['pravin i am from ']
>>> reg = re.compile(r'<(.*)?>')
>>> reg.findall(txt)
['pravin i am from > tiruchengode ']
>>> reg = re.compile(r'Agent \w+')
>>> txt = 'Agent Carter sent a secrete message to Agent Bow'
>>> reg.sub("MRX", txt)
'MRX sent a secrete message to MRX'
>>> reg = re.compile(r'Agent (\w)\w*')
>>> reg.sub("Agent \1***", txt)
'Agent \x01*** sent a secrete message to Agent \x01***'
>>> 
>>> reg.sub(r"Agent \1***", txt)
'Agent C*** sent a secrete message to Agent B***'
>>> tst = 'you need to go to the url https://www.github.com and loing with the link http://linkedin.com'
>>> url = re.compile(r'((http)|(https))?:\/\/(www\.)?[a-zA-Z0-9]+\.[a-zA-Z]{2,3}')
>>> url = re.compile(r'(((http)|(https))?:\/\/(www\.)?[a-zA-Z0-9]+\.[a-zA-Z]{2,3})')
>>> url.findall(tst)
[('https://www.github.com', 'https', '', 'https', 'www.'), ('http://linkedin.com', 'http', 'http', '', '')]
>>> for i in url.findall(tst):
...     print(i[0])
... 
...     
https://www.github.com
http://linkedin.com
