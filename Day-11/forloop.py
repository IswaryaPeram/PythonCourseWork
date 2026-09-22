
s='python programming'
for i in s:
    print(i)
    

l=[1,2,3,4,5]
for num in l:
    print(num)
    

prices=(98,456,678,908)
for price in prices:
    print(price)

   
names={'mounsri','usharani','lohitha'}
for name in names:
    print(name)


d={1:2,4:5,7:9}
for i in d:
    print(i,d[i])
    

for i in range(1,11):
    print(i)
  

for i in range(2,21,2):
    print(i)
    

for i in range(5,101,5):
    print(i)
    

for i in range(5,0,-1):
    print(i)
    

for i in range(19,0,-2):
    print(i)
    
s='python programming'
for i in range(len(s)):
    print(i,s[i])
    

a=[1,2,3,4,5]
for i in range(len(a)):
    print(i,a[i])
    
s=(5,6,7,8,9)
for i in range(len(s)):
    print(i,s[i])
    

s=[123,344,567,890]
for i in enumerate(s):
    print(i[0],i[1])
    

s=(123,344,567,890)
for i in enumerate(s):
    print(i)
    

s={123,344,567,567}
for i in enumerate(s):
    print(i)
    

s={1:2,3:4,5:6}
for i in enumerate(s):
    print(i,s[1],s[3],s[5])

    
for i in range(1,11):
    if i==5:
        break
    print(i)

    
for i in range(1,11):
    if i==5:
        continue
    print(i)
    

l=[23,34,54,56,89]
n=56
for i in l:
    if i==n:
        print(n,"found")
        break
else:
    print(n,"not found")
   

l=[23,34,54,56,89]
n=23
for i in l:
    if i==n:
        print(n,"found")
       
else:
    print(n,"not found")
 

pin=1234
for i in range(5):
    epin=int(input("Enter the pin: "))
    if epin==pin:
        print("unlock phone")
        break
    else:
        print("Invalid pin")
else:
    print("Try after 30 seconds")
   
n=7
for i in range(2,n//2+1):
    if n%i==0:
        print("Not a prime number")
        break
else:
    print("prime number")