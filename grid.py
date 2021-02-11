from tkinter import *
root=Tk()

# label widget
mylabel1 = Label(root,text="wassupppp")
mylabel2 = Label(root,text="good")
mylabel3 = Label(root,text="aight").grid(row=2,column=2)
# inserting in the screen
mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1,column=5)
root.mainloop()