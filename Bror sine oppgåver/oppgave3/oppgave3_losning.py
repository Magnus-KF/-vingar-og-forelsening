
class Bil:
    def __init__(self, merke, modell, årsmodell, pris):
        self.merke = merke
        self.modell = modell
        self.årsmodell = årsmodell
        self.pris = pris
    
    def printInfo(self):
        print("{} {}, {}: {},-".format(self.merke, self.modell, self.årsmodell, self.pris))

class BilButikk:
    def __init__(self, biler):
        self.biler = biler
    
    def printBilInfo(self):
        for bil in self.biler:
            bil.printInfo()

ford = Bil("Ford", "Fiesta", 1987, 25000)
bmw = Bil("BMW", "i4", 2022, 450000)
toyota = Bil("Toyota", "Avensis Verso", 2013, 150000)

tyssedalAuto = BilButikk([ford, bmw, toyota])
tyssedalAuto.printBilInfo()
