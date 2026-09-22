data={
    'pen':5,
    'pencils':10,
    'book':50,
    'plank':100,
    'egg':200,
    'rice':300,
    'oil':250
}
for i in data:
    print(i.ljust(20),data[i])
product=input("Enter the product: ").split()
print("--------------bill------------")
bill=0
for i in product:
    print(i.ljust(20),data[i])
    bill += data[i]
print("Total bill".ljust(20),bill)