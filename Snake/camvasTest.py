import tkinter as tk
import time

window_size = int(600)
root = tk.Tk()
root.resizable(height = window_size, width= window_size)


board = tk.Canvas(root)
board.configure(height = window_size,width = window_size)


#grid for game
grid_resolution = int(20)
for i in range(1,grid_resolution):
    board.create_line(i*(window_size/grid_resolution),0,i*int(window_size/grid_resolution),window_size)  
    board.create_line(0,i*(window_size/grid_resolution),window_size,i*int(window_size/grid_resolution)) 

#snakeshape

#initial position
if "head_x" not in locals():
    head_x = window_size/grid_resolution
    head_y = window_size/grid_resolution

board.create_rectangle(head_x,head_y,head_x+(window_size/grid_resolution),head_y+(window_size/grid_resolution), fill= "green")

#controls
def moveRight (event):
            global head_x
            time.sleep(0.2)
            head_x += window_size/grid_resolution
            root.after(200,moveRight)
            print("right")
            print("{}".format(event))

root.bind("<KeyPress-d>", moveRight )

board.pack()


root.mainloop()