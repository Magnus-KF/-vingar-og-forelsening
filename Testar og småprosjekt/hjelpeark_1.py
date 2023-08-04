
#To lister, ei med matvarer og ei som beksriver kor god matvara er.
from xml.etree.ElementPath import prepare_parent


liste = ["sjokolade","Kaffi","Banan","Syltetøy","kaffigrut"]
liste_2 = ["Betre","Best","Bestast"]
liste_som_lagrer_kor_gode_ting_er = []
count = 0

#Fusnkjon som definerer kor bra matvara er
def kor_god_er_den():
    global liste_som_lagrer_kor_gode_ting_er
    while True:
        print("kor god er:", liste[count])
        # Int() gjer at input() blir til ein integer, altså eit heiltal. Standard for input er string.
        x = int(input("trykk 0 for betre, trykk 1 for best eller trykk 2 for bestast"))

        liste_som_lagrer_kor_gode_ting_er.append[x]
        ## len(liste) er lik 5 i dette tilfellet, fordi lista "liste" har 5 element. len() er alltid eit tal.
        if count == len(liste):
            break
        
        

kor_god_er_den()
count = 0

while True:
    print(liste[count]+" : ", end="")
    print(liste_som_lagrer_kor_gode_ting_er[count])

    count += 1
    if count == 5:
        break

