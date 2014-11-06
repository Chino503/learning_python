from tkinter import *

root = Tk()

one = Label(root, text="One",bg="red", fg="white")
one.pack()
two = Label(root, text="Two",bg="black", fg="white")
two.pack(fill=X)
three = Label(root, text="Three",bg="purple", fg="yellow")
three.pack(side=LEFT, fill=Y)

root.mainloop()