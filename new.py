import getpass
username=input("username:")
password=getpass.getpass("password:")
found=False
with open("nf.txt","r") as file:
    for line in file:
        user,pwd=line.strip().split()
        if(username==user and password==pwd):
            found=True
            break
    if(found):
        print("login success")
    else:
        print("login failed")