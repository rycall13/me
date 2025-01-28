user_age = input("Please enter your age: ")
try:
    age = int(user_age)
except ValueError:
    print("Invalid input! Please enter a numeric age.")
    exit()


age_plus_5 = age + 5


with open("q2.out", "w") as file:
    file.write(f"User's provided age: {age}\n")
    file.write(f"Age plus 5: {age_plus_5}\n")

print("The age and calculated age have been written to q2.out.")