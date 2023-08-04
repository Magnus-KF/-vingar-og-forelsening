# Dette er sekkspelet
#Sekkspelet handler om å kjøpe forskjellige sekkar, samle dei og putte ting i sekkane.

import time
import random
from re import A

class Sekk:
    def __init__ (self,merke,modell,volum,innhold):
        self.merke = merke
        self.modell = modell
        self.volum = volum
        self.innhold = innhold
    
    def printInfo(self):
        print("   Merke: {}  Modell: {} Størrelse: {}L  innhold: {}".format(self.merke,self.modell,self.volum,self.innhold))

#No kan eg lage sekkar, det neste steget er å lage ein sekkgenerator. Eg kan genererere random tal med random


merker = ["Belroy","Incase","The north face", "Osprey", "Camelback", "Bergans", "Ringnessekken!","Vintagebrand", "JustinBag","Nike","Tier","Adidas"]
modell = ["xps","ss69","light","Travelm8","sx80","BigBag","Fannypack","WIP","Adventure", "Lightweight","Color","Aero","Laser","Funtime","CandyCarry","BackBreaker"]




kortTur = ["stein","kvistar","jord","blader"]
mediumTur = ["hyssing","bær","sopp","maling"]
langTur = ["hasj","diamantar","pengar","pizza"]
turType = [kortTur,mediumTur,langTur]


def sekkMakar():
    rand1 = random.randint(0,len(merker)-1)
    rand2 = random.randint(0,len(modell)-1)
    rand3 = random.randint(2,26)
    
    nySekk = Sekk(merker[rand1],modell[rand2],rand3*5,"Ingenting")
    return nySekk

#Liste som held på sekkane
sekkar = []
#sekkar.append(sekkMakar())

kjør = 1
print("""
    
    --------------------------------
              Sekkspelet!
    --------------------------------
    Kode sekk for å kjøpe ny sekk.
    Kode tur for å gå tur
    Kode Samling for å sjå samlinga. 
    
    """)

def tur ():
    if turLengde == "kort":
        turmodus = int(1)
    elif turLengde == "medium":
        turmodus = int(2)
    elif turLengde == "lang":
        turmodus = int(3)
    else:
        pass
    randTall = random.randint(0,2)
    nyttInnhold = turType[turmodus][randTall]
    sekkar[valgtSekk-1].innhold = nyttInnhold
    print("Du fant: ",nyttInnhold)
    return


while kjør == 1:
    modus = input()
    if modus == "sekk":
        sekkar.append(sekkMakar())
        sekkar[-1].printInfo()

    elif modus == "tur":
        
        valgtSekk = int(input("Kva nummer har sekken du vil bruke?"))
        turLengde = input("vil du gå: kort(2 sekunder), medium(10 sekunder) eller lang(1 minutt) tur?")

        if turLengde == "kort":
            print("Du er på tur.")
            time.sleep(2)
            tur()

        elif turLengde == "medium":
            print("Du er på tur.")
            time.sleep(10)
            tur()

        elif turLengde == "lang":
            print("Du er på tur.")
            time.sleep(60)
            tur()
            
    elif modus == "samling":
         for index, sekk in enumerate(sekkar, start=1):
            print(index, end="")
            sekk.printInfo()
        

# very clever bro, fint opplegg. Om randint == altså er lik som ein er det sant, om ikkje er det false.
# ledig = random.randint(0,1) == 1
