# Felleskostnadsreknar.
#Totalt vil me ikkje betale meir en me gjer i dag. tora 8500 og hans olav 5000
# Totalt 13500

hans_olav = 5000
tora = 8500
rente = 5.0
år = 30

total_månad = hans_olav + tora
utregna = (1+(rente/100))**(1/12)-1
felles_kost = int(input("Skriv inn felleskostnadane: "))

while 1 :
    nedbetaling = total_månad - felles_kost
    lån = nedbetaling * ((1-(1+utregna)**(-år*12))/utregna)
    print("Du får: ", round(lån+2000000,0),"til saman")
    felles_kost = int(input("Skriv inn felleskostnadane: "))



