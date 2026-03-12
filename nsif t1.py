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
