students = {}  

while True:
    print("\n1. Add student")
    print("2. Show students with avg > 80")
    print("3. Update marks")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        roll = input("Enter roll number: ")
        if roll in students:
            print("Roll number already exists.")
        else:
            name = input("Enter name: ")
            n = int(input("Number of marks to enter: "))
            marks = []
            for i in range(n):
                m = float(input("Enter mark " + str(i+1) + ": "))
                marks.append(m)
            students[roll] = (name, marks)
            print("Student added.")

    elif choice == '2':
        print("Students with average > 80:")
        found = False
        for roll in students:
            name = students[roll][0]
            marks = students[roll][1]
            total = 0
            for m in marks:
                total = total + m
            if len(marks) > 0:
                avg = total / len(marks)
            else:
                avg = 0
            if avg > 80:
                print(roll, ":", name, "(avg =", avg, ")")
                found = True
        if not found:
            print("None.")

    elif choice == '3':
        roll = input("Enter roll number to update: ")
        if roll not in students:
            print("Roll number not found.")
        else:
            name = students[roll][0]
            old_marks = students[roll][1]
            print("Current marks for", name, ":", old_marks)
            n = int(input("Number of new marks to enter: "))
            new_marks = []
            for i in range(n):
                m = float(input("Enter mark " + str(i+1) + ": "))
                new_marks.append(m)
            students[roll] = (name, new_marks)
            print("Marks updated.")

    elif choice == '4':
        break

    else:
        print("Invalid choice.")