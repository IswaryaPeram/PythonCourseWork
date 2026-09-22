Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={}
type(d)
<class 'dict'>
d={1:2,2:3,4:5}
d
{1: 2, 2: 3, 4: 5}
>>> d={}
>>> d[1]=1
>>> d
{1: 1}
>>> d[12.3]=1
>>> d
{1: 1, 12.3: 1}
>>> d['str']=1
>>> d
{1: 1, 12.3: 1, 'str': 1}
>>> d[(1,2,3)]=1
>>> d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1}
>>> d[(2+3j)]=d
>>> d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): {...}}
>>> d[True]=d
>>> d
{1: {...}, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): {...}}
>>> d[[1,2,3,4,5]]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d[[1,2,3,4,5]]
TypeError: unhashable type: 'list'
>>> d[False]=1
>>> d
{1: {...}, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): {...}, False: 1}
>>> d[1]=1
>>> d[2]=12.3
>>> d[3]='str'
>>> d[4]=True
>>> d[6]=[1,2,3,4]
>>> d[7]=(3,4,5)
>>> d[8]={5,6,7}
>>> d[9]=frozenset({3,4,7})
>>> d[10]={1:2,4:7}
>>> d[11]=None
>>> d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): {...}, False: 1, 2: 12.3, 3: 'str', 4: True, 6: [1, 2, 3, 4], 7: (3, 4, 5), 8: {5, 6, 7}, 9: frozenset({3, 4, 7}), 10: {1: 2, 4: 7}, 11: None}
>>> d={}
>>> d[1]=2
>>> d
{1: 2}
>>> d[1]=3
>>> d
{1: 3}
data={'name':'Iswarya','course':'pfs','batch':65}
data
{'name': 'Iswarya', 'course': 'pfs', 'batch': 65}
'Iswarya' in data
False
'name' in data
True
'course' in data
True
'class' not in data
True
'batch' in data
True
data['age']
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    data['age']
KeyError: 'age'
data.get('name')
'Iswarya'
data.get('batch')
65
data.get('age')
data.get('age','key is not present')
'key is not present'
data['age']=21
data
{'name': 'Iswarya', 'course': 'pfs', 'batch': 65, 'age': 21}
data.update({'email':'iswarya@gmail.com','py':2026})
data
{'name': 'Iswarya', 'course': 'pfs', 'batch': 65, 'age': 21, 'email': 'iswarya@gmail.com', 'py': 2026}
data.popitem()
('py', 2026)
data
{'name': 'Iswarya', 'course': 'pfs', 'batch': 65, 'age': 21, 'email': 'iswarya@gmail.com'}
data.pop('age')=21
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
id(data)
2152299581888
data['py']
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    data['py']
KeyError: 'py'
data['batch']
65
data['batch']=45
data
{'name': 'Iswarya', 'course': 'pfs', 'batch': 45, 'age': 21, 'email': 'iswarya@gmail.com'}
id(data)
2152299581888
del data['batch']
data
{'name': 'Iswarya', 'course': 'pfs', 'age': 21, 'email': 'iswarya@gmail.com'}
data.clear()
data
{}
len(data)
0
data={'name': 'Iswarya', 'course': 'pfs', 'batch': 45, 'age': 21, 'email': 'iswarya@gmail.com'}
data
{'name': 'Iswarya', 'course': 'pfs', 'batch': 45, 'age': 21, 'email': 'iswarya@gmail.com'}
len(data)
5
max(data)
'name'
min(data)
'age'
data.keys()
dict_keys(['name', 'course', 'batch', 'age', 'email'])
data.values()
dict_values(['Iswarya', 'pfs', 45, 21, 'iswarya@gmail.com'])
data.items()
dict_items([('name', 'Iswarya'), ('course', 'pfs'), ('batch', 45), ('age', 21), ('email', 'iswarya@gmail.com')])
sorted(data)
['age', 'batch', 'course', 'email', 'name']
max(data)
'name'
d={2:2,3:3}
m=d
m
{2: 2, 3: 3}
d
{2: 2, 3: 3}
m[6]=6
m
{2: 2, 3: 3, 6: 6}
d
{2: 2, 3: 3, 6: 6}
n=d.copy()
n[5]=5
d
{2: 2, 3: 3, 6: 6}
m
{2: 2, 3: 3, 6: 6}
n
{2: 2, 3: 3, 6: 6, 5: 5}
d
{2: 2, 3: 3, 6: 6}
m
{2: 2, 3: 3, 6: 6}
data={'name': 'Iswarya', 'course': 'pfs', 'batch': 45, 'age': 21, 'email': 'iswarya@gmail.com'}
data.get('py')
dta.setdefaulat('name',2026)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    dta.setdefaulat('name',2026)
NameError: name 'dta' is not defined. Did you mean: 'data'?
data.setdefaulat('name',2026)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    data.setdefaulat('name',2026)
AttributeError: 'dict' object has no attribute 'setdefaulat'. Did you mean: 'setdefault'?
data.setdefaulat('name',21)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    data.setdefaulat('name',21)
AttributeError: 'dict' object has no attribute 'setdefaulat'. Did you mean: 'setdefault'?
