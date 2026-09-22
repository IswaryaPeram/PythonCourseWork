
n=45678923
sumofdigits=0
while n>0:
    sumofdigits+=n%10
    n//=10
print("sum of digits:",sumofdigits)


n=9874234
proofdigits=1
while n>0:
    proofdigits *=n%10
    n//=10
print("sum of digits:",proofdigits)



n=28554327
res=0
while n>0:
    rem=n%10
    if rem%2==0:
       res+=rem
    n//=10
print(res)


l=[7,9,23,8,9,0,0,0,3,7,0,13,0]
while 0 in l:
    l.remove(0)
    print(l)
    

l=[2,4,8,9,34,56,23,89,87,9]
i,j=0,len(l)-1
while i<=j:
    if i==j:
        print(l[i])
    else:
        print((l[i]+l[j]))
    i+=1
    j-=1
    
data={
    'pen':5,
    'pencils':10,
    'book':50,
    'plank':100,
    'egg':200,
    'rice':300,
    'oil':250
}
bill=0
while True:
    product=input("Enter the product name or [E]xit: ")
    if product == 'E'or product=='e':
        print("Thanks for shopping")
        print("Total bill:",bill)
        break
    else:
        quantity=int(input("Enter the quantity: "))
        bill += data[product]*quantity



    




    