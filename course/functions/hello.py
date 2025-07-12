def hello():
    print("Hello Akirachix")

def say_hello(name):
    print(f"Hello {name}")

def greet(name,age):
    year = 2025 - age
    print (f"Hello my name is {name} born in {year}")

def greet_student(name,age,school):
    year = 2025 - age
    print(f"Hello {name}, born in{year}, welcome to {school}")

def my_country(name = "Uganda"):
    print (f"I love my country {name}")


#fArbitrary keywod
def welcome_student(**kwargs):
    print(kwargs)

#function that accepts any no. of positional argument or any no. of keyword argument
def exam_result(*args, **kwargs):
    print(args)
    print(kwargs)
   

def exams_results(names, room, *scores):
    total_scores = sum(scores)
    print(f"Hello {names} of {room}, your total score is {total_scores}")


