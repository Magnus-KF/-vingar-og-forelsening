# Dette er klassen Akjse, den har variablane namn, verdi, risiko, ending og antall.

from random import randint, choice 


#liste med aksjenamn
aksjeNamn = ["DNB","SlatanWEAR","WhitePowederCompany","Cashflow","IBM",
"Lenovo","MyLittlePony","Disney+","Mercedes","Mclarren","HBO","Apple","Snøfnugg","Wizards of the coast","AppleTV"
]
class Aksje:
    def __init__ (self,namn,verdi,risiko,endring,antall):
        self.namn = namn
        self.verdi = verdi
        self.risiko = risiko
        self.endring = endring
        self.antall = antall

    def printInfo(self):
        print("%-30s %7d %7s %7d" % (self.namn,self.verdi,str(self.endring)+"%",self.antall))

#Dette er aksjelagaren. Den gir aksjen ein verdi og eit namn som er 
def aksjeLagar():
    global aksjeNamn
    randVerdi = randint(10,200)
    randNameIndex = randint(0,len(aksjeNamn)-1)
    randRisiko = randint(0,2)
    randNamn = aksjeNamn.pop(randNameIndex)
    nyAksje = Aksje(randNamn,randVerdi,randRisiko,0,0)

    return nyAksje
