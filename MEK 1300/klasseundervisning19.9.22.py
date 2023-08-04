from calendar import c

"""
a = int(input("Enter a"))
b = int(input("Enter b:"))


def main():
    print("Before swap:")
    print("a =", a)
    print("b =", b)

    swap()

    print("After swap")
    print("a =", a)
    print("print")



def swap():
    global a ,b 
    c = a
    a = b
    b = c
    


main()
"""
#eks2
"""
def middle(string):
    pos = len(string) // 2

    if (len(string) % 2) == 1:
        return string[pos]
    else:
        return string[pos-1]+string[pos]

string = input("Enter a string: ")

print(middle(string))
"""


def main():
    choice = menu()
    while choice != 5:
        if choice > 1 and choice < 5:
            print("Invalid choice!")
        else:
            num1 = int(input("Enter 1: "))
            num2 = int(input("Enter 2: "))

            if choice == 1:
                result = add(num1,num2)
                print(f"{num1} + {num2} = {result}")
            elif choice ==2:
                result = subtraction(num1,num2)
                print(f"{num1} - {num2} = {result}")
            elif choice ==3:
                result = multiplication(num1,num2)
                print(f"{num1} * {num2} = {result}")
            else:
                result = add(num1,num2)
                if result == False:
                    print("Zero division error!")
                else:
                    print(f"{num1} + {num2} = {result}")
    choice = menu()       

def add(num1,num2):
    return num1 + num2

def subtraction(num1,num2):
    return num1 - num2

def multiplication(num1,num2):
    return num1 * num2

def division(num1,num2):
    if num2 == 0:
        return False
    else:
        return num1 / num2

def menu():
    print("""
    1: addision
    2: Subtraction
    3: multiplication
    4: Division
    5: Quit""")
    choice = int(input("Enter the operation you waht  to perform"))
    return choice

main()

