Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#opretors in python
a=10
b=5
a+b
15
a-b
5
a*2
20
a/2
5.0
a//2
5
a%2
0
a**3
1000
16***3
SyntaxError: invalid syntax
16**3
4096
a=10
b=5
a>b
True
a<b
False
a<=b
False
a>=b
True
a==b
False
a!=b
True
>>> a=10
>>> b=30
>>> a+=b
>>> a
40
>>> a-=b
>>> a
10
>>> a *= b
>>> a
300
>>> a /=b
>>> a
10.0
>>> a //=b
>>> a
0.0
>>> a **=b
>>> a
0.0
>>> a=20
>>> b=67
>>> a **=b
>>> a
1475739525896764129280000000000000000000000000000000000000000000000000000000000000000000
>>> a%=b
>>> a
20
>>> email = Ture
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    email = Ture
NameError: name 'Ture' is not defined
>>> email = Ture
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    email = Ture
NameError: name 'Ture' is not defined
>>> #
>>> email = Ture
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    email = Ture
NameError: name 'Ture' is not defined
>>> email = True
>>> password = False
>>> email and password
False
email or password
True
email not password
SyntaxError: invalid syntax
's' in 'aeiou'
False
's' not in 'aeiou'
True
4%2==0 and 4%24
4
4%2==0 and 4%24==0
False
3%3==0 or 23%2==0
True
#str list tuple set dict
a = "iswarya"
i in a
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    i in a
NameError: name 'i' is not defined. Did you mean: 'id'?
"i" in a
True
"s" not in a
False
"e" not in a
True
b=[1,2,3, 4]
4 in b
True
6 not in b
True
34  in b
False
c=(3,4,5,6)
7 not in c
True
5 in c
True
44 in c
False
set = {34,45,67,89}
34 in set
True
80 not in set
True
123 in set
False
s={2:3,3:8,8:0}
 2 in s
 
SyntaxError: unexpected indent
2 in s
True
4 in s
False
9 not in s
True
#identity
a=[2,3,4]
b=[2,3,4]
a==b
True
id(a)
2041474051072
id(b)
2041474051136
a=b
a
[2, 3, 4]
id(a)
2041474051136
a is b
True
b is a
True
a is not b
False
b is not a
False
#bitwise
# & ^ | ~ << , >>
2&3
2
14 & 45
12
15 ^ 12
3
~23
-24
~12
-13
14 | 23
31
2 <<3
16
2>>4
0
