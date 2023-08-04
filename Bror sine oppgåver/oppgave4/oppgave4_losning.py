
class Person:
    def __init__(self, navn, penger, timeslønn):
        self.navn = navn
        self.penger = penger
        self.timeslønn = timeslønn
    
    def jobb(self, timer):
        self.penger = self.penger + self.timeslønn * timer

kåre = Person("kåre", 10000, 200)
peder = Person("peder", 2000000, 500)

kåre.jobb(10)
peder.jobb(10)