student_names = []

while True:
    name = input("Enter a student's name (or type 'exit' to finish): ")
    if name.lower() == 'exit': 
        break
    student_names.append(name.title()) 


with open("q4.out", "w") as file:
    for student in student_names:
        file.write(student + "\n")


print("The list of students has been written to q4.out.")
