#oppg1

#a) 8
"""
for i in range(1,10,2):

     print(i)
"""
#oppg2
#a
"""
string = input("Enter a string:")

for letter in string:
    if letter == letter.upper():
        print(letter, end="")
"""
#b
"""
string = input("Enter a string:")

count = 0
for letter in string:

    if count % 2 == 0:
        print(letter)    
    count = count + 1
"""
#c
"""
string = input("Enter a string:")

for letter in string:
    if letter in "aeiou":
        print("_", end="")
    else:
        print(letter, end="")
"""
#d
"""
string = input("ENter any string with digits:")

count = 0

for letter in string:
    if letter in "0123456789":
        count = count + 1



print("The string has",count,"digits.")
"""
#e
"""
string = input("Enter any stirng")

count = 0

for letter in string:
    if letter.lower() in "aeiouy":
        count = count + 1

print("The string contains", count, "vowel(s).")
"""
#3 
"""
name = input("Enter your name:")

for letter in name:
    print(letter)
"""
#4
"""
name = input("Enter yout name: ")
count = -1
for letter in name:
   print(name[count], end="")
   count = count -1
"""
#5
"""
for y in range(6):
    for x in range(y):
        print("*", end="")
    print("")
"""
#6



