#oppg 2
"""
n = int(input("Enter maximum square: "))
square = 0
count = 0
check = count
while square < n:
    print(square)
    count = count + 1
    square = count*count
    # check = (count+1)*(count+1)


"""
#oppg3
"""
c = 0
f = c * (9/5) +32
print("%10s %1s %10s" % ("celsius","|","Farenheit"))
print("%10s %1s %10s" % ("----------","+","---------"))

while c < 100:
    print("%-10.2f %1s %-80.2f" % (c,"|",f))
    c = c + 10
    f = c * (9/5) +32
"""
#oppg4
"""
first_name = input("Enter first name:")
last_name = input("Enter last name: ")

condition = 0
count = 0
total_score = 0

print("Enter your scores. When you are finished, enter -1")
while condition > -1:
    condition = int(input(":"))
    count = count+1
    total_score = total_score + condition

print(first_name," ",last_name,", your average score is: ", total_score/count,".")

"""
#oppg5
#A
"""
string = input("Enter any string")
count = 0

while len(string) > count:
    if string[count].isupper():
        print(string[count])

    count = count + 1

string = input("Enter any string")
count = 0
"""
#B
"""
while len(string) > count:

    print(string[count])

    count = count + 2
"""
#C
"""
string = input("Enter any string")
count = 0
vowels = ["a","e","u","i","o","y"]

while len(string) > count:
    if string[count].lower() in vowels:
        print("_", end="")
    else:
        print(string[count], end="")

    count = count + 1
"""
#D
"""
string = input("Enter anything: ")
print("Your string is ",len(string)," digits long.")
"""
#E
"""
string = input("Enter anything: ")
count = 0
vowels = ["a","e","u","i","o","y"]

print("The vowels are the the ", end="")
while len(string) > count:
    if string[count].lower() in vowels:
        print(count+1,",", end="")


    count = count + 1
print("places in the string.")
"""
#oppg5
"""
kjør = 1
count = 0
total = 0

print("When youre done, enter 666:")

while kjør == 1:
    value = float(input("Enter any floating point value: "))
    if count == 0:
        maximum = float(value)
        minimum = float(value)
       
    total = total + value
    count = count + 1

    maximum = max(value, maximum)
    minimum = min(value, minimum)

    if value == 666:
        kjør = 0

print("Avreage value is:", total/count)
print("Smallest value is:",minimum)
print("Biggest value is:", maximum)
"""
#oppg7
"""
string = input("Enter you name: ")
count = 0

while count < len(string):
    print(string[0+count])

    count = count + 1
"""
#oppg8

string = input("Enter you name: ")
count = len(string)-1 

while count > -1:

    print(string[count], end="")
    count = count -1



