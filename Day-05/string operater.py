Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
names='iswarya lalitha chaitu'
names[:7]
'iswarya'
names[8:15]
'lalitha'
names[16:22]
'chaitu'
lalitha in names
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    lalitha in names
NameError: name 'lalitha' is not defined
names='iswarya lalitha chaitu'
'iswarya' in names
True
'priya' not in names
True
"chaitu" in names
True
names='iswarya chaitu lalitha'
names[-1:-6]
''
len(names)
22
ord('i')
105
ord(12)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    ord(12)
TypeError: ord() expected string of length 1, but int found
chr(13)
'\r'
ord('c')
99
ord('s')
115
chr(45)
'-'
chr(15)
'\x0f'
chr(11)
'\x0b'
ord('t')
116
s='pyton programming language'
s.upper()
'PYTON PROGRAMMING LANGUAGE'
s,lower()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s,lower()
NameError: name 'lower' is not defined
s.lower()
'pyton programming language'
s,title()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s,title()
NameError: name 'title' is not defined. Did you mean: 'tuple'?
>>> s.title()
'Pyton Programming Language'
>>> s.swapcase()
'PYTON PROGRAMMING LANGUAGE'
>>> s.capitalize()
'Pyton programming language'
>>> s.center(20,'*')
'pyton programming language'
>>> s.center(50,'-')
'------------pyton programming language------------'
>>> s.rjust(40,'*')
'**************pyton programming language'
>>> s.ljust(50,'*')
'pyton programming language************************'
>>> '123'.zfill(4)
'0123'
>>> '234'.zfill(7)
'0000234'
>>> '34'.zfill(1)
'34'
>>> s
'pyton programming language'
>>> s.find('m')
12
>>> s.rfind('e')
25
>>> s.lfind('i')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s.lfind('i')
AttributeError: 'str' object has no attribute 'lfind'. Did you mean: 'find'?
>>> s.rfind('i')
14
>>> s.index('l')
18
>>> s.rindex('p')
6
>>> s.count('m')
2
>>> s.replace('m','i')
'pyton prograiiing language'
>>> s.maketrans('aeiou','@#$%*')
{97: 64, 101: 35, 105: 36, 111: 37, 117: 42}
