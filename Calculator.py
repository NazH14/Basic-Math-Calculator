num1 = float(input("first number: "))
num2 = float(input("second number: "))
operation = input("what operation would you like to apply? ")

if operation == "+":
    result = num1 + num2
    print(result)
elif operation == "-":
    result = num1 - num2
    print(result)
elif operation == "*":
    result = num1 * num2
    print(result)
elif operation == "/":
    result = num1 / num2
    print(result)
else:
    print("Invalid operation")