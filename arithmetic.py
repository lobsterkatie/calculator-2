def add(arg_list):
    sum = 0
    for index in range(0,len(arg_list)):
        addend = int(arg_list[index])
        sum += addend

    return sum

def subtract(arg_list):
    num1 = int(arg_list[0])
    num2 = int(arg_list[1])

    return num1 - num2

def multiply(arg_list):
    num1 = int(arg_list[0])
    num2 = int(arg_list[1])

    return num1 * num2

def divide(arg_list):
    num1 = float(arg_list[0])
    num2 = int(arg_list[1])

    return num1/num2

def square(arg_list):
    num1 = int(arg_list[0])

    return num1 ** 2

def cube(arg_list):
    num1 = int(arg_list[0])

    return num1 ** 3

def power(arg_list):
    base = int(arg_list[0])
    exponent = float(arg_list[1])

    return base ** exponent

def mod(arg_list):
    num1 = int(arg_list[0])
    num2 = int(arg_list[1])

    return num1 % num2



