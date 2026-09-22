Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #string:String is a sequence of characters enclosed within single quotes(' '),(" "),
>>> a='python'
>>> b="programming"
>>> c='''language'''
>>> a
'python'
>>> b
'programming'
>>> c
'language'
>>> #operations on Strings
>>> #concatenation:joining two or more string
>>> #repetition:repeating a string multiple times.
>>> #indexing:accessing individual characters using indice.
>>> #slicing:substring of the string.
>>> #membership(in, not in):
>>> a='hello'
>>> b='world'
>>> a+b
'helloworld'
>>> a+" "+b
'hello world'
>>> print((a*3)
...  a
...       
SyntaxError: '(' was never closed
>>> b='hello'
...       
>>> a*3
...       
'hellohellohello'
>>> a * 3
...       
'hellohellohello'
>>> w='python'
...       
>>> w[0]
...       
'p'
>>> w[-1]
...       
'n'
>>> t='slicing'
...       
t[0:3]
      
'sli'
t[:6]
      
'slicin'
t[-1:-6]
      
''
t[:-1]
      
'slicin'
t='python'
      
a=[1,2,3,4]
      
1 in a
      
True
2 in 4
      
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    2 in 4
TypeError: argument of type 'int' is not iterable
3 in a
      
True
7 not in a
      
True
a=[4,5,6,7,8]
      
len(a)
      
5
max(a)
      
8
min(a)
      
4
sorted(a)
      
[4, 5, 6, 7, 8]
chr(4)
      
'\x04'
ord(a)
      
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    ord(a)
TypeError: ord() expected string of length 1, but list found
ord('a')
      
97
n='python'
      
n.upper()
      
'PYTHON'
n.lower()
      
'python'
n.capitalize()
      
'Python'
n.title()
      
'Python'
n.swapcase()
      
'PYTHON'
n.casefold()
      
'python'
a='IswaRya'
      
a.casefold()
      
'iswarya'
k='python'
      
k.center(50,"*")
      
'**********************python**********************'
k.ljust(10,"-")
      
'python----'
k.rjust(40,"*")
      
'**********************************python'
f='iswarya'
      
f.find('a')
      
3
f.rfind(a)
      
-1
f.lfind('w')
      
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    f.lfind('w')
AttributeError: 'str' object has no attribute 'lfind'. Did you mean: 'find'?
f.find(w)
      
-1
l="chaitu"
      
l.index("u")
      
5
l.rindex("t")
      
4
l.count("a")
      
1
t='python programming'
      
t.startswith('py')
      
True
t.endswith("ing")
      
True
t.isalpha()
      
False
t="123python"
      
t
      
'123python'
t="1234"
      
t.isalnum()
      
True
t='ishu'
      
t.isalpha()
      
True
t.islower()
      
True
y='LALLI'
      
y.isupper()
      
True
p=" aishu"
      
p.isspace()
      
False
p.istitle()
      
False
a="Ishu"
      
a.istitle()
      
True
r="python"
      
r.replace("p","b")
      
'bython'
a="a,b,c"
      
a.split("a")
      
['', ',b,c']
a,split()
      
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a,split()
NameError: name 'split' is not defined
a.split()
      
['a,b,c']
p="hello\nworld"
      
p.splitlines()
      
['hello', 'world']
p.join()
      
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    p.join()
TypeError: str.join() takes exactly one argument (0 given)
