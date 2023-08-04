from hashlib import new
from unicodedata import name
from Aksjespel_utility import print_2
import os
from InquirerPy import inquirer
import getpass

def login_main():
    
    newUser = inquirer.select(
        message= ""
        ,choices = ["Login","Create new user"]
    ).execute()

    if newUser == "Login":
        login()
    else:
        pass    

def login():
    while True:
        try:
            
            username = inquirer.text(
                message = print_2("Username: ")
                ).execute()
                
            file = open("save.txt", "r")
            content = file.read()
            print(content)
         
        except:
            print_2("you fucked up kid, go again.")
        else:
            break


"""
def login():
    while True:
        try:    
            username = inquirer.text(
                message = print_2("Username: ")
                ).execute()
            userpath = username+".txt"
            os.path.exists(userpath) == True
        except:
            print_2("you fucked up kid, go again.")
        else:
            usr = open(userpath, "r")
            break
    #while True:
"""

        
            


login_main()


"""
print_2("Enter username: ")
    username = input()
    print_2("Enter password: ")
    password = getpass.getpass("")
    print("*"*len(password))



name = inquirer.text(message="What's your name:").execute()
fav_lang = inquirer.select(
    message="What's your favourite programming language:",
    choices=["Go", "Python", "Rust", "JavaScript"],
).execute()
confirm = inquirer.confirm(message="Confirm?").execute()
"""