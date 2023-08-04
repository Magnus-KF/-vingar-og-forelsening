import tkinter as tk
import time

#boardsize
x_board_size = 20
y_board_size = 20

#window and grid configuration
root = tk.Tk()
root.wm_withdraw()
root.resizable(400,400)
root.columnconfigure(x_board_size)
root.rowconfigure(y_board_size)

#coodrinate system
    #dictionary with names "x:(x value)_y:(y value)", 
coordinate_system_dictionary= {}
for y in range(0,y_board_size):
    for x in range(0,x_board_size):
        var_name = "x:{}_y:{}".format(x,y)
        coordinate_system_dictionary[var_name] = tk.Button( width=2, height=1,bd=1)
        coordinate_system_dictionary[var_name].grid(column=x, row=y)

#starting position for snake
starting_position = "x:{}_y:{}".format(int(x_board_size/2),int(y_board_size/2))
coordinate_system_dictionary[starting_position].configure(text="S")

#snake controls
x_position = int(x_board_size/2)
y_position = int(y_board_size/2)
snake_head = "x:{}_y:{}".format(x_position,y_position)
speed = 1

def moveRight (event):
       global x_position, coordinate_system_dictionary
       x =1
       while x < 6:
            x_position += 1
            snake_head = "x:{}_y:{}".format(x_position,y_position)
            coordinate_system_dictionary[snake_head].configure(text ="s")
            time.sleep(1)
            x +=1
root.bind("<KeyPress-d>", moveRight )
    

root.wm_deiconify()
root.mainloop()