import tkinter as tk
import json
import os
from div import transform_text_to_list

#olist = {}
f = None
newfile = None
dn = None
cookingSpeedRadiobButton = None
inf = None

#Function that makes a recipe file if none exists
def file_check():
    try:
        if os.path.exists("recipes.txt"):
            return
        else:
            temporaryFile = open("recipes.txt", "w")
            temporaryFile.write('{}')

    except:
        temporaryFile.close()

file_check()


# Loads the list of recipes
def load_recipes():
    try:
        global f, recipeList
        f = open("recipes.txt", "r")
        recipes = f.read()
        print("saved", recipes)
        recipeList = json.loads(recipes)


    finally:
        f.close()
        return recipeList

# saves the name of the different recipies in the different lists
newfile = None
def save_recipes():
    try:
        global f, recipeList
        dishName = dn.get()
        speed = cookingSpeedRadiobButton.get()
        
        if speed not in recipeList:
            recipeList[speed] = set()
        if isinstance(recipeList[speed], list):
            recipeList[speed] = set()
        recipeList[speed].add(dishName)
        updatedList = json.dumps(recipeList, default=list)
        f = open("recipes.txt", "w")      
        f.write(updatedList)
    finally:
        f.close()
    try:
        dishName = dn.get()
        ingredients = inf.get(0.0,tk.END)
        ingredientsList = transform_text_to_list(ingredients)
        ingredientsJson = json.dumps(ingredientsList)
        
        newfile = open("{}.txt".format(dishName), "w")
        newfile.write(ingredientsJson)
        inf.delete("1.0", tk.END)
        dn.delete("0", tk.END)

    finally:
        if newfile:
            newfile.close()


#window func
def windowCreator(root):
    global dn,cookingSpeedRadiobButton, inf, rb, window2
    window2 = tk.Toplevel()
    window2.title("Add Recipe")
    window2.resizable(10,10)
    window2.rowconfigure(6, weight=1)
    window2.columnconfigure(4, weight=1)
    window2.protocol("WM_DELETE_WINDOW", on_closing)
    #window2.protocol("WM_DELETE_WINDOW",load_recipes())
    #tutorial
    hl = tk.Label(window2,text = "welcome to the dish creator. Simply name the dish, dicide its cooking speed and enter the neccessery cooking ingedients! ",padx=2,pady=2)
    hl.grid(row=0,column=0,columnspan=4,sticky=tk.NW)

    #Descrition 
    hl = tk.Label(window2,text = "Dishname: ",padx=2,pady=2)
    hl.grid(row=1,column=0,sticky=tk.NW,padx=2,pady=2)

    #Entry for dish name
    dn = tk.Entry(window2,width=40)
    dn.grid(row=1,column=1,columnspan=2,padx=2,pady=2,sticky=tk.W)

    #Frame that holds textfield
    f1 = tk.Frame(window2,width=100,height=200,padx=2,pady=2)
    f1.grid(row=5,column=0,columnspan=5,padx=2,pady=2)

    #textfield
    inf = tk.Text(f1)
    inf.grid(row=5,column=0,padx=2,pady=2)

    #Label for ingredients
    l2  = tk.Label(window2,text="Ingredients:")
    l2.grid(row=4,column=0,padx=2,pady=2)

    #label for cooking speed!
    l3 = tk.Label(window2,text="Cooking speed!")
    l3.grid(row=3,column=0,sticky= tk.W,padx=2,pady=2)

    #radiobuttons (cooking speed)
    count = 0
    rb = ["fast","medium","slow"]
    cookingSpeedRadiobButton = tk.StringVar(window2)
    cookingSpeedRadiobButton.set("medium")
    for speed in rb:
        speed = tk.Radiobutton(window2,text=speed,value=speed,variable=cookingSpeedRadiobButton)
        speed.grid(row=3,column=count+1,sticky=tk.W,padx=2,pady=2)
        count += 1

    #add to dishes button
    b1 = tk.Button(window2,text="Add to dishes", command = save_recipes)
    b1.grid(row=6,column=4, sticky=tk.E,padx=2,pady=2)

def on_closing():
    if window2.winfo_exists():
        load_recipes()
        window2.destroy()

        


"""
def saveText():
    global olist, dn,vb,inf
    dishName =  dn.get()
    speed = vb.get()
    olist[speed].append(dishName)
    try:
        f = open("{}.txt".format(dishName),"w")
        f.write(inf.get(0.0,tk.END))

    except:
        print("Something went wrong, please try again.")
    finally:
        f.close()
"""
load_recipes()






