'''

file=open("nf.txt","a")
file.write(" nalla than irrukum")
file=open("nf.txt","r")
print(file.read())
file.close()
'''
with open("nfile.txt","r") as file:
    print(file.read())