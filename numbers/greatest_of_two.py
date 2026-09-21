number1 = int(input("Enter the first number : "))
number2 = int(input("Enter the second number : "))

if number1 > number2:
    print(number1 ,"is greater than", number2)
elif number1 == number2:
    print("Both the numbers are equal")
else:
    print(number2 ,"is greater than", number1)