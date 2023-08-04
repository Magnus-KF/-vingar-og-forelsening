#in class oppgaver

#oppg1
"""
run = 1
while run : 
    vowel = ["a","e","i","o"]

    letter = input("Enter a letter: ")

    if letter in vowel:
        print("your letter is a vowel")
    elif letter == "y":
        print("your letter is somtimes a vowel and somtimes a consonant.")
    else:
        print("Your letter is a consonant")"
"""
#oppg2
"""
shapes = ["Triangle","Square","Pentagon","Hexagon","Heptagon","Octagon","Nanogon","Decagon"]

kjør = 1

while kjør:
    number = int(input("Enter the number of sides "))
    if number >=3 and number <=10:
        print("your shape is a ",shapes[number-3])
    else:
        print("please enter a integer between 3 and 10.")
"""
#oppg3
"""
l28 =["28 or 29","February"]
l29 =[""]
l30 =[30,"April","June","September","November"]
l31 =[31,"January","March","May","July","August","October","December"]

kjør = 1

while kjør:
    month = input("Enter the name of a month: ").capitalize()
    if month in l31:
        print(month,"is", l31[0], "days long.")
    elif month in l30:
        print(month,"is", l30[0], "days long.")
    elif month in l28:
        print(month,"is", l28[0], "days long.")
    else:
        print("Invalid month name.")
"""
#oppg4
"""
kjør =1

while kjør:
    
    side1 = int(input("Enter lenght of side 1:"))
    side2 = int(input("Enter lenght of side 2:"))
    side3 = int(input("Enter lenght of side 3:"))

    if side1 == side2 and side1 == side3:
        print("your tiangle is equalateral")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("your tiangle is likebeint")
    elif side1 != side2 and side1 != side3 and side2 != side3:
        print("your triangle scelene")
"""
#oppg5
"""
month = input("Enter month:").capitalize()
date = int(input("Enter date:"))

months = ["January","February","March","April","May","June","Jule","August","September","October","November","December"]

if month == months[0 or 1]:
    print("Winter")
elif month == months[2] and date < 20:
    print("Winter")
elif month == months[2] and date > 21:
    print("Winter")
elif month == months[3 or 4]:
    print("Spring")
elif month == months[5] and date < 21:
    print("Spring")
"""
#opgg5

animal = ["Dragon","Snake","Horse","Sheep","Monkey","Rooster","Dog","Dog","Pig","Rat","Ox","Tiger","Hare"]
kjør = 1
while kjør == 1:
    year = int(input("Enter year number:"))    
    yearanimal = animal[year%12-8]
    print("Its the year of the ",yearanimal)

#oppg6
"""

incre = 2400

while True:
    rating = float(input("Enter your rating:"))
    if rating == 0.0:
        print("Your performance is unacceptable, youre fired!")
    elif rating == 0.4:
        print("Your performance is acceptable, your raise is:",incre*rating," dollars")
    elif rating > 0.4 and rating <= 1:
        print("Your performance is amazing! your raise is:",rating*incre, " dollars")
    elif rating < 0.4 or rating > 1:
        print("This is not your rating")
"""