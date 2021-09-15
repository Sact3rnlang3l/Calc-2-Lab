"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    equation = input('Put your Maths here \n')
    tokens = equation.split(' ')

    if 'q' in tokens:
        print('Goodbye Then')
        break

    elif len(tokens) < 2:
        print('There Ain\'t enough numbers here for nothin\'')
        continue

    ops = tokens[0]
    num1 = tokens[1]

    if len(tokens) < 3:
        num2 = '0'

    else:
        num2 = tokens[2]

    if len(tokens) > 3:
        num3 = tokens[3]

    answer = None

    if not num1.isdigit() or not num2.isdigit():
        print('Those ain\'t numbers!')
        continue

    elif ops == '+':
        answer = add(float(num1),float(num2))

    elif ops == '-':
        answer = subtract(float(num1),float(num2))

    elif ops == '*':
        answer = multiply(float(num1),float(num2))

    elif ops == '/':
        answer = divide(float(num1),float(num2))

    elif ops == 'sqr' or 'square':
        answer = square(float(num1))

    elif ops == 'cube':
        answer = cube(float(num1))

    elif ops == 'pow' or 'power':
        answer = power(float(num1),float(num2))

    elif ops == 'mod' or 'modus':
        answer = mod(float(num1),float(num2))
    
    print(answer)

