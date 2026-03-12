num=int(input("enter a number:"))
if(num>=0):
    print("num is positive")
    if(num%2==0):
        print("num is even")
        if(num%3==0):
            print("num is div by 3")
        else:
            print("num is not div by 3")

    else:
        print("num is odd")
else:
    print("num is negative")