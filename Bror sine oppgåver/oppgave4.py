# Lag ein ny klasse Person
# Person har tre variablar: navn, penger og timeslønn
# Person har ein funksjon jobb()
# jobb tar inn parameteret timar, penger øker etter timeslønn og timer

class Person:
    def __init__(self,namn,penger,timelønn):
        self.namn = namn
        self.penger = penger
        self.timelønn = timelønn
    
    def jobb(self,timar):
        self.penger += (self.timelønn*timar)
        return self.penger


klaus = Person("Klaus",0,180)
print(klaus.penger)
klaus.jobb(2)
print(klaus.penger)
klaus.jobb(4)
print(klaus.penger)
