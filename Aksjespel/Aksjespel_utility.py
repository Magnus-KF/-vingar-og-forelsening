import time
import random

number_lines = ["Gimme that number!", "Let me see these numbers man:","Digits... please...","What's the number?"]
invalid_lines = ["You must be joking!","Thats not a number","Do you think im stupid?"," And 1 + 1 is 3, my ass...."]
def print_2(tekst,sleepTime=0.5):
    for i in tekst:
        print(i, end="", flush=True)
        time.sleep(random.randint(1,20)/250)
    time.sleep(sleepTime)
    print()

def Def_tall():
    t = input(print_2(random.choice(number_lines)))
    if t.isdigit():
        return int(t)
    else:
        print_2(random.choice(invalid_lines))
    
