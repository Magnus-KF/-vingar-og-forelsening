"""
test = [ 1,2,3,]

#print(int(test))

try:
    a = 20
    b = 10
    print(a/b)
except NameError:
    print("Something went wrong")
except TypeError:
    print("Not possible to add int and string")
except ZeroDivisionError as err:
    print(err)
except:
    print("Something else went wrong")
else:
    print("Oslomet")
finally:
    print("Welcome to MEK1300")

print("Hi")
"""
"""
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("a + b = ", a+b)
    print("a/b = ", a/b)
except ValueError:
"""
"""
while True:
    try:
        a = int(input("Enter a integer"))
        print("You entered", a)
    except ValueError:
        print("This is not an integer!")
    else:
        print("Thank you!")
        break
"""

"""
sum of all the numbers enter by the user
while ingoring any input that is not valid
exit the program when the user enters a blank line
"""
"""

total = 0
value = input("Enter a number")

while value != "":
    try:
        number = float(value)
        total = total + number
        print("The total is", total)
    except ValueError:
        print("That was not a number")
    except:
        print("Something went wrong")
    value = input("Enter a number: ")

print("The grand total is: ",total)
"""

"""
Assumes: L1 and L2 are lists of equal lenght of numbers
Returns: a list containg L1[i],/l2[i]
"""


def get_ratios(L1,L2):
    ratios = []
    for i in range(len(L1)):
        try:
            ratios.append(L1[i]/L2[i])
        except TypeError:
            print("Get_ratios called with bad arguments")
        except ZeroDivisionError:
            ratios.append("NaN")
        else:
            print("Success")
        finally:
            print("Executed no matter what!")
    return ratios


a = [1,4]
b = [2,4]


print(get_ratios(a,b))