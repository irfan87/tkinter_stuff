from tkinter import *

root = Tk()

firstLabel = Label(root, text="Hello World!")
secondLabel = Label(root, text="My first name is Ahmad Irfan")

firstLabel.grid(row=0, column=0)
secondLabel.grid(row=1, column=1)

root.mainloop()
