num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
operation = input("Operation: ")

if operation in ("multiplication", "multiply"):
    print(num1 * num2)
elif operation in ("division", "divide"):
    if num2 == 0:
        print("Undefined")
    else:
        print(num1 / num2)
elif operation in ("add", "addition"):
    print(num1 + num2)
elif operation in ("subtract", "subtraction"):
    print(num1 - num2)
else:
    print("Invalid operation")