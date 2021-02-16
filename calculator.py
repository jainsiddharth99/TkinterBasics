from tkinter import *
root = Tk()
root.title("Calculator")
e=Entry(root,width='35',borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
# e.insert(0,"")

def buttonclick(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(number))
    
def buttonclear():
    e.delete(0,END)
    
def add():
    first_num=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_num)
    e.delete(0,END)
    
def sub():   
    first_num=e.get()
    global f_num
    global math
    math="subtract"
    f_num=int(first_num)
    e.delete(0,END)
    
def multiply():
    return

def divide():
    return

def equal():
    second_num=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,f_num+int(second_num))
    elif math=="subtract":
        e.insert(0,f_num-int(second_num))
        
        
# buttons
button1=Button(root,text="1",padx=40,pady=20,command=lambda: buttonclick(1))
button2=Button(root,text="2",padx=40,pady=20,command=lambda: buttonclick(2))
button3=Button(root,text="3",padx=40,pady=20,command=lambda: buttonclick(3))
button4=Button(root,text="4",padx=40,pady=20,command=lambda: buttonclick(4))
button5=Button(root,text="5",padx=40,pady=20,command=lambda: buttonclick(5))
button6=Button(root,text="6",padx=40,pady=20,command=lambda: buttonclick(6))
button7=Button(root,text="7",padx=40,pady=20,command=lambda: buttonclick(7))
button8=Button(root,text="8",padx=40,pady=20,command=lambda: buttonclick(8))
button9=Button(root,text="9",padx=40,pady=20,command=lambda: buttonclick(9))
button0=Button(root,text="0",padx=40,pady=20,command=lambda: buttonclick(0))

buttonadd=Button(root,text="+",padx=39,pady=20,command=add)
buttonsub=Button(root,text="-",padx=40,pady=20,command=sub)
buttonequal=Button(root,text="=",padx=87,pady=20,command=equal)
buttonclear=Button(root,text="Clear",padx=60,pady=20,command=buttonclear)

buttondivide=Button(root,text="/", padx=20,pady=51,command= divide)
buttonmultiply=Button(root,text="X", padx=20,pady=51,command=multiply)

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

buttonmultiply.grid(row=1,column=3,rowspan=2)
buttondivide.grid(row=3,column=3,rowspan=2)
buttonequal.grid(row=5,column=0,columnspan=2)
buttonclear.grid(row=5,column=2,columnspan=2)

root.mainloop()