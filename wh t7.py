a=[1,2,3,4,5,6,7,8,9,12]
check=int(input("enter the number:"))
search=0
while(search<len(a)):
    if(check==a[search]):
         print("found")
         search = search + 1
         break
    search=search+1
else:
    print("not found")
