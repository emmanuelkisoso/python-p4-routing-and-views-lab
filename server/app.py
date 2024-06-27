#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text

@app.route('/count/<int:num>')
def count(num):
    output = ''
    for i in range(num+1):
        output += str(i) + '\n'
    return output

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return "Invalid input.Please enter numbers.", 400
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return f'Invalid operation: {operation}', 400

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
