def check_if_even(number):
    if number % 2 == 0:
        print (f"{number} is even")

def check_if_even_or_odd(number):
    if number % 2 == 0:
        print (f" {number}is even")
    else:
        print  (f" {number}is odd")

def check_divisibility(n):
    for x in range(1,n+1):
        if x%2 == 0:
            print(f"{x} is divisible by 2")
        elif x %3 == 0:
            print(f"{x} is divisible by 3")
        elif x% 5 ==0:
            print(f"{x} is divisible by 5")
        elif x%7 == 0:
            print(f"{x} is divisible by 7")
        else:
            print(f"{x} is not divible by 2,3,5,7")

def fizz_buzz(number):
    for i in range(1, number+1):
        if i%2 == 0:
            print (f"{i} fizz")
        elif i%3 == 0:
            print(f"{i} buzz")
        elif i %5== 0:
            print (f"{i} fizzbuzz")
        else:
            print({i}) 
# we can use break to stop the while loop even if the set condition is true
# To interrupt infinity ctrl+C
def countdown (start):
    while start >= 0:
        print (f"countdown at {start}")
        start -=1   

def countdown_with_break(start,stop):
    while start >= 0:
        print (f"countdown at {start}")
        if start == stop:
            print(f"stopping at {stop}")
            break
        start -=1 
        
# continue skips a certain iteration to the next iteration
def countdown_with_odd_numbers(start):
    while start >= 0:
        if start % 2== 0:
            start -=1
            continue
        print (f"countdown at {start}")
        start -=1

# use a while loop to create a function to print all the even numbers between 0 &100
def even_numbers():
    even = 0
    while even <= 100:
        if even % 2 != 0:
            even +=1
            continue
        print(even)
        even +=1
        
    






        