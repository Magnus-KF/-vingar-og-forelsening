from random import randint
count =0
"""

f = open("demofil.txt", "r")

for x in f:
    print(x)

f.close()

f = open("demofil.txt", "a")

f.write( "\n Oh yes")

for x in f:
    print(x)

f.close()
"""

x = open("number.txt","a")

while True:
    x.write(str(randint(1,10))+"\n")
    count += 1
    if count == 5:
        break
x.close()

x = open("number.txt", "r")

for t in x:
    print(t)

x.close()