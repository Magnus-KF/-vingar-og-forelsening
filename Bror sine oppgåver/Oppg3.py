# Lag ein ny klasse BilButikk
# BilButikk har kun ein variabel på seg: biler
# biler er ei liste med objekter av Bil-klassen
# BilButikk har ein funksjon printBilInfo
# Den går gjennom kvar Bil i biler og kjører printInfo på den bilen
# Hint: På den siste delen må du bruke ein for-loop

# Tre bilar du kan bruke:



class Bil:
    def __init__(self,merke,modell,årgang,pris):
        self.merke = merke
        self.modell = modell
        self.årgang = årgang
        self.pris = pris

    def printInfo(self):
        print("%-10s %-20s %-10s %-10s" % (self.merke,self.modell,self.årgang,self.pris))


ford = Bil("Ford", "Fiesta", 1987, 25000)
bmw = Bil("BMW", "i4", 2022, 450000)
toyota = Bil("Toyota", "Avensis Verso", 2013, 150000)
 
#minFord.printInfo()

class BilButikk:
    def __init__ (self,biler):
        self.biler = biler

    def printBilInfo(self):
        print("%-10s %-20s %-10s %-10s" % ("Merke:","Modell:","Årgang:","Pris:"))
        for Bil in self.biler:
                Bil.printInfo()

teslaAuto = BilButikk([toyota,ford,bmw])
teslaAuto.printBilInfo()

