from tkinter import *
root = Tk()
root.title("Calculator")
e=Entry(root,width='35',borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
# e.insert(0,"")

def buttonadd(number):
    return 

# buttons
button1=Button(root,text="1",padx=40,pady=20,command=Lambda: buttonclick())
button2=Button(root,text="2",padx=40,pady=20,command=Lambda: buttonclick())
button3=Button(root,text="3",padx=40,pady=20,command=Lambda: buttonclick())
button4=Button(root,text="4",padx=40,pady=20,command=Lambda: buttonclick())
button5=Button(root,text="5",padx=40,pady=20,command=Lambda: buttonclick())
button6=Button(root,text="6",padx=40,pady=20,command=Lambda: buttonclick())
button7=Button(root,text="7",padx=40,pady=20,command=Lambda: buttonclick())
button8=Button(root,text="8",padx=40,pady=20,command=Lambda: buttonclick())
button9=Button(root,text="9",padx=40,pady=20,command=Lambda: buttonclick())
button0=Button(root,text="0",padx=40,pady=20,command=Lambda: buttonclick())
buttonadd=Button(root,text="+",padx=39,pady=20,command=Lambda: buttonclick())
buttonsub=Button(root,text="-",padx=40,pady=20,command=Lambda: buttonclick())
buttonclear=Button(root,text="Clear", padx=30,pady=53,command= Lambda: buttonclick())
buttonequal=Button(root,text="=",padx=40,pady=51,command=Lambda: buttonclick())


# on screen,
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
buttonadd.grid(row=4,column=1)
buttonsub.grid(row=4,column=2)
buttonequal.grid(row=1,column=3,rowspan=2)
buttonclear.grid(row=3,column=3,rowspan=2)


# button1.pack()

root.mainloop()