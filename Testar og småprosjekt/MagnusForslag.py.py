import random

bokstavar = ["a","b","c","d"]

class Bokstav:
    def __init__ (self, bokstav):
        self.bokstav = bokstav
    def printInfo (self):
        print(self.bokstav)
    def fao_bokstav (self):
        return self.bokstav

liste = []
checkList = set()

while len(liste) <= 3:
    liste.append(Bokstav(bokstavar[random.randint(0,3)]))
    if liste[-1].fao_bokstav() in checkList:
        print("Fins frå før")
        liste.pop(-1)
    checkList.add(liste[-1].fao_bokstav())


for objekt in liste:
   objekt.printInfo()

