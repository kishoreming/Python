'''
n=int(input("Enter a number:"))
fact=1
i=1
while(i<=n):
    fact=fact*i
    i=i+1
print("Factorial is:",fact)
'''
'''
a=input("")
r=a[::-1]
while(a==r):
    print("it is a palindrome")
    break
else:
    print("it is not a palindrome")
'''
'''
n=int(input("enter the number:"))
i=n
while(i>=0):
    print(i)
    i=i-1
'''
'''
n=int(input("enter the number:"))
sum=0
i=1
while(i<=n):
    sum=sum+i
    i=i+1
print("sum is:",sum)
'''
'''
n=1
while(n<=50):
    if(n%5!=0):
      n=n+1
      continue
    print(n)
    n=n+1
'''
'''
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
'''
'''
n=int(input("enter the number:"))
while(n>=0):
    if(n==0):
        print("stop")
        break
    print(n)
    break
'''
