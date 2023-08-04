#Oppg1
"""
number = int(input("Enter this any integer:"))
odd = 1
while number > odd:
    print(odd)
    odd = odd + 2
"""
#oppg2
"""
stars = int(input("Enter the number of stars you want:"))


while stars > 0:
    print("*" * stars)
    stars = stars - 1
"""
#oppg3
"""
number = int(input("Enter your factorial number:"))
factorial = number
save = number
if number == 0:
    factorial = 1
while number > 1:
    number = number - 1
    factorial = factorial * number

print("Factorial !",save," =",factorial)
"""
#oppg4
"""
class Employee:
    def __init__ (self,sales,salery):
        self.sales = sales
        self.salery = salery
    def print_info (self):
        print(self.sales,self.salery)
count = 0
employers = []
print("Enter your sales: ")
while count < 5:
    sales = int(input(":"))
    if sales < 20000:
        salery = 400 + sales*0.02
        employers.append(Employee(sales,salery))
    elif sales < 25000:
        salery = 500 + sales*0.05
        employers.append(Employee(sales,salery))        
    elif sales < 30000:
        salery = 400 + sales*0.1
        employers.append(Employee(sales,salery))
    if sales >= 30000:
        salery = 575 + sales*0.2
        employers.append(Employee(sales,salery))
    count = count + 1
print("Sales  salery")
for index, eplo in enumerate(employers, start=1):
    print(index," ", end="")
    eplo.print_info()
"""
