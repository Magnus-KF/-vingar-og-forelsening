import json
from lists import windowCreator, file_check, load_recipes, save_recipes
from div import transform_text_to_list, shopping_list_cleaner
import tkinter as tk
import random
import io
newfile = None
window2 = None
ingredientJson = None
olist = {}
variables = {}

file_check()

week = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
#adding skip to picked meal dict to avoid 
pickedMealDict = {}
for day in week:
    pickedMealDict[day] = "skip"

alreadyRolled = set()

#window setup
root = tk.Tk()
root.resizable(300,700)
root.rowconfigure(9, weight= 1)
root.columnconfigure(7,weight = 2)


#titlescreen
hl = tk.Label(root,text = "I'm here to help you with the food. Just follow the steps and i gotcha in no time!",padx=2,pady=2)
hl.grid(row=0,column=0,columnspan=4)

#function that writes shopping list based on what recipes is chosen
def shoppingListWriter():
    global week, variables, pickedMealDict
    #print("in shopping list writer pickedMelaDIct is: ",pickedMealDict)
    ingredientList = None
    shoppingList = []
    for day in week:
        chosenMeal =pickedMealDict[day]
        #print("dagen er :",day)
        #print("retten er:" , pickedMealDict[day])
        if chosenMeal == "skip":
            continue
      
        try:
            #print("valgt rett: ",chosenMeal)            
            with open("{}.txt".format(chosenMeal), "r") as ingredientFile:
                #print("ingredientlist in json is: ", ingredientFile)
                ingredientList = json.load(ingredientFile)
                ingredientFile.close()
                

                shoppingList.append(ingredientList)

        except FileNotFoundError:
            print(f"file not found {chosenMeal}.txt")
        finally:
            if ingredientFile is not None or isinstance(ingredientFile, IOBase):
                ingredientFile.close()
    ingredients.delete("1.0", "end")

    sortedList = shopping_list_cleaner(shoppingList)
    for ingredient in sortedList.keys():
        ingredients.insert("0.0","{}x  {}\n".format(sortedList[ingredient],ingredient))
        #print("ingredient:", ingredient,"the type is: ", type(ingredient))


# function for getting random meal

def mealPicker(day):
    global variables, pickedMealDict
    recipeList = load_recipes()
    speed = variables[day].get()
    if speed == "skip":
        ChosenMealLabel[day].config(text="----------")
        pickedMealDict[day] = "skip"
        return
    #print("olist",recipeList)
    pickedMeal = random.choice(recipeList[speed])
    
    print("the picked meal is ",pickedMeal,"its type is:" ,type(pickedMeal))
    
    pickedMealDict[day] = pickedMeal
    print("meal for",day," is", pickedMealDict[day])
    ChosenMealLabel[day].config(text=pickedMeal)
    try:
        pickedStr = str(pickedMeal)
        ingredients = open(pickedStr+".txt", "r")       
    finally:
        ingredients.close()
    shoppingListWriter()


# label, radiobuttons, picked meal and buttons for rollin!


options = [(1,"slow"),(2,"medium"),(3,"fast",),(4,"skip")]
counter = 0
roller ={}
ChosenMealLabel= {}
for day in week:
        counter += 1
        counter2 = 1
        dayLabel = tk.Label(text = day)
        dayLabel.grid(row=counter,column=0)
        dayStr = str(day)+"speed"
        #Radiobuttons
        variables[day] = tk.StringVar(root)
        variables[day].set("skip")
        for opt, speed in options:
            optStr = str(opt)
            combi = dayStr+optStr
            combi = tk.Radiobutton(root, text= speed, value= speed, variable= variables[day])
            combi.grid(row=counter, column=counter2, columnspan=1)
            counter2 += 1
        #Button for rolling that meal
        roller[day] = tk.Button(root,text="Roll!", command=lambda day = day:mealPicker(day), padx=10)
        roller[day].grid(row=counter, column=7)
        #Label for picked meal
        ChosenMealLabel[day] = tk.Label(text = "----------")
        ChosenMealLabel[day].grid(row=counter,column=6)


#OneButtonToRollTHemAll
def OneButtonToRollTHemAll():
    for day in week:
        mealPicker(day)
oneButton = tk.Button(root,text ="One button to roll them all.",command=OneButtonToRollTHemAll)
oneButton.grid(row= 8,column= 6)

#textbox for shopping list
ingredientsFrame = tk.Frame(root,width=50,height=10,padx=2,pady=2)
ingredientsFrame.grid(row=8,column=0,columnspan= 5, padx=2,pady=2)
ingredients = tk.Text(ingredientsFrame,height=15)
ingredients.grid(row=0,column=0,padx=2,pady=2)

      

#Button and function for opnening recipe saver
def receipeSaver():
    windowCreator(root)

addMealButton = tk.Button(root, text="Add meal")
addMealButton.configure(command=receipeSaver)
addMealButton.grid(column=6,row=9,padx=2,pady=2)


root.mainloop()