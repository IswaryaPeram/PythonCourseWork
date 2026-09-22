Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s ="    Hello       world     "
s.strip()
'Hello       world'
s.lstrip()
'Hello       world     '
s.rstrip()
'    Hello       world'
s.replace(' ','')
'Helloworld'
s='java-python -sql-flask-restapi'
s.split('-')
['java', 'python ', 'sql', 'flask', 'restapi']
s.rsplit('-',2)
['java-python -sql', 'flask', 'restapi']
s.lsplit('-',3)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s.lsplit('-',3)
AttributeError: 'str' object has no attribute 'lsplit'. Did you mean: 'rsplit'?
a='''python'''
a='''python
java
mysql
restapi
'''
a
'python\njava\nmysql\nrestapi\n'
a.splitlines()
['python', 'java', 'mysql', 'restapi']
c="python,  java sql flask"
c
'python,  java sql flask'
'@'.join(c)
'p@y@t@h@o@n@,@ @ @j@a@v@a@ @s@q@l@ @f@l@a@s@k'
>>> '-'.join(c)
'p-y-t-h-o-n-,- - -j-a-v-a- -s-q-l- -f-l-a-s-k'
>>> a='strings.py'
>>> a.partition('.')
('strings', '.', 'py')
>>> s='python.java.sql.flask'
>>> s.rpartition('.')
('python.java.sql', '.', 'flask')
>>> a='Peramiswarya.Reddy'
>>> s.startwith('Peramiswarya')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s.startwith('Peramiswarya')
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
>>> s.startswith('Peramiswarya')
False
>>> s.startswith('Peram')
False
>>> s.endswith('Reddy')
False
>>> s.endswith('.Reddy')
False
>>> b='peram.iswarya'
>>> s.startswith('per')
False
>>> s.startswith('p')
True
>>> s.endswith('a')
False
>>> 'iswarya'.lowercase()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    'iswarya'.lowercase()
AttributeError: 'str' object has no attribute 'lowercase'
>>> '2345'.isalnum()
True
>>> 'swaoprfd237'.isalnum()
True
>>> 'hello'.istitle()
False
>>> 'hello'.isspace()
False
>>> '23456'.isdigit()
True
>>> '234567'.isnumeric()
True
s='iswarya.reddy'
s.startswith('iswarya')