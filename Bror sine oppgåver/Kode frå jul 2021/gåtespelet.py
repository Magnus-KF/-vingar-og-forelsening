##Gåtespelet
kjør = True
nivå = 1
svar = ["Marihøne",'Blå','e']

print('Dette er gåtespelet.\n Klarer du alle dei tre gåtene får du heder, ære og kanskje ein klem')

def gåte1():
    global kjør
    global nivå
    global svar
    svar1 = input('Hvilken høne kan fly? \n')
    if svar1 == svar[0]:
        nivå = 2
    else:
        kjør = False

def gåte2():
    global kjør
    global nivå
    global svar
    svar2 = input('Jeg er tre bokstaver lang Jeg kan ses på himmelen\n Jeg er havet og jeg er sjøen\n Kan du gjette hva? \n')
    if svar2 == svar [1]:
        nivå = 3
    else:
        kjør = False

def gåte3():
    global kjør
    global nivå
    global svar
    svar3 = input('Hvordan begynner evigheten og hvordan slutter hver eneste time? \n')
    if svar3 == svar [2]:
        nivå = 4
    else:
        kjør = False        

while kjør:
    if nivå == 1:
        gåte1()
    elif nivå == 2:
        gåte2()

    else:
        gåte3()


print('Du får gruble vidare...')
