from tkinter import *
root = Tk()

mybutton = Button(root,text="Click me",padx=50)
mybutton2 = Button(root,text="Click me",padx=50,pady=50)
mybutton3 = Button(root,text="Click me")
mybutton.pack()
mybutton2.pack()
mybutton3.pack()

root.mainloop()