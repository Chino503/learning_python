from tkinter import *

root = Tk()

lblName = Label(root, text="Name")
lblPassword = Label(root, text="Password")
txtName = Entry(root);
txtPassword = Entry(root);

lblName.grid(row=0)
lblPassword.grid(row=1)
txtName.grid(row=0,column=1)
txtPassword.grid(row=1,column=1)

root.mainloop()