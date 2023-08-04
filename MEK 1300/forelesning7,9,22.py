"""
total = 0
count = 0

salary = float(input("Enter a salary:" ))

while salary >= 0:
    total = total + salary
    count = count + 1
    salary = float(input("Enter a salary:" ))


if count > 0:
    average = total/count
    print("Average salarary:", average)
else:
    print("No data entered")
"""

smallest = int(input("Enter a number:"))
my_input = input("Enter a number: ")

while my_input != "":
    value = int(my_input)
    if value < smallest:
        smallest = value

    my_input = input("Enter a number: ")

print(smallest)