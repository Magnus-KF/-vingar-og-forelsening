import random

game = "yes"

def final():
    print("The number was:", solution,"!")
    print()
    while True:
        game = input("do you want to play again (yes / no) :")
        if game == "yes" or game == "no":
            return game
            break

        else:
            print("Enter a valid input")


def valid_input():
     while True:
        n = input("Enter a number: ")
        if n.isdigit():
            n = int(n)
            return n
            break
        else:
            print("Enter a valid value!")



def check(answer):
        global count
        if answer == solution:
            print("You win!")
            count = 5
            return count
        elif answer > solution:
            print("Your number is to big!")
        elif answer < solution:
            print("Your number is to small!")
        else:
            print("Input a valid answer")
        
        print("You have",4-count,"guesses left")
        
        print()
        return count


print("""
welcome to the number guessing game!
you have 5 guesses!
good luck!""")

while game == "yes":
    solution = random.randint(0,1000)
    count = 0
    while count < 5:
        check(valid_input())
        count += 1
    game = final()
    
print("Goodbye!")