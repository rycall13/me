from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_user():
    if request.method == "POST":
        return "Hello, Computer!"
    else:
        return "Hello, User!"

app.run(host='127.0.0.1', port=4356, debug=False)