from tkinter import *
root = Tk()

def click():
    label=Label(root,text="Clicked")
    label.pack()
    
button=Button(root,text="click me",command=click)
button.pack()
root.mainloop()