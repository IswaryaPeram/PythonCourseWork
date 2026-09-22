
followers=eval(input("Follows Account: "))
if followers:
    closefriend=eval(input("close friend "))
    if closefriend:
        print("story visible")
    else:
        print("not in close friend list")
else:
    print("follow the account first")
    

reg=eval(input("Registered: "))
if reg:
    fee=eval(input("Fee paid: "))
    if fee:
        print("Tournament Entry confirmed")
    else:
        print("Entry Fee pending")
else:
    print("Registration Required")
    

link=eval(input("Enter your respones:"))
if link:
    permission=eval(input("permission Granted: "))
    if permission:
        print("file opend")
    else:
        print("access denied")
else:
    print("Invalid file link")
    

data={
    'lohitha':{'status':True,'python':90,'mysql':95,'flask':98},
    'dipak':{'status':False,'python':None,'mysql':None,'flask':None},
    'teja':{'status':True,'python':20,'mysql':45,'flask':56},
    'kalyani':{'status':True,'python':78,'mysql':83,'flask':90},
    'usharani':{'status':True,'python':80,'mysql':89,'flask':99}
}
name=input("Enter the name: ")
if name in data:
    if data[name]['status']:
        sum=data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg=sum/3
        print(f"hello{name}!!!")
        print(f"yuor average score is {avg}")
        if avg>=90:
            print("outstanding performance")
        elif avg>80:
            print("very good")
        elif avg>70:
            print("good, work hard")
        elif avg>35:
            print("failed")
        else:
            print(f"{name} not found in data")
            

n=int(input("Enter the number: "))
if n>0:
    print("positive number")
else:
    print("negative number")
    
n=int(input("Enter the number: "))
if n%2==0:
    print("even")
else:
    print("odd")
