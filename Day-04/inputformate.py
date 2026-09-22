Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # int str float complex list tuple set dict
>>> a=input()
a
>>> 10
10
>>> a=input()
3
>>> a
'3'
>>> c= intput()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    c= intput()
NameError: name 'intput' is not defined. Did you mean: 'input'?
>>> c= input()
'codegnan
>>> c
"'codegnan"
>>> a=int(input())
45
>>> a
45
>>> c=float(input('Enter the cgpa')
...         45.4
...         
SyntaxError: '(' was never closed
>>> c=float(input('Enter the cgpa'))
...         
Enter the cgpa 34.6
>>> c
...         
34.6
>>> names = 'usharani,lohitha,mounasri'
...         
>>> name.split(',')
...         
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    name.split(',')
NameError: name 'name' is not defined. Did you mean: 'names'?
>>> names.split(',')
...         
['usharani', 'lohitha', 'mounasri']
>>> courses = 'python -sql-c++-flask'
...         
courses.split('-')
        
['python ', 'sql', 'c++', 'flask']
list=input("Enter values:").split
        
Enter values:2,3,4,5,6,
list
        
<built-in method split of str object at 0x000001A618D4D7F0>
list=list(input("Enter values:").split)
        
Enter values:2,3,4,5,6,7,8,
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    list=list(input("Enter values:").split)
TypeError: must be str or None, not builtin_function_or_method
list
        
<built-in method split of str object at 0x000001A618D4D7F0>
Enter values:2,3,4,5,6,7,8,
        
SyntaxError: invalid syntax
list=input("Enter values:").split
        
Enter values:[1,3,4,5]
list
        
<built-in method split of str object at 0x000001A618D4EEF0>
name=list(input("Enter values:").split)
        
Enter values:6,7,8
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    name=list(input("Enter values:").split)
TypeError: must be str or None, not builtin_function_or_method
softskills ='communication quickleaner'
        
softskills.split()
        
['communication', 'quickleaner']
names = input("Enter the names:").split()
        
Enter the names:usharani lohitha mounasri
names
        
['usharani', 'lohitha', 'mounasri']
names = tuple(input("Enter the names:").split())
        
Enter the names:usharani lohitha mounasri
names
names
        
('usharani', 'lohitha', 'mounasri')
marks = input().split()
        
12 34 56,78
        
SyntaxError: invalid syntax
12,34,56,78
        
(12, 34, 56, 78)
marks
        
['names']
markes = input().split
        
map(int,marks)
number = input().split()
        
14 46 78 90
number
        
['14', '46', '78', '90']
map(int,marks)
        
<map object at 0x000001A618D61BA0>
list(map(int,marks))
        
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    list(map(int,marks))
TypeError: must be str or None, not map
>
list(map(int,number))
        
SyntaxError: invalid syntax
map(int,number)
        
<map object at 0x000001A618D625C0>
list(map(int,number))
        
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    list(map(int,number))
TypeError: must be str or None, not map
list(map(int,input))
        
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    list(map(int,input))
TypeError: 'builtin_function_or_method' object is not iterable
a,b =[1,2]
        
a
        
1
b
        
2
a,b,c=(1,12.3,"str")
        
a
        
1
b
        
12.3
c
        
'str'
email,password = input("Enter the email,password: ").split()
        
Enter the email,password: iswarya@gmail.com,1234
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    email,password = input("Enter the email,password: ").split()
ValueError: not enough values to unpack (expected 2, got 1)
email,password = input("Enter the email,password: ").split()
        
Enter the email,password: iswarya@gmail.com 1234
email
        
'iswarya@gmail.com'
password
        
'1234'
name,marks = input("Enter the name marks: ").split()
        
Enter the name marks: iswarya 87
name
        
'iswarya'
marks
        
'87'
a,b,c=list(map(input().split()))
        
13 24 56
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a,b,c=list(map(input().split()))
TypeError: map() must have at least two arguments.
a,b,c=list(map(int,input().split()))
        
23 56 89
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
TypeError: must be str or None, not map
status = eval(input())
        
True
status
        
True
type(status)
        
<class 'bool'>
status
        
True
status = eval(input())
        
2+3j
status
        
(2+3j)
type(status)
        
<class 'complex'>
status = eval(input())
        
(2,3,4,5,)
status
        
(2, 3, 4, 5)
status=eval(input())
        
[2,3,6,7]
atatus
        
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    atatus
NameError: name 'atatus' is not defined. Did you mean: 'status'?
status
        
[2, 3, 6, 7]
status = eval(input())
        
{1:1,2:2,3:3,4:4,5:5}
status
        
{1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
