def save_explanation(filename, content):
    with open(filename, "w") as f:
        f.write(content)
        
Q3_explanation = "To ensure the Flask app is only available on the local os, change 'host' from '0.0.0.0' to '127.0.0.1'."
save_explanation("../Q3/Q3.txt", Q3_explanation)