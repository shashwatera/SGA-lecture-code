num = int(input("Enter number:"))

if isinstance(num, float):
    print("Invalid Input: Decimal cannot be prime")

if num < 2:
    print("Not prime") 
else:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print("Prime")
    else:
        print("Not prime")