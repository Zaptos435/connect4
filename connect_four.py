from tkinter import*
from tkinter import messagebox
root = Tk();
root.title('Connect 4')
root.iconbitmap();

#button click 
def b_click(b):
    pass

b00 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b00))
b01 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b01))
b02 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b02))
b03 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b03))
b04 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b04))
b05 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b05))
b06 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b06))

b10 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b10))
b11 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b11))
b12 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b12))
b13 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b13))
b14 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b14))
b15 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b15))
b16 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b16))

b20 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b20))
b21 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b21))
b22 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b22))
b23 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b23))
b24 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b24))
b25 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b25))
b26 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b26))

b30 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b30))
b31 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b31))
b32 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b32))
b33 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b33))
b34 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b34))
b35 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b35))
b36 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b36))


b40 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b40))
b41 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b41))
b42 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b42))
b43 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b43))
b44 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b44))
b45 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b45))
b46 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b46))

b50 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b50))
b51 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b51))
b52 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b52))
b53 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b53))
b54 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b54))
b55 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b55))
b56 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg="blue", command= lambda: b_click(b56))

board = [
    [b00,b01,b02,b03,b04,b05,b06],
    [b10,b11,b12,b13,b14,b15,b16],
    [b20,b21,b22,b23,b24,b25,b26],
    [b30,b31,b32,b33,b34,b35,b36],
    [b40,b41,b42,b43,b44,b45,b46],
    [b50,b51,b52,b53,b54,b55,b56]
    
    ]

b00.grid(row=0,column=0)
b01.grid(row=0,column=1)
b02.grid(row=0,column=2)
b03.grid(row=0,column=3)
b04.grid(row=0,column=4)
b05.grid(row=0,column=5)
b06.grid(row=0,column=6)

b10.grid(row=1,column=0)
b11.grid(row=1,column=1)
b12.grid(row=1,column=2)
b13.grid(row=1,column=3)
b14.grid(row=1,column=4)
b15.grid(row=1,column=5)
b16.grid(row=1,column=6)

b20.grid(row=2,column=0)
b21.grid(row=2,column=1)
b22.grid(row=2,column=2)
b23.grid(row=2,column=3)
b24.grid(row=2,column=4)
b25.grid(row=2,column=5)
b26.grid(row=2,column=6)

b30.grid(row=3,column=0)
b31.grid(row=3,column=1)
b32.grid(row=3,column=2)
b33.grid(row=3,column=3)
b34.grid(row=3,column=4)
b35.grid(row=3,column=5)
b36.grid(row=3,column=6)

b40.grid(row=4,column=0)
b41.grid(row=4,column=1)
b42.grid(row=4,column=2)
b43.grid(row=4,column=3)
b44.grid(row=4,column=4)
b45.grid(row=4,column=5)
b46.grid(row=4,column=6)

b50.grid(row=5,column=0)
b51.grid(row=5,column=1)
b52.grid(row=5,column=2)
b53.grid(row=5,column=3)
b54.grid(row=5,column=4)
b55.grid(row=5,column=5)
b56.grid(row=5,column=6)


root.mainloop();