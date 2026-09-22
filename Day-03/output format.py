Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a= 10
>>> b=12.3
>>> c="codegnan"
>>> a
10
>>> b
12.3
>>> c
'codegnan'
>>> print(a,b,c)
10 12.3 codegnan
>>> print("a=" ,a ,"b=" ,b , "c=" ,c)
a= 10 b= 12.3 c= codegnan
>>> print("a=",a ,"b=",b , "c=",c)
a= 10 b= 12.3 c= codegnan
>>> print("a=",a ,"b=",b , "c=",c sep='')
SyntaxError: invalid syntax
>>> print("a=",a ,"b=",b , "c=",c ,sep='')
a=10b=12.3c=codegnan
>>> print("a=",a ,"b=",b , "c=",c ,sep='\n')
a=
10
b=
12.3
c=
codegnan
>>> print("a=",a ,"b=",b , "c=",c ,end='')
a= 10 b= 12.3 c= codegnan
>>> print("a=",a ,"b=",b , "c=",c ,end='\n')
a= 10 b= 12.3 c= codegnan
>>> print("a=",a ,"b=",b , "c=",c ,end='\t')
a= 10 b= 12.3 c= codegnan	
>>> print("a=",a ,"b=",b , "c=",c ,end='\n\n')
a= 10 b= 12.3 c= codegnan

>>> a=10
... b=12.3
... c="codegnan"
SyntaxError: multiple statements found while compiling a single statement
>>> print('a={} b={} c={}'.format(a,b,c))
a=10 b=12.3 c=codegnan
>>> print('a={} b={} c={}'.format(b,a,c))
a=12.3 b=10 c=codegnan
>>> print('a={2} b={1} c={0}'.format(b,a,c))
a=codegnan b=10 c=12.3
>>> print('a={2} b={2} c={1}'.format(b,a,c))
a=codegnan b=codegnan c=10
