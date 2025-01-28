user_age = input("Please enter your age: ")
try:
    age = int(user_age)
except ValueError:
    print("Invalid input! Please enter a numeric age.")
    exit()

if age < 20:
    result = "fail"
elif 20 <= age <= 30:
    result = "pass"
else:
    result = "fail"

with open("q3.out", "w") as file:
    file.write(result)

print(f"The result '{result}' has been written to q3.out.")
