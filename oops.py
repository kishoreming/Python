from abc import ABC,abstractmethod

class kayment(ABC):
    @abstractmethod
    def pay(self,a):
        pass

class CreditCard(kayment):
    def pay(self,a):
        print("Paid",a,"usingCreditCard")

class UPI(kayment):
    def pay(self,a):
        print("Paid",a,"usingUPI")

a=int(input("EnterAmount:"))
ch=input("EnterChoice(CreditCard/UPI):")

if ch=="CreditCard"or ch=="CREDITCARD":
    k=CreditCard()
elif ch=="UPI" or ch=="upi":
    k=UPI()
else:
    print("InvalidChoice")
    exit()

k.pay(a)