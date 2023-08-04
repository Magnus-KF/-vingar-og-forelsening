import math

#oppg1
""""
print("Converter:   kilograms ---> pounds")
amount = float(input("Enter amount in kg: "))
#print("%-4i %-4s %-3f %-4s" % ( amount,"kilograms is",(amount*2.2),"pounds"))
print("{}{}{}{}".format ( amount,"kilograms is",(amount*2.2),"pounds"))
"""
#oppg2
""""
radius = int(input("Enter radius: "))

area = round(math.pi*radius**2, 3)
circumference = round(math.pi*radius*2, 3)
volume = round((4/3)*math.pi*radius**3, 3)
surfaceArea = round(4*math.pi*radius**2, 3)

print("Area of circle: {}, circumference: {}, volume of sphere: {}, surface area of sphere: {}".format(area,circumference,volume,surfaceArea))
"""
#oppg3
""""
username = input("Enter your username: ")

password = input("Enter your password: ")
passwordLength = len(password)
print("Hi {}. Your password is {} is {} characters long.".format(username,("*"*passwordLength),passwordLength))
"""
#oppg4

gasolineInTank = int(input("How many liters of gasoline is in the tank?: "))
efficiency = float(input("How many liters of fuel does the engine spend per kilomter?: "))
gasolinePrice = int(input("How much does is a litre of gasoline today? in kr please:"))

pricePer100km = int((efficiency*100)*gasolinePrice)
rangeWithCurrentFuel = (efficiency*gasolineInTank)

print("With your current fuel you can drive {} kilometers.".format(rangeWithCurrentFuel))
print("The cost of driving 100 kilometers is {}kr.".format(pricePer100km))