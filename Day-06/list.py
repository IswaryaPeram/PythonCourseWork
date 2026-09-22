
'''
Enter "help" below or click "Help" above for more information.
a=[]
a=list()
type(a)
<class 'list'>
a=[2,3,4,2,3,4,2,3,4]
a
[2, 3, 4, 2, 3, 4, 2, 3, 4]
a=list(1,2,3,)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a=list(1,2,3,)
TypeError: list expected at most 1 argument, got 3
a=list(2)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a=list(2)
TypeError: 'int' object is not iterable
s=[1,2,3]
d=[4,5,6]
s+d
[1, 2, 3, 4, 5, 6]
s*2
[1, 2, 3, 1, 2, 3]
l=[234,98,809,456]
l
[234, 98, 809, 456]
l[2]
809
l[-2]
809
l[:-1]
[234, 98, 809]
l[2:1]
[]
>>> l[1:2]
[98]
>>> l[:-3]
[234]
>>> l[-1:-3]
[]
>>> c=[9,34,56,23,12,45]
>>> c
[9, 34, 56, 23, 12, 45]
>>> max(c)
56
>>> min(c)
9
>>> id(c)
2420613926656
>>> c[2]=31
>>> c
[9, 34, 31, 23, 12, 45]
>>> c.append(78)
>>> c
[9, 34, 31, 23, 12, 45, 78]
>>> c.insert(2,33)
>>> c
[9, 34, 33, 31, 23, 12, 45, 78]
>>> c.extend([2,3,45,21])
>>> c
[9, 34, 33, 31, 23, 12, 45, 78, 2, 3, 45, 21]
>>> c.pop()
21
>>> c.pop(2)
33
>>> c.remove[3]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    c.remove[3]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> c.remove(3)
>>> c
[9, 34, 31, 23, 12, 45, 78, 2, 45]
>>> del c[1]
>>> c
[9, 31, 23, 12, 45, 78, 2, 45]
>>> c.clear()
>>> c
a=[1,2,3,4,5]
a.remove[4]
print(a)


'''
a=[11,12,13,14,15]
even=[]
for i in range(len(a)):
    if a[i]%2==0:
        even.append(i)
        print(i)
      