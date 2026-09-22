
sales=int(input("Enter the sales: "))
if sales>1000:
    print("Best seller")
    
eli_acc = eval(input("Eligible Account: "))
ver_sub = eval(input("Meta Verified subscription: "))
if eli_acc and ver_sub:
    print("verified Badge Granted")
    
rain_status = eval(input("Enter the rain status: "))
if rain_status:
    print("Extra Rain Change Applied")