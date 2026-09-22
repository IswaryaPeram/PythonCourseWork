Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Datatypes
>>> #int float complex
>>> a=12
>>> type(a)
<class 'int'>
>>> b=10.0
>>> type(b)
<class 'float'>
>>> c=23+3j
>>> type(c)
<class 'complex'>
>>> #str list tuple
>>> a="codegnan"
>>> a
'codegnan'
>>> 'codegnan'#
'codegnan'
>>> a=[12, "iswarya" , 23.4}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a=[12, "iswarya" ,23.4]
>>> a
[12, 'iswarya', 23.4]
>>> a.append(32)
>>> a
[12, 'iswarya', 23.4, 32]
>>> id(a)
2679741311296
>>> a.append(23)
>>> id(a)
2679741311296
>>> #tuple
>>> b=(12,34,56,"iswarya",34.5)
>>> b
(12, 34, 56, 'iswarya', 34.5)
>>> id(b)
2679741277552
>>> #maping set dict
>>> c={23,45,6,"ishu",34.5}
>>> c
{34.5, 6, 23, 'ishu', 45}
>>> c.append(12)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    c.append(12)
AttributeError: 'set' object has no attribute 'append'
id(c)
2679741498976
d={"name":"ishu","class":12}
d
{'name': 'ishu', 'class': 12}
s={23,45,6,9}
s.forzen
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s.forzen
AttributeError: 'set' object has no attribute 'forzen'
a=10
b=10
a==b
True
#nontype
a=[]
b=()
c={}
d={}
a
[]
b=
SyntaxError: invalid syntax
d
{}
