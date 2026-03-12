'''
try:
    a=int(input("Enter a number: "))
    b=int(input("Enter b number: "))
    result=a/b
except ZeroDivisionError:
    print("cannot div by zero")
    b=int(input("Enter a number:"))
    result=a/b
except ValueError:
    print("invalid input")
else:
    print(result)
finally:
    print(result)
    print("completed")
'''
'''
try:
    age = int(input("Enter age: "))
    if age<18:
        raise ValueError("Age must be 18 or above")
    print("You can vote")
except ValueError as e:
    print("Error:",e)
'''


class MyException(Exception):
    pass
try:
    age = int(input("Enter age: "))

     if age < 18:
        raise MyException("Age must be 18 or above")

    print("You can vote")

except MyException as e:
    print("Custom Error:", e)

except ValueError:
    print("Invalid input")
