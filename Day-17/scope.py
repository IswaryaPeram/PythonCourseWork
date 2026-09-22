'''
local variable access the inside variable of the function .
global variable access the outside variable of the function .
'''
def display():
    n=10
    print("inside of the function: " ,n)

display()
print("outside of the function: " ,n)
 #if we access the variable the local we use global key

def display():
    global n
    n+=10
    print("inside of the function: " ,n)
n=10
display()
print("outside of the function: " ,n)

def display():
    course="pfs"
    def update():
        nonlocal course
        course="jfs"
        print("inner function:",course)
    update()
    print("outer function:",course)
display()

l=[1,2,3,4]
print(sum(l))
sum=20
print(sum)

def display(n):
    n.add(5)
    print("inside of the function:",n)
n={6,7,8}
print("outside of the function:",n)
display(n)

def display(n):
    n[5]=6
    print("inside of the function:",n)
n={1:2,3:4}
print("outside of the function:",n)
display(n)

def display(n):
    n+=10
    print("inside of the function:",n)
n=20
print("outside of the function:",n)
display(n)

def display(n):
    n+='python'
    print("inside of the function:",n)
n='language'
display(n)
print("outside of the function:",n)

