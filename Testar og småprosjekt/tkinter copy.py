from tkinter import *
root  = Tk()
root.title("Simple calculator")


e = Entry(root, width=35)
e.grid(row=0,column=0,columnspan=3,padx=2,pady=10)

# The number we rar writing 
tn = ""
nl = []
sum = 0

#define buttons
def Button_typing(number):
    global tn
    tn += str(number)
    e.delete(0,len(tn))
    e.insert(0, tn)
    #print(tn)


def clear_button():
    global tn, nl
    e.delete(0,len(tn))
    tn = ""
    nl.clear()
        


def button_adding():
    global tn
    nl.append(int(tn))
    e.delete(0,len(tn))
    tn = ""


def equal_button():
    global sum, nl, tn
    e.delete(0,len(tn))
    for i in nl:
        sum += int(i)
    sum += int(tn)
    tn = str(sum)
    e.insert(0,sum)
    sum = 0


#define buttons
button_1 = Button(root,text="1",padx=40,pady=40,command=lambda: Button_typing(1))
button_2 = Button(root,text="2",padx=40,pady=40,command=lambda: Button_typing(2))
button_3 = Button(root,text="3",padx=40,pady=40,command=lambda: Button_typing(3))
button_4 = Button(root,text="4",padx=40,pady=40,command=lambda: Button_typing(4))
button_5 = Button(root,text="5",padx=40,pady=40,command=lambda: Button_typing(5))
button_6 = Button(root,text="6",padx=40,pady=40,command=lambda: Button_typing(6))
button_7 = Button(root,text="7",padx=40,pady=40,command=lambda: Button_typing(7))
button_8 = Button(root,text="8",padx=40,pady=40,command=lambda: Button_typing(8))
button_9 = Button(root,text="9",padx=40,pady=40,command=lambda: Button_typing(9))
button_0 = Button(root,text="0",padx=40,pady=40,command=lambda: Button_typing(0))

button_add = Button(root,text="+",padx=80,pady=40,command= button_adding)
button_equal = Button(root,text="=",padx=80,pady=40,command= equal_button)
button_clear = Button(root,text="clear",padx=40,pady=40,command=clear_button)

button_1.grid(row=3 ,column=0)
button_2.grid(row=3 ,column=1)
button_3.grid(row=3 ,column=2)
button_4.grid(row=2 ,column=0)
button_5.grid(row=2 ,column=1)
button_6.grid(row=2 ,column=2)
button_7.grid(row=1 ,column=0)
button_8.grid(row=1 ,column=1)
button_9.grid(row=1 ,column=2)

button_0.grid(row=4 ,column=0)

button_add.grid(row=4,column=1,columnspan=2)
button_clear.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)


"""
button_1.grid(row= ,column=)
button_1.grid(row= ,column=)

button_1(root,text="1",padx=40,pady=40,command=button_add)
button_1(root,text="1",padx=40,pady=40,command=button_add)
button_1(root,text="1",padx=40,pady=40,command=button_add)
"""

"""
def myClick():
    myLabel = Label(root, text="Hello " + e.get())
    myLabel.pack()

myButton = Button(root,text="Enter your name",  padx=40,pady=20, command=myClick, fg="blue", bg="red" )
myButton.pack()
"""


root.mainloop()

