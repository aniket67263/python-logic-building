# Write a Python program that accepts one integer from the user and checks whether the number is even or odd.

number = int(input("Enter a number to check even or odd : "))

if number % 2 == 0:
    print(number, "is number is even.")
else:
    print(number, "is number is odd.")