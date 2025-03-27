def save_explanation(filename, content):
    with open(filename, "w") as f:
        f.write(content)

Q2_explanation = "Running two copies of flask applications on the same computer will cause an address problem, each app needs a different port number to avoid errors."
save_explanation("../Q2/Q2.txt", Q2_explanation)