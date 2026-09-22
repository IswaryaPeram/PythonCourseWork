Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
int(a)
10
float(a)
10.0
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
complex(a)
(10+0j)
b=12.6
int(a)
10
float(b)
12.6
str(b)
'12.6'
list(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
complex(b)
(12.6+0j)
s="Iswarya"
s
'Iswarya'
int(s)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'Iswarya'
s="123456"
int(s)
123456
float(s)
123456.0
complex(s)
(123456+0j)
list(s)
['1', '2', '3', '4', '5', '6']
tuple(s)
('1', '2', '3', '4', '5', '6')
set(s)
{'2', '1', '3', '5', '4', '6'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True
c=[1,2,3,4]
int(c)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
bool(c)
True
>>> tuple(c)
(1, 2, 3, 4)
>>> set(c)
{1, 2, 3, 4}
>>> s=(3,4,5,6)
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
>>> list(s)
[3, 4, 5, 6]
>>> set(s)
{3, 4, 5, 6}
>>> bool(s)
True
>>> complex(s)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'tuple'
>>> a={23,45,67,}
>>> list(a)
[67, 45, 23]
>>> tuple(a)
(67, 45, 23)
>>> complex9a)
SyntaxError: unmatched ')'
>>> complex(a)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    complex(a)
TypeError: complex() first argument must be a string or a number, not 'set'
>>> bool(a)
True
>>> i={2:3,4:5,6:5}
>>> list(i)
[2, 4, 6]
>>> set(i)
{2, 4, 6}
>>> tuple(i)
(2, 4, 6)
>>> bool(i)
True
>>> str(i)
'{2: 3, 4: 5, 6: 5}'
