#Velkommen til aksjespelet
# Det er eit spel som skal la deg kunna kjøpe og selje forskjellige aksjer. 
# Det skal også vere ein funskjon som lar dagen gå slika t det blir endringar i verdien på aksjene.
# Det hadde også vore spennand eå lage ein funskjon som kjøyrte i bakgrunne som ga deg info om kva som skjer i bakgrunnen.

from random import randint , choice
import time
from traceback import print_list
from Aksje import Aksje ,aksjeLagar
from Aksjespel_utility import print_2,Def_tall
from InquirerPy import inquirer
from Aksjespel_login import username


             
pengar = randint(90000,124000)
aksje_list = []
aksjeRisiko = [0.5,1,3]
namn_liste = []
kjøp_liste = []
username = "Ola"
kjøpe_line = ["Pleaseure doing buisniss with you.","Good choice dude!","Good luck with those...","Goodbye","Bye "+username,]


#Loop som lagar 10 forsjellige aksjar
while len(aksje_list) < 10:
    
    aksje_list.append(aksjeLagar())

#funskjon som printer printer alle aksjane
def liste_printar(liste):
    print("%3s %-30s %7s %7s %7s" % (" ","Name:","Price:","Change:","You own:"))
    for index , aksje in enumerate(liste, start = 1):
        time.sleep(0.1)
        print("{:3} ".format(index), end="")
        aksje.printInfo()

#Function that temporarely makes a list consisting of stocks youve invested in.
def what_you_own():
    own_list = []
    for x in aksje_list:
        if x.antall > 0:
            own_list.append(x.namn)
    return own_list


#Function that makes transactions for buying stocks
def kjøpar(aksjenummer,mengde):
    global pengar
    aksje_list[aksjenummer].antall = mengde

    pengar = pengar - aksje_list[aksjenummer].verdi*mengde
    return pengar , aksje_list[aksjenummer].antall

# Kjøper aksjer
def main_buy():
    print_2("Wich stock do you wish to buy?")
    nummer = namn_liste.index(inquirer.select(message="---------------------", choices=namn_liste).execute())
    print_2("How many stocks do you want "+ username +" ?")
    antall = Def_tall()  
    kjøpar(nummer,antall)
    print_2("You bought "+str(antall)+" "+aksje_list[nummer].namn +" "+choice(kjøpe_line))

#funkjson som seljer aksjer
def selje(aksjenummer,mengde):
    global pengar
    if mengde <= aksje_list[aksjenummer].antall:
        aksje_list[aksjenummer].antall -= mengde
        pengar = pengar - aksje_list[aksjenummer].verdi*mengde
        return pengar , aksje_list[aksjenummer].antall
    else:
        print_2("You dont own the appropriate amount of "+ aksje_list[aksjenummer].namn )


# Main function for selling stocks
def main_sell():
    own = what_you_own()
    print_2("Wich stock do you wish to Sell?")
    nummer = own.index(inquirer.select(message="---------------------", choices=own).execute())
    for x in aksje_list:
        if x.namn == own[nummer]:
            listenummer = aksje_list.index(x)
            break

    print_2("You own "+str( aksje_list[listenummer].antall)+" "+str( aksje_list[listenummer].namn) )
    print_2("How many are you getting rid off?")
    antall = Def_tall()
    selje(listenummer,antall)


# Simply prints your balance in a smooth and sexy way
def balance():
    print_2("Your balance is "+str(pengar)+"$")

#Function that refreshes the pricing, might need some tweeking.
def ny_dag():
    global aksje_list
    for i in range(len(aksje_list)): 
        endring = randint(-10,10)
        aksje_list[i].verdi = aksje_list[i].verdi + (aksje_list[1].verdi*((endring/100) * aksje_list[i].risiko))
        aksje_list[i].endring = endring*aksje_list[i].risiko

#loop som lager ei liste med kun namna til aksjene
for i in aksje_list:
    namn_liste.append(i.namn)

##her kjøyrer heile spelet.
ny_dag()

def tutorial():
    global aksje_list
#    print_2("Welcome "+username)
  #  print_2("Here is todays stock market")
    liste_printar(aksje_list)
    time.sleep(5)
 #   print_2("You dont own any stocks "+ username)
    print_2("However....")
    balance()
    print_2("Looks like its time you buy some stocks.",2)

    main_buy()
    liste_printar(aksje_list)
    print_2("Now thats more like it!")
    print_2("Youre a natural!")
    print_2("Ill quickly show you how to sell stocks, then you should be set.")
    main_sell()


tutorial()



