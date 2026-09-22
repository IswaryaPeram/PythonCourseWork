'''
username = input("Enter the username: ")
password = input("Enter the password: ")
if username == "admin" and password == "admin123":
    print("login successfuly")
else:
    print("invalid ")
   

products = ["Laptop","mobile","bag","bottel"]
search = input("search product: ")
if search in products:
    print("product Found")
else:
    print("product Not found")
   
order_bill=int(input("enter the bill: "))
if order_bill>=99:
    final_bill =order_bill
else:
    final_bill=order_bill+30
print("Final Bill Amount:",final_bill)


seat_type=input("Enter your seat: ")
booking_days=int(input("Enter your booking days: "))
festival=input("Enter  festival or Not: ").lower()=="true"
age=int(input("Enter your age: "))
price=5000
if seat_type=='Business':
    price*=1.4
elif seat_type=='premium':
    price*=1.2
if booking_days>=30:
    price*=0.9
elif booking_days<=7:
    price*=1.25
if festival:
    price*=1.2
if age>60:
    price*=0.85
print(price)
'''
age=int(input("Enter the age: "))
health_score=int(input("Enter health score: "))
vehicle=input("Enter vehicle type: ")
premium=10000
if age<25:
    premium*=1.2
elif age>50:
    premium*1.15
if health_score>=80:
    premium*0.90
elif health_score<60:
    premium*1.2
if vehicle=='sports car':
    premium*1.3
elif vehicle=='suv':
    premium*1.15
print(premium)