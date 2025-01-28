student_names = []

while True:
    print("Menu:")
    print("1) Enter user")
    print("2) Exit")
    
    
    choice = input("Please select an option (1 or 2): ")
    
    if choice == "1":
        name = input("Enter a student's name: ")
        student_names.append(name.title())
        print(f"Added {name.title()} to the list.")
    elif choice == "2":
        print("Exiting and saving the list of students...")


        with open("q5.out", "w") as file:
            for student in student_names:
                file.write(student + "\n")
        print("The list of students has been written to q5.out.")
        break
    else:
        print("Invalid choice. Please select 1 or 2.")
