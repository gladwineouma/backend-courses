def greet(name):
    print("My name is {}".format(name))

# default argument
def greeting(name = "guest"):
    return f"Hello, {name}!"

# keyword argument
def add(a,b):
    return a+b

# list comprehension. simple code
def squares():
    squares = [x**2 for x in range(8)]
    return squares

# list with condition
def even_numbers():
    even = [x for x in range(50) if x%2==0]
    return even

def nums():
    num = []
    for x in range(10):
        num.append(x**2)
        return num

# dictionaries
def dictionaries():
    student = {"name": "James Kamau","age": "20","course":"Python"}
    return student

def calculator():
    print ("simple calcuator")

    num1= float(input("Enter first number"))
    op = input("Choose operation(+,-,*,/):") 
    num2=float(input("Enter second number"))

    if op =='+':
        print("result ",num1 + num2)
    elif op=='-':
        print("result", num1 - num2)
    elif op == '*':
        print("result", num1 * num2)
    elif op =='/':
        if num2 !=0:
            print ("result", num1 / num2)
        else:
            print("Error Division by zero!")
    else:
        print("Invalid operation")
    calcuator()


def squares():
    squares = []
    for x in range (10):
        squares.append(x**2)

def calculate(num1, num2=4):
    res = num1 * num2
    print(res)

def person(name, age):
    print(f"My name is {name} and I am {age} years old.")


def func1(*args):
    for args in args:
        print(args)

def calculation(a,b):
    sum = a+b
    sub = a - b
    print(sum,sub)

def show_employee(name, salary= 9000):
    return name, salary


# nested function?
def outer(a,b):
    squares = a**2

    def inner(a,b):
        return a+b

# def reccursion(num):
#     if num:
#         return num + addition(num -1)
#     else:
#         return 0
#     res = additon(10)
#     print (res)

def display_student(name,age):
    print (name, age)

#  To give a function a new name   
showStudent = display_student

def numbers():
    res = [i for i in range (4,30+1)if i %2 == 0]
    print (res)  

# printing max in python
def maxi():
    num = [2,3,4,56,7,9]
    return(max(num))
# The exercise requires you to create a function that can accept any number of keyword arguments. A keyword argument is where you specify the name of the argument along with its value (e.g., name="Alice", age=30). Inside the function, you need to access these arguments and print them in a key-value format.

# Create a function print_info(**kwargs) that accepts keyword arguments and prints the key-value pairs. Call it with different keyword arguments
def describe_pet(animal_type,pet_name):
    return (animal_type,pet_name)


# the code should be explained
def print_info(**kwargs):
    if kwargs:
        print ("\n---Information---")
        for key, value in kwargs.item():
            print(f"{key}: {value}")
    else:
        print("\nNo information provided.")

# how to call the function
# Example calls to the function
# print_info(name="Alice", age=30, city="New York")
# print_info(job="Engineer", salary=75000)
# print_info(country="USA", state="California", zip_code="90210")
# print_info()

global_var = 10

def modify_global_var():
    global_var = 20
    return global_var

def factorial_recursive(n):
    if n <0:
        return ("factorial is not defined for negative numbers")
    elif n ==0:
        return 1
    else:
        return n*factorial_recursive(n-1)


def multipy(a,b):
    return a*b

def number_check(check):
    if check > 0:
        return ("positive" )   
    elif check < 0:
        return ("Negative")
    else:
        return("Zero")

def even():
    count = 0
    number = 0
    while count < 10:
        print(number)
        number+=2
        count+=1

def multiply_list():
    numbers = [2,3,4,5,6]
    res = [i*i for i in numbers]
    return res

def max_without_inbuilt():
    numbers = [2,3,4,5,6]
    

def checkOddEven(x):
    if (x % 2 == 0):
        return True

    else:
        return False


def checkStatus(self,a,b,flag):
    if ((a>= 0 and b< 0)and flag is False):
        return True
    if((a < 0 and b< 0) and flag is False):
        return True
    if(a< 0 and b < 0 and flag is True):
        return True
    return False

    

            
# // Build a system to keeptrack of personal connections and their contact details.
# // The system should allow users to add new contact details
# // modify existing ones, remove contacts, and retrieve their 
# // contact's details without specifying how to store the contacts.


# // Develop a task scheduling platform that helps users organise their daily 
# //activities. Users should be able to add, edit, and delete tasks, set priority
# //and deadlines and receive reminders for upcoming tasks. Design the system to handle
# //recurring task



# Inheritance : allows properties and method to be inherited from a a parent class.

class Animal:
    def __init__self(self, name):
        self.name = name

    def speak(self):
        pass #used for a method that is to be overridden by a child class

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} barks!"  #overriding speak method in parent class
 

    


   



        
    


    