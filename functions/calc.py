def add(a,b):
    answer = a+b
    return answer

def subtract(a,b):
    answer = a-b
    return answer

def multiply(a,b):
    answer = a*b
    return answer

def division(a,b):
    answer = a//b
    return answer

def modulus (a,b):
    answer = a%b
    return answer

def exponent (a):
    answer= a**2
    return answer

def cube(a):
    answer =a*a*a
    return answer

def square(a):
    answer = a*a
    return answer

def sum(*numbers):
    total = 0
    for number in numbers :
        print(number)
        total+=number
    return total




