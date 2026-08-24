marks = int(input("Enter percentage: "))
if marks in range(90, 101):
    print("Excellent")
elif marks in range(75, 90):
    print("Very Good")
elif marks in range(60, 75):
    print("Good")
elif marks in range(40, 60):
    print("Average")
elif marks in range(0, 40):
    print("Fail")
else:
    print("Invalid Input")