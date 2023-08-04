
"""
# åpner en liste og formaterer innholdet og lagrer det i et nytt textdokument
input_file_name = input("Enter file name: ")
output_file_name = input("Enter file name: ")

input_file = open(input_file_name, "r")
output_file = open(output_file_name, "w")

total = 0
for line in input_file:
    parts = line.split(":")
    item = parts[0]
    price = float(parts[1])
    
    total = total + price
    
    output_file.write("%-20s%10.2f\n" % (item,price))

output_file.write("-" * 31 + "\n")

output_file.write("%-20s%10.2f\n" % ("Total", total))

input_file.close()
output_file.close()
"""

# les en fil som inneholder en liste med ord
# programmet skal ta to av ordene og produsere et passord mellom 8 og 12.
# hvert ord skal være minst 3 og på det meste 7 bokstaver langt
# gjør om hvert ord til store bokstaver og vis passordet
# vis passordet

from random import randint

words = []

input_file = open("input1.txt", "r")
for line in input_file:
    line = line.rstrip("\n")
    
    # behold ordene som er mellom 3 og 7 bokstaver lange
    
    if len(line) >=3 and len(line) <= 7:
        # legg dem til i listen words
        words.append(line)
        

input_file.close()

first = words[randint(0,len(words)-1)]

first = first.capitalize()

password = first

while len(password) <8 or len(password) >12:
    second = words[randint(0, len(words)-1)]
    second = second.capitalize()
    password = first+second
    
print("Your password is ----------------->", password)
































