from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("PokéMon Game")

root.geometry("1920x1080")

root.configure(bg="orange")

img = ""

player1  = Label(root, bg="red", fg="white", text="player 1")

player1.place(relx=0.1, rely=0.3, anchor=CENTER)

## Player 2


player2  = Label(root, bg="red", fg="white", text="player 2")

player2.place(relx=0.9, rely=0.3, anchor=CENTER)


p1_score = Label(root, bg="blue", fg="white", text="hello")

p1_score.place(relx=0.1, rely=0.4, anchor=CENTER)

p2_score = Label(root, bg="blue", fg="white")

p2_score.place(relx=0.9, rely=0.4, anchor=CENTER)


rdl = Label(root, fg="black", bg="white")
rdl.place(relx = 0.5 , rely = 0.6, anchor = CENTER )

root,mainloop()