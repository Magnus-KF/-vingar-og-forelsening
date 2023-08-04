#Python
import random


liste = []
def leggTilTall(min, max):
    global liste
    liste.append(int(random.randint(min,max)))
    print("Her er talet ditt",liste[-1])


print("""
---
velkommen til talgeneratoren.
---
Du får generert eit tal som ligg mellom eit lite og eit stort tal""")
leggTilTall(int(input("Skriv eit lite tal")),int(input("skriv eit stort tal")))


    
