
import tkinter as tk
from PTL import Image, ImageTK
import random


window = tk.Tk()
window.geometry("500*360")
window.title("Dice Roll")
def roll_dice():
 a= random.randint(1,6)
 label= tk.Label(window,text = a).pack


button= tk.Button(window,text="click",command=roll_dice)
button.pack()


dice=["dice1.png","dice2.png","dice3.png","dice4.png","dice5.png"," dice6.png"]
image1 = ImageTK.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTK.PhotoImage(Image.open(random.choice(dice)))

label1= tk.Label(window,image=image1)
label2= tk.Label(window,image=image2)
label1.image=image1
label2.image=image2

label1.place(x=40, y=100)
label2.place(x=300,y=100)

def dice-roll():
    image1 = ImageTK.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image= image1)
    label1.image=image1
    image2 = ImageTK.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image= image2)
    label2.image=image2



button= tk.Button(window,text="ROLL",bg="black",fg="pink", font="Times 20 bold",command=dice_roll)
button.place(x=230, y=0)


window.mainloop()


