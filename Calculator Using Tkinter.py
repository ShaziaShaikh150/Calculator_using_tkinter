from tkinter import *


root = Tk()
root.geometry("354x460")
root.title("Calculator")


entry_val = StringVar()
value = ""

def exit():
    e1.delete(0,"end")
    value = ""

def click_button(number):
    global value
    value = value +str(number)
    entry_val.set(value)

def equal_button():
    global value
    equal = eval(value)
    entry_val.set(equal)
    value = ""

# Entry


e1 = Entry(root , width = 40 ,textvariable = entry_val )
e1.place(x = 50 , y = 30)

# Number Button Button

b1 = Button(root,text = "1" , padx =14 ,pady = 14 ,font=("arial 15"),command = lambda : click_button(1))
b1.place(x = 10,y = 100)

b2 = Button(root,text = "2" , padx =14 ,pady = 14 ,font=("arial 15"),command = lambda : click_button(2))
b2.place(x = 75,y = 100)

b3 = Button(root,text = "3" , padx =14 ,pady = 14 ,font=("arial 15"),command = lambda : click_button(3))
b3.place(x =140 ,y = 100)

b4 = Button(root,text = "4" , padx =14 ,pady = 14 ,font=("arial 15"),command = lambda : click_button(4))
b4.place(x = 10,y = 170)

b5 = Button(root,text = "5" , padx =14 ,pady = 14 ,font=("arial 15"),command = lambda : click_button(5))
b5.place(x = 75,y = 170)

b6 = Button(root,text = "6" , padx =14 ,pady = 14 ,font=("arial 15"),command = lambda : click_button(6))
b6.place(x =140 ,y = 170)

b7 = Button(root,text = "7" , padx =14 ,pady = 14 ,font=("arial 15"),command = lambda : click_button(7))
b7.place(x = 10,y = 240)

b8 = Button(root,text = "8" , padx =14 ,pady = 14 ,font=("arial 15"),command = lambda : click_button(8))
b8.place(x = 75,y = 240)

b9 = Button(root,text = "9" , padx =14 ,pady = 14 ,font=("arial 15"),command = lambda : click_button(9))
b9.place(x =140 ,y = 240)

b0 = Button(root,text = "0" , padx =14 ,pady = 14 ,font=("arial 15"),command = lambda : click_button(0))
b0.place(x =10 ,y = 310)

b_dot = Button(root,text = "." , padx =47 ,pady = 14 ,font=("arial 15"),command = lambda : click_button("."))
b_dot.place(x =75 ,y = 310)

# calculation button


add_b = Button(root,text = "+" , padx =14 ,pady = 14 ,font=("arial 15"),command = lambda : click_button("+"))
add_b.place(x =205 ,y = 100)

sub_b = Button(root,text = "-" , padx =14 ,pady = 14 ,font=("arial 15"),command = lambda : click_button("-"))
sub_b.place(x =205 ,y = 170)

mul_b = Button(root,text = "x" , padx =14 ,pady = 14 ,font=("arial 15"),command = lambda : click_button("*"))
mul_b.place(x =205 ,y = 240)

div_b = Button(root,text = "/" , padx =14 ,pady = 14 ,font=("arial 15"),command = lambda : click_button("/"))
div_b.place(x =205 ,y = 310)

# operational
#

equal_b = Button(root,text = "=" , padx =14 ,pady = 48 ,font=("arial 15"),command = equal_button)
equal_b.place(x =270 ,y = 242)

clear_b = Button(root,text = "C" , padx =14 ,pady = 48 ,font=("arial 15") , command = exit)
clear_b.place(x =270 ,y = 100)



root.mainloop()