number1 = int(input("Enter the first number : "))
number2 = int(input("Enter the second number : "))
number3 = int(input("Enter the third number : "))

if number1 > number2 and number1 > number3:
    print(number1 ,"is greater than", number2, "and",number3)
elif number1 == number2 and number1 > number3:
    print(number1, "and", number2, "are equal, and both are greater than",number3)
elif number1 == number3 and number1 > number2:
    print(number1, "and", number3, "are equal, and both are greater than",number2)
elif number2 == number3 and number2 > number1:
    print(number2, "and", number3, "are equal, and both are greater than",number1)
elif number1 == number3 == number2:
    print("All three numbers are equal")
elif number2 > number1 and number2 > number3:
    print(number2 ,"is greater than", number1, "and",number3)
else:
    print(number3 ,"is greater than", number1, "and",number2)