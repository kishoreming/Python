age=int(input("enter your age:"))
degree=str(input("enter your degree(BE,BCA,MCA,ME):"))
if (age>18):
    if degree in ("BCA,BE,ME,MCA"):
        print("YOU ARE ELIGIBLE FOR THIS JOB")
    else:
        print("YOUR DEGREE IS NOT ELIGIBLE FOR THIS JOB")
else:
    print("YOUR AGE IS NOT ELIGIBLE FOR THIS JOB")