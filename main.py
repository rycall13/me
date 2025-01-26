#Q1

user_name = input("Please enter your name: ")

formatted_name = user_name.title()

greeting_message = f"Hello, {formatted_name}"

print(greeting_message)

with open("q1.out", "w") as file:
    file.write(greeting_message)
