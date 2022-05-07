from tkinter import *

root = Tk()


def btnClick():
    textLabel = Label(root, text="Hello World!")
    textLabel.pack()
    # textLabel.grid(row=2, column=2)


# firstButton = Button(root, text="Click Me!", state=DISABLED)
# firstButton = Button(root, text="Click Me!", padx=50, pady=50)
firstButton = Button(root, text="Click Me!", command=btnClick, fg="green", bg="#40E0D0")

# firstButton.grid(row=1, column=2)
firstButton.pack()

root.mainloop()
