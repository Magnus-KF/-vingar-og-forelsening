qo1 = ["Bergen","Oslo","Stavanger","Trondheim"]
qo2 = ["Euro","Pound","Krone","Deutche Mark"]
qo3 = ["Oslo ","Stavanger","Bergen","Deutche Mark"]
qo4 = ["27th May","17th May","17th April","27th April"]
qo5 = ["Red","White","Blue","Yellow"]
qo6 = ["1","2","3","4"]
qo7 = ["Uis","UiO","UNBT","NTNU"]
qo8 = ["96km","196km","296km","396km"]
qo9 = ["North","South","South-wesdt","South-east"]
qo10 = ["Oslo","Bergen","Stavanger","Tromsø"]

quiz = {
    "q1":{
        "question" : "What is the capital of norway?",
        "options" : qo1,
        "answer" : "Oslo"
    },
    "q2":{
        "question" : "What is the currency of Norway?",
        "options" : qo2,
        "answer" : "Krone"
    },
    "q3":{
        "question" : "What is the largest ciry in Norway?",
        "options" : qo3,
        "answer" : "Oslo"
    },
    "q4":{
        "question" : "When is constitution day (the national day) of Norway?",
        "options" : qo4,
        "answer" : "17th May"
    },
    "q5":{
        "question" : "What color is the background of the Norwegian flag?",
        "options" : qo5,
        "answer" : "Red"
    },
    "q6":{
        "question" : "How many countries does Norway border?",
        "options" : qo6,
        "answer" : "3"
    },
    "q7":{
        "question" : "What is the university in Trondheim?",
        "options" : qo7,
        "answer" : "NTNU"
    },
    "q8":{
        "question" : "How long is the border between Norway and Russia?",
        "options" : qo8,
        "answer" : "196km"
    },
    "q9":{
        "question" : "Where in Norway is Stavanger?",
        "options" : qo9,
        "answer" : "South-west"
    },
    "q10":{
        "question" : "From which Norwegian city did the world's famous composer Edvard Grieg come form?",
        "options" : qo10,
        "answer" : "Bergen"
    }                                                 
    }

correct = 0
wrong = 0
wrong_details = []

#Sjekker om svaret er rikig, om svaret ikkje er riktig får
def corrector(qnr, answer):   
    global quiz, correct, wrong, wrong_details
    ans = int(answer)
    if quiz[qnr]["answer"] == quiz[qnr]["options"][ans]:
        correct += 1
        return 
    else:
        wrong += 1
        wrong_details.append(quiz[qnr]["question"])
        wrong_details.append(quiz[qnr]["options"][ans])
        wrong_details.append(quiz[qnr]["answer"])
        return

#Konverterer inputen a,b,c,d til 0 ,1, 2 , 3
def converter(svar):
    if svar == "a":
        return 0
    elif svar == "b":
        return 1
    elif svar == "c":
        return 2
    elif svar == "d":
        return 3
    else:
        print("feil inputt")

# Sjekker om inputen er a,b,c eller d
def abccheck(svar):
    while True:
        if svar == "a" or svar == "b" or svar =="c" or svar == "d":
            b = converter(svar)
            return b
        else:
            svar=input("Skriv inn a, b, c eller d : ") 

#funksjon stiller spørmsål og tar inn svar
def questioner(qnr):
    global quiz, correct, wrong, wrong_details
    print()
    print(qnr)
    print(quiz[qnr]["question"])
    print()
    for i in range(0,4):
        print(chr(97+i)+": " + quiz[qnr]["options"][i])
    print()

    a = abccheck(input())
    corrector(qnr,a)

#inlogging
username_password = {"Password": "Python", "Username": "MEK1300"}
username = username_password.get("Username")
password = username_password.get("Password")

def login():
    print("")
    print("Quiz about Norway")
    print("")
    print("Please login to start the quiz.")
    print("_____________________________")
    print("")

    while True:
        if input("Enter username : ") != username:
            print("")
            print("The username is incorrect! please enter a valid username.")
        else:
            break

    while True:
        if input("Enter password : ") != password:
            print("")
            print("The Password you have entered is not correct. Please try again")
        else:
            break
    return

#Her logger me inn
login()

#Loop som kjøyrer gjennom quizen
for i in range(0,9):
    questioner(str("q"+str(i+1)))

print("You got", correct, "answers correct")
print("these are the ones you got wrong: ")
   


