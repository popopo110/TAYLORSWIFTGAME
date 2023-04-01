from tkinter import *
import random
from PIL import ImageTk, Image
root = Tk()

# Load the image
img = Image.open("/Users/hokhaloi/Downloads/SNA.jpg")
photo = ImageTk.PhotoImage(img)

# Create a canvas
canvas = Canvas(root, width=500, height=500)
canvas.pack()

# Add the image to the canvas
canvas.create_image(250, 250, image=photo)

# Run the main loop
root.mainloop()

GAME_WIDTH= 700
GAME_HEIGHT= 700
SPEED=50
SPACE_SIZE=50
BODY_PARTS=3
SNAKE_COLOR="red"
FOOD_COLOR="green"
BACKGROUND_COLOR="white"

class SNAKE:
    pass
class FOOD:
    def __init__(self):
        x=random.randint(0,(GAME_WIDTH/SPACE_SIZE))*SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE)) * SPACE_SIZE

        self.coordinates=[x,y]
        canvas.create_image()
def nextturn():
    pass
def changedirection():
    pass
def checkcollision():
    pass
def gameover():
    pass

window= Tk()
window.title("THE TAYLOR SWIFT")
window.resizable(False,False)

score=0
direction='down'
label=Label(window, text=f"score is: {score}", font=("consolas",30))
label.pack()

canvas=Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

x=int((screen_width/2)-(window_width/2))
y=int((screen_height/2)-(window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.mainloop()


