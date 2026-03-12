'''
passcode="kis"
usname="kish"
password=str(input("enter your password:"))
username=str(input("enter your username:"))
if(username==usname):
    if(password==passcode):
        print("logged in")
    else:
        print("invalid password")
else:
    print("invalid username")

'''
'''
age=int(input("enter your age:"))
degree=str(input("enter your degree(BE,BCA,MCA,ME):"))
if (age>18):
    if degree in ("BCA,BE,ME,MCA"):
        print("YOU ARE ELIGIBLE FOR THIS JOB")
    else:
        print("YOUR DEGREE IS NOT ELIGIBLE FOR THIS JOB")
else:
    print("YOUR AGE IS NOT ELIGIBLE FOR THIS JOB")
'''
'''
age=int(input("enter your age:"))
degree=str(input("enter your degree(BE,BCA,MCA,ME):"))
if (age>18):
    if degree in ("BCA,BE,ME,MCA"):
        print("YOU ARE ELIGIBLE FOR THIS JOB")
    else:
        print("YOUR DEGREE IS NOT ELIGIBLE FOR THIS JOB")
else:
    print("YOUR AGE IS NOT ELIGIBLE FOR THIS JOB")

'''
'''
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
'''

'''
mark=int(input("enter your mark:"))
if(mark>=90):
    print("your mark is A")
else:
    if(mark>=75):
        print("your mark is B")
    else:
        if(mark>=50):
            print("your mark is C")
        else:
            print("your mark is fail")

'''
