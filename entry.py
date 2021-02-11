from tkinter import *
root = Tk()

e=Entry(root,width='50')
e.pack()

def click():
    label=Label(root,text=e.get())
    label.pack()
    
button=Button(root,text="enter your name",command=click)
button.pack()

root.mainloop()