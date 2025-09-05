from tkinter import*
from tkinter import messagebox
import tkinter as tk
#import pygame

root = tk.Tk();
root.title('Connect 4')
canvas_width = 820
canvas_height = 790
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="blue")
canvas.pack()

startx = 20
starty = 100
endx = startx+100
endy = starty+100
count=0

for i in range(6):
    for j in range(7):
        count = canvas.create_oval(startx,starty,endx,endy,outline="black", fill="white", width=3)
        startx+=100+15
        endx+=100+15
        count+=1
    startx =20
    endx  = 20+100
    starty+=100+15
    endy+=100+15
    
def on_button_click():
    pass
    
button = tk.Button(root, text="Click Me", command=on_button_click)
#canvas.create_window()
button.place(x=150, y=100, width=100, height=50)

#canvas.itemconfigure("1", fill="red")
turn = True # red starts
count = 0


        


root.mainloop();