import json
from Aksjespel_utility import print_2

userDict =  {
    "username" : [],
    "password" : [],
    "Snumber": []
}
def new_user():
    name = input(print_2("Enter your name: "))
    pswrd = input(print_2("Enter password:"))
    snum = input(print_2("Enter social security number"))

    return userDict["username"].append(name), userDict["password"].append(pswrd),userDict["Snumber"].append(snum)

user1 = new_user()

x = json.dumps(user1)

def save():

    y = open("save.txt", "w")  
    y.write(x)
    y.close()


def open():
    y = open("save.txt", "r")
    content = y.read(0)
    return userDict()
save()
    







#Parses content so that it is usable in python
# json.loads()

# converts into json
# json.dumps()





