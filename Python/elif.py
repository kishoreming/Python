a=int(input("Enter a number:"))
b=int(input("Enter b number:"))
c=int(input("Enter c number:"))
if(a>b and a>c):
    print("a is greaterst")
elif(b>a and b>c):
    print("b is greater")
else:
    print("c is greater")

a=int(input("Enter a number:"))
b=int(input("Enter b number:"))
o=input("enter operator(+,-,*,/):")
if(o=="+"):
    print("c is",a+b)
elif(o=="-"):
    print("c is",a-b)
elif(o=="*"):
    print("c is",a*b)
elif(o=="/"):
    print("c is",a/b)

signal_light=str(input("Enter the signal_color(red,yellow,green):"))
if(signal_light=="red"):
    print("stop")
elif(signal_light=="green"):
    print("go")
elif(signal_light=="yellow"):
    print("ready")
else:
    print("not recognized")

day = int(input("enter date: "))
if day in (2, 9, 16, 23):
    print("monday")
elif day in (3, 10, 17, 24):
    print("tuesday")
elif day in (4, 11, 18, 25):
    print("wednesday")
elif day in (5, 12, 19, 26):
    print("thursday")
elif day in (6, 13, 20, 27):
    print("friday")
elif day in (7, 14, 21, 28):
    print("saturday")
elif day in (1, 8, 15, 22):
    print("sunday")
else:
    print("not recognized")

month = int(input("Enter month number (1-12): "))
if month in (12, 1, 2):
    print("Winter season")
elif month in (3, 4, 5):
    print("Summer season")
elif month in (6, 7, 8, 9):
    print("Rainy season")
elif month in (10, 11):
    print("Autumn season")
else:
    print("Invalid month number")
