#exercice5
"""
from cmath import sqrt
import math

def f (x):
    return g(x) + (h(x))**(1/2)

def g (x):
    return 4* h(x)

def h (x):
    return x*x + k(x)-1

def k (x):
    return 2* (x+1)

print(k(g(2)+h(2)))
"""

#oppg2
"""


def fact():  
    result = 1 
    num = int(input("Enter a number:"))
    if num >= 1:
        for amount in range(1,num+1):
            result = amount * result
    if num < 0:
        print("Invalid input")

    print(f"!{num} = {result}")


while True:
    fact()
"""

#oppg3
"""
def integerPower (x,y):
    return x**y

while True:
    x = int(input("x: "))
    y = int(input("y: "))
    print(integerPower(x,y))

"""

#oppg4
"""
def multiple (a,b):
    if b % a == 0:
        return "a multiple"
    else:
        return "not amultiple"

while True:
    a = int(input("a: "))
    b = int(input("b: "))
    print(f"{b} is {multiple(a,b)} of {a}")
"""
#oppg5

while True:
    select = int(input("""
    Enter 1 to convert from Celsius to Fahrenheit 
    Enter 2 to convert from Fahrenheit to Celsius 
    Select 1 or 2: """))

    if select == 1:
        celsius = int(input("Enter temperatrue in celsius: "))
        farenheit = celsius * 1.8 + 32
    elif select ==2:
        farenheit = int(input("Enter temerature in farheit: "))
        celsius = 2
    