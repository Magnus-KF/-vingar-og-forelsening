#python
from distutils.log import fatal
import math
#Øvingar
#oppg1
""""
x = 2.5
y = -1.5
m = 18
n = 4

#a
print(x + n * y - (x + n) * y)
#b
print(m // n + m % n)
#c
print(1-(1-(1-(1-(1-n)))))
#d
print(math.sqrt(math.sqrt(n)))
"""
#oppg2
""""
n = 17
m = 18
#a
print(n//10+n%10)
#B
print(n%2+m%2)
#c
print((m+n)//2)
#d
print((m+n)//2.0)
#e
print(0.5*(m+n))
#f
print(round(0.5*(m+n)))
"""
#oppg3
""""
s = "Hello"
t = "World"

#a
print(len(s)+len(t))
#b
print(s[1]+s[2])
#c
print(s[len(s)//2])
#d
print(s+t)
#f1

print(s*2)
"""
#oppg4
""""
#print("%-15s %10d" % ("Enter number 1:",input()))
a = int(input("%-17s" % ("Enter number 1:")))
b = int(input("%-17s" % ("Enter number 2:")))
print()
print("%-16s %-10d" % ("Sum =",a+b))
print("%-16s %-10d" % ("Differance =",a-b))
print("%-16s %-10d" % ("Product =",a*b))
print("%-16s %-10d" % ("Average =",a+b/2))
print("%-16s %-10d" % ("Distance =",abs(a+b/2)))
print("%-16s %-10d" % ("Maximum =",max(a,b)))
print("%-16s %-10d" % ("Minimum =",min(a,b)))
"""
#oppg6
""""
print("This program calculates the parimiter and Area of rectangles.")
side1 = int(input("Enter lenght of side 1:"))
side2 = int(input("Enter lenght of side 2:"))

areale = side1 * side2
omkrets = side1*2 + side2*2

print("areale: ",areale )
print("Omkrets: ", omkrets)
"""
#oppg7
""""
namn = input("input any name:  ")
lenght = len(namn)

print("{}...{}".format(namn[0:2],namn[lenght-2:lenght]))
"""
#oppg8
"""""
ot = input("skriv inn eit femsifra tal: ")

o0 = ot[0]
o1 = ot[1]
o2 = ot[2]
o3 = ot[3]
o4 = ot[4]

print(o0,o1,o3,o4)

#Done
"""