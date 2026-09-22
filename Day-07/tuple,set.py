Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=()
s=(1,2,3,4,)
s
(1, 2, 3, 4)
s=(1)
s
1
s=(1,)
s=(2,34.5,Python,(1,2,3),True)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s=(2,34.5,Python,(1,2,3),True)
NameError: name 'Python' is not defined
s=(2,3,44.5,'python',(3,4,5),True)
s
(2, 3, 44.5, 'python', (3, 4, 5), True)
type(s)
<class 'tuple'>
a=(2,3,4)
b=(4,5,6)
a+b
(2, 3, 4, 4, 5, 6)
a*4
(2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4)
w=(2,34.6,'python',(4,5,6),{3,9,0],False)
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
w=(3,45.6,'python',(3,4,5),{2,3,6},False)
w
(3, 45.6, 'python', (3, 4, 5), {2, 3, 6}, False)
>>> w[4]
{2, 3, 6}
>>> w[-1]
False
>>> w[2:4]
('python', (3, 4, 5))
>>> w[:-1]
(3, 45.6, 'python', (3, 4, 5), {2, 3, 6})
>>> w[:-2]
(3, 45.6, 'python', (3, 4, 5))
>>> 'python' in w
True
>>> i=(23,45,6,90,6,1,3,56,98,90,23,56)
>>> i
(23, 45, 6, 90, 6, 1, 3, 56, 98, 90, 23, 56)
>>> sorted(t)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    sorted(t)
NameError: name 't' is not defined
>>> sorted(i)
[1, 3, 6, 6, 23, 23, 45, 56, 56, 90, 90, 98]
>>> max(i)
98
>>> min(i)
1
>>> len(i)
12
>>> i.index(45)
1
>>> i.count(90)
2
>>> all(1,3,4)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    all(1,3,4)
TypeError: all() takes exactly one argument (3 given)
>>> all((1,2,3))
True
>>> all((3,2,1))
True
>>> any((2,5,6,00,1))
True
>>> sum(i)
497
>>> s=set{}
SyntaxError: invalid syntax
s=set()
type(s)
<class 'set'>
s={1,3,4,,0,9,99,77,55}
SyntaxError: invalid syntax
s={2,34,4,5,123,45,5}
s
{2, 34, 4, 5, 123, 45}
s={2,3,3,4,1,5}
s
{1, 2, 3, 4, 5}
s={1,45,56,(78,34),95}
s
{1, 56, (78, 34), 45, 95}
s={1,2,3,'python'}
s
{1, 2, 3, 'python'}
s={12345,555556,097}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
s={1234,456,9087}
s2={456,986,789}
s+s2
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    s+s2
TypeError: unsupported operand type(s) for +: 'set' and 'set'
1234 in s
True
900 not in s
True
s | s2
{1234, 789, 456, 986, 9087}
s & s2
{456}
s - s2
{1234, 9087}
s2 - s
{986, 789}
a={2,3,4,5,6}
a
{2, 3, 4, 5, 6}
#{2}{2,3,4}{3}{5}{6}
{2}>=a
False
{2}<=a
True
s={1,9,7}
p={2,3,4}
s.isdisjoint(p)
True
a={12,3,4,5,78,90,45}
a
{3, 4, 5, 90, 12, 45, 78}
sorted(a)
[3, 4, 5, 12, 45, 78, 90]
max(a)
90
min(a)
3
len(a)
7
all({12,34,56,77})
True
any({12,34,'python',0})
True
sum(a)
237
a={1,2,3}
b=a
b.add(4)
a
{1, 2, 3, 4}
b
{1, 2, 3, 4}
c=a.copy()
c
{1, 2, 3, 4}
c.add(9)
c
{1, 2, 3, 4, 9}
a
{1, 2, 3, 4}
a.add(7)
a
{1, 2, 3, 4, 7}
a.update(5)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a.update(5)
TypeError: 'int' object is not iterable
a.update({6,54,23})
a
{1, 2, 3, 4, 6, 7, 54, 23}
a.pop()
1
a.pop()
2
a.pop()
3
a.pop()
4
a.pop()
6
a.pop()
7
a.pop()
54
a.pop()
23
a.remove(23)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a.remove(23)
KeyError: 23
a.discard(23)
a
set()
a.discard(77)
a
set()
p={12,34,56}
p
{56, 34, 12}
p.remove(12)
p
{56, 34}
p.discard(12)
p
{56, 34}
