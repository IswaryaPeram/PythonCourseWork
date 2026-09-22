from abc import ABC,abstractmethod
class payment(ABC):
    def source(self):
        print("scanner/upiid/mobile number")
    def amount(self):
        print("Enter the amount")
    def bank(self):
        print("select the bank")
    def pin(self):
        print("Enter the pin")
    @abstractmethod
    def paymentprocess(self):
        pass
    def paymentstatus(self):
        print("payment success/fail")

class HDFC(payment):
    def paymentprocess(self):
        print("payment is process through HDFC Bank")


class ICIC(payment):
    def paymentprocess(self):
        print("payment is process through ICIC Bank")

class UNION(payment):
    def paymentprocess(self):
        print("payment is process through UNION Bank")

class AXIS(payment):
    def paymentprocess(self):
        print("payment is process through AXIS Bank")

iswarya=HDFC()
iswarya.source()
iswarya.amount()
iswarya.bank()
iswarya.pin()
iswarya.paymentprocess()
iswarya.paymentstatus()

aishu=ICIC()
aishu.source()
aishu.amount()
aishu.bank()
aishu.pin()
aishu.paymentprocess()
aishu.paymentstatus()


lalitha=UNION()
lalitha.source()
lalitha.amount()
lalitha.bank()
lalitha.pin()
lalitha.paymentprocess()
lalitha.paymentstatus()

lali=AXIS()
lali.source()
lali.amount()
lali.bank()
lali.pin()
lali.paymentprocess()
lali.paymentstatus()



     
     
     
      