# Øving på class i python

class Sekk:
    def __init__ (self, modell, merke, volum, beltestropp):
       
        self.modell = modell
        self.merke = merke
        self.volum = volum
        self.beltestropp = beltestropp

    def printInfo(self):
        print("Modell:{}   Merke:{}   Volum:{}   Beltestropp:{}  , - ".format(self.modell,self.merke,self.volum,self.beltestropp))

class SekkSamanliknar:
    def __init__(self,sekkSamling):
       self.sekkSamling = sekkSamling

    def sekkPrintar(self):
        for Sekk in self.sekkSamling:
            Sekk.printInfo()

bergans = Sekk("Xp3","Bergans",50,"ja")
kløvertopp = Sekk("xxx5","Kløvertopp",90,"nei")

samlinga = SekkSamanliknar([bergans,kløvertopp])
samlinga.sekkPrintar()
