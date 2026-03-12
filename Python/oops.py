from abc import ABC,abstractmethod

class kayment(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCard(kayment):
    def pay(self):
        print("Paid","usingCreditCard")

class UPI(kayment):
    def pay(self):
        print("Paid","usingUPI")

a=int(input("EnterAmount:"))
b=a
ch=input("EnterChoice(CreditCard/UPI):")

if ch=="CreditCard"or ch=="CREDITCARD":
    k=CreditCard()
elif ch=="UPI" or ch=="upi":
    k=UPI()
else:
    print("InvalidChoice")
    exit()

k.pay()