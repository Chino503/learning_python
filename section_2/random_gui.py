from tkinter import *

root = Tk() # always make a main window

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

btnFirst = Button(topFrame, text="Button Red", fg="red")
btnTwo = Button(topFrame, text="Button Green", fg="green")
btnThree = Button(bottomFrame, text="Button Blue", fg="blue")

btnFirst.pack(side=LEFT)
btnTwo.pack(side=LEFT)
btnThree.pack(side=LEFT)

root.mainloop() # always have this
