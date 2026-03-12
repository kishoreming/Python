'''
def rev(k):
    print(k[::-1])
rev(k="kis")
'''
'''
def arithmetic(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a//b)
arithmetic()
'''
'''
def oden(a,b):
    if(a%2==0):
        print(a,"is even")
    else:
        print(a,"is  odd")
    if(b%2==0):
        print(b,"is even ")
    else:
        print(b,"is odd ")
oden()
'''
a="i love python"
rev=""
for i in a.split():
    rev=i+" "+rev
print(rev)