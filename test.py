students = []

while True:
    print("\n1. Add Student")
    print("2. Show All Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll = int(input("Enter roll no: "))
        marks = int(input("Enter marks: "))

        s = Student(name, roll, marks)
        students.append(s)
        print("Student Added Successfully!")

    elif choice == "2":
        for s in students:
            s.show_name()
            s.show_details()
            print("Grade:", s.grade())
            print("-----------")

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid choice")
