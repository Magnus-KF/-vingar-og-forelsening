#Python
import random


liste = []
def leggTilTall(min, max):
    liste.append(random.randint(min+1,max-1))
    print("""
    Her er talet ditt:""",liste[-1],"""

    versegod.""")


print("""
---
velkommen til talgeneratoren.
---
Du får generert eit tal som ligg mellom eit lite og eit stort tal""")
leggTilTall(int(input("Skriv eit lite tal: ")),int(input("skriv eit stort tal: ")))


    
