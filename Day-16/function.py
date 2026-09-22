'''
funtion is block of code perform specfic task.insted of writing the same code again and again 
code resuablity: write code once and use many times
makes code simple:no need to write code again and again 
improve readability:function name makes the purpose of code clear
easy debugging
provides modularity
reduce program complexity
improve programm organiztion
helps scalability

def functionname(arg):
    #stsmt
    return(opt)
funtionname(para)

def gst(price):
    print("original price:",price)
    print("Final price:",price+price*0.18)
gst(1000)
gst(800)
gst(500)
gst(300)
gst(10000)

def table(n):
    print(f"{n}-Table")
    print('-------------')
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')
for i in range(1,12):
    table(i)

def isleap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "Leap year"
    else:
        return "Not a leap year"
print(isleap(2012))
print(isleap(2020))
print(isleap(2026))

def prime(number):
    for i in range(2,number+1):
        if number%i==0:
            return "not a prime number"
    return "prime number"
print(prime(16))
print(prime(5))
print(prime(7))
print(prime(8))
print(prime(3))

#positional arguments:
def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)
display('iswarya','iswarya@gmail','ishu@123')
display('iswarya@gmail','iswarya','ishu@123')
display('iswarya','ishu@123','iswarya@gma')

#keyword argument:

def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)
display(name='iswarya',email='iswarya@gmail',pwd='ishu@123')
display(email='iswarya@gmail',name='iswarya',pwd='ishu@123')
display(name='iswarya',pwd='ishu@123',email='iswarya@gmail')

#default argument:

def display(name,email,pwd=None):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)
display('iswarya','email','ishu@123')
 
#variable argument:

def display(*names):
    print(names)
display('iswarya')
display('Aishwarya','iswarya')
display('Aishwarya','iswarya','Aishu')

def display(**names):
    print(names)
display(n1='iswarya')
display(n1='Aishwarya',n2='iswarya')
display(n1='Aishwarya',n2='iswarya',n3='Aishu')

def table(n):
    print(f"{n}-table")
    print("------------------------------")
    for i in range(1,11):
        print(f"{n} * {i}= {n*i}")
for i in range(1,26):
    table(i)

a=int(input("Enter the number:"))
for i in range(1,11):
    print(f"{a}*{i} = {a*i}")

n="iswarya"
for i in range(-1):
    print(n)

print(int(input())*55)
'''
a="iswarya"
vowels=0
consonates=0

