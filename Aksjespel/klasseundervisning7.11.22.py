"""class Person:
    def __init__ (self,name, age):
        self.name = name
        self.age = age
    def myfinc(self):
        print(f"My name is {self.name}. I am {self.age} years old.")

    

p1 = Person("jhon", 24)

p1.myfinc()
"""
"""
class Animal:
    def __init__(self, age ):
        self.age = age
        self.name = ""
    def get_age (self):
        return self.age
    def set_name (self, name):
        self.name = name
    def get_name(self):
        return self.name

    def set_age (self, newage):
        self.age = newage
    def __str__ (self):
        return "Animal: " + self.name + "=-> " + str(self.age)


print("animal class test")


a1 = Animal(22)

print(a1)
"""
"""
class Counter:
    def __init__(self):
        self.value = 0

    def reset(self):
        self.value = 0
    
    def click(self):
        self.value = self.value + 1

    def get_value(self):
        return self.value

tally = Counter()

tally.click()
tally.click()
tally.click()
tally.click()

print(tally.get_value())
"""
"""
class CashRegister:
    def __init__ (self):
        self.itemCount = 0
        self.totalPrice = totalPrice
    def add_item(self,price):
        self.itemCount = self. itemCount + 1
        self.totalPrice = self.totalPrice + price 
    def get_count(self):
        return self.itemCount
    def get_total(self):
        return self.totalPrice
    
cr1 = CashRegister()

print(cr1.get_count())
print(cr1.get_total())

cr1.add_item(200)
cr1.add_item(40)
cr1.add_item(213300)
cr1.add_item(2200)


print(cr1.get_count())
print(cr1.get_total())
"""
"""

class vehicle:
    def __init(self,brand,model,type_of_car):
        self.brand = brand
        self.model = model
        self.type_of_car = type_of_car
        self.gas_tank_size = 14
        self.fuel_level = 0
    def fuel_up(self):
        self.fuel_level = gas_tank_size
        print("Gas tank is now full.")
    def drive(self):
        print(f"the {self.model} is now driving.")
    
    def fuel_up(self,new_level):
        if new_level <= self.gas_tank_size:
            self.fuel_level = new_level
    def get_gas(self,amount):
        if self.fuel_level + amount <= self.gas_tank_size:
            self.fuel_level = self.fuel_level.g
"""