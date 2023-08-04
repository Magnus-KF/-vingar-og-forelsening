from random import randint
game = "yes"

def final():
    if count == 5:
        print("Sorry!! You did not manage to guess the number. You have reached the guessing limit.")
        print("The correct number was:", solution,"!")
        print()

        while True:
            game = input("do you want to play again (yes / no) :")
            if game == "yes" or game == "no":
                return game
                break
            else:
                print("Enter a valid input")
    else:
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
            print("Congratulation! You guessed the number in", count + 1, "attempt(s)")
            return answer
        elif answer > solution:
            print("Your number is to big!")
        elif answer < solution:
            print("Your number is to small!")
        else:
            print("Input a valid answer")

        print("You have",4-count,"guesses left")
        print()
print("""

welcome to the number guessing game!
you have 5 guesses!
good luck!""")

while game == "yes":

    solution = randint(0,1000)
    print(solution)
    count = 0
    while count < 5:
        n = check(valid_input())
        if n == solution:
            break
        count += 1
    game = final()
print("Goodbye!")