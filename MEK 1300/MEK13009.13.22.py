#Forelesning 14.9.22

from cmath import sqrt
import math

#Eks 1
"""
while True:
    def cube_volume(length):
        volume = length**3
        return volume

    number = int(input("Enter a cube side lenght: "))

    result = cube_volume(number)

    print(result)
"""
#Eks 2
"""
while True:
    def welcome(name):
        print("Hi",name)
    
    name = input("Enter your name:")
    welcome(name)
"""
#Eks 3
"""
def main():
    result = cube_volume(10)
    print("volume=",result)

def cube_volume(length):
    volume = length**3
    return volume

main()
"""
#Eks4
"""
def pyramid_volume(length,height):
    volume = length**2*height*(1/3)
    print("The volume of the pyramid is:", volume)

while True:

    height = float(input("ENter height:"))
    length = float(input("Enter the pyramid length: "))
    pyramid_volume(length,height)
"""
#Eks5
"""
def minimum_two(x,y):
    if x < y:
        return x
    elif x > y:
        return y
    else:
        return False
    
a = int(input("Enter x:"))
b = int(input("Enter y:"))

minimum = minimum_two(a,b)

if not minimum:
    print("The numbers are equal")
else:
    print("This is the lesser number is:", minimum)
"""
#Eks 6

## distance between two points: (x_1,y_1), (x_2,y_2)
"""
def main():
    x1 = int(input("Enter x_1:"))
    y1 = int(input("Enter y_1:"))
    x2 = int(input("Enter x_2:"))
    y2 = int(input("Enter y_2:"))

    dis = float(distance(x1,y1,x2,y2))

    print(dis)

def distance(x_1,y_1,x_2,y_2):
    x_dif = x_2 - x_1
    y_dif = y_2 - y_1
    length = ((x_dif**2)+(y_dif**2))**0.5
    return length

main()
"""
#Eks 7

def main():
    sentence = input("Gi meg ein setning:")
    count = count_words(sentence)
    print(f"{sentence} har {count} ord.")


def count_words(string):
    count = 1
    for char in string:
        if char in " ":
            count = count + 1
    return count

main()