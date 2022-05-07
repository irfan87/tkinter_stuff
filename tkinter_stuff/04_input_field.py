from tkinter import *

root = Tk()

# firstEntry = Entry(root, width=50, bg="blue", fg="white", borderwidth=5)
firstEntry = Entry(root, width=50)
firstEntry.pack()
firstEntry.insert(0, "Enter your name: ")


def getResult():
    result = f"Hello, {firstEntry.get().capitalize()}! Good Day!"
    resultText = Label(root, text=result)
    resultText.pack()


btnResult = Button(root, text="Enter your name", command=getResult)
btnResult.pack()

root.mainloop()
