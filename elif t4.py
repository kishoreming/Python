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
