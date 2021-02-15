from tkinter import *
root = Tk()

e=Entry(root,width='50')
e.pack()
e.insert(0,"enter your name:")

def click():
    label=Label(root,text='hello'+e.get())
    label.pack()
    
button=Button(root,text="enter your name",command=click)
button.pack()

root.mainloop()