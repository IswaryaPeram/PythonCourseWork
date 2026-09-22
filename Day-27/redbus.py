class Redbus:
    bus = {i: "Avaliable" for i in range(1,11)}
    def displayseats(self):
        print("---xyz bus---")
        for i in Redbus.bus:
            print(i,Redbus.bus[i])
    def booking(self,seatno):
        for i in Redbus.bus:
            if i == seatno and Redbus.bus[i] == 'Available':
                Redbus.bus[i] = 'Booked'
                print(f"your seat - {seatno} is sucessfully Booked")
                break
        else:
            print(f"your seat - {seatno} is already Booked")
class users(Redbus):
    def __init__(self,name,email,phoneno):
        self.name=name
        self.email=email
        self.phoneno=phoneno
        print(f"Hello {self.name},Welcome to the RedBus")
class driver(Redbus):
    def __init__(self,name,phoneno):
        self.name=name
        self.phoneno=phoneno
        self.busnumber=self.busnumber
        print(f"")
       

aishu=users('aishu','aishu@gmail.com',233456789)
aishu.displayseats()
aishu.booking(4)
aishu.displayseats()
aishu.booking(4)

a=driver('a',23459875,45)
a.displayseats()

        