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
player_x = window_size / grid_resolution
player_y = window_size / grid_resolution

player_shape = board.create_rectangle(player_x, player_y, player_x + (window_size / grid_resolution),
                                      player_y + (window_size / grid_resolution), fill="green")

# variables to track movement
move_direction = "right"

def move_loop():
    global move_direction
    if move_direction == "right":
        moveRight()
    elif move_direction == "left":
        moveLeft()
    elif move_direction == "up":
        moveUp()
    elif move_direction == "down":
        moveDown()
    root.after(200, move_loop)

def input_handler(event):
    global move_direction

    if event.char == "d":
        move_direction = "right"
    elif event.char == "a":
        move_direction = "left"
    elif event.char == "w":
        move_direction = "up"
    elif event.char == "s":
        move_direction = "down"

#controls
def moveRight():
    global player_x
    global board
    
    next_x = player_x + (window_size / grid_resolution)
    if next_x <= window_size - (window_size / grid_resolution):
        player_x = next_x
    else:
        first_x = window_size / grid_resolution
        player_x = first_x - 1

    board.coords(player_shape, player_x, player_y, player_x + (window_size / grid_resolution),
            player_y + (window_size / grid_resolution))

    print("Moved right")

def moveLeft():
    global player_x

    next_x = player_x - (window_size / grid_resolution)
    if next_x >= 0:
        player_x = next_x
    else:
        last_x = window_size - (window_size / grid_resolution)
        player_x = last_x + 1

    board.coords(player_shape, player_x, player_y, player_x + (window_size / grid_resolution),
            player_y + (window_size / grid_resolution))

    print("Moved left")

def moveUp():
    global player_y

    next_y = player_y - (window_size / grid_resolution)
    if next_y >= 0:
        player_y = next_y
    else:
        last_y = window_size - (window_size / grid_resolution)
        player_y = last_y + 1

    board.coords(player_shape, player_x, player_y, player_x + (window_size / grid_resolution),
            player_y + (window_size / grid_resolution))

    print("Moved up")

def moveDown():
    global player_y

    next_y = player_y + (window_size / grid_resolution)
    if next_y <= window_size - (window_size / grid_resolution):
        player_y = next_y
    else:
        first_y = window_size / grid_resolution
        player_y = first_y - 1

    board.coords(player_shape, player_x, player_y, player_x + (window_size / grid_resolution),
            player_y + (window_size / grid_resolution))

    print("Moved down")

root.bind("<KeyPress>", input_handler )

board.pack()
root.after(200, move_loop)
root.mainloop()