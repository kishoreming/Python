month = int(input("Enter month number (1-12): "))
if month in (12, 1, 2):
    print("Winter season")
elif month in (3, 4, 5):
    print("Summer season")
elif month in (6, 7, 8, 9):
    print("Rainy season")
elif month in (10, 11):
    print("Autumn season")
else:
    print("Invalid month number")
