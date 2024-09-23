import tkinter 
from tkinter import *

root=Tk()
root.title("Calculator")
root.geometry("400x430+400+100")
root.resizable(False,False)

expression=""

def display(value):
    global expression
    expression += str(value)
    num.set(expression)

def output():
    try:
        global expression
        result = str(eval(expression))
        num.set(result)
        expression = result
    except:
        num.set("Error")
        expression = "" 

def allclear():
    global expression
    expression = ""
    num.set("")
 
def clear():
    global expression
    expression = expression[:-1]
    num.set(expression)

#icon
Image_icon=PhotoImage(file="Image/calc.png")
root.iconphoto(False,Image_icon)

#input frame
frame= Frame(root,width=380,height=80,bg="#595959")
frame.place(x=10,y=20)

num = StringVar()
num_entry = Entry(frame, textvariable=num, width=23, font="Aparajita 28", fg="black",bg="white", bd=0, state='readonly')
num_entry.place(x=19, y=18)
num_entry.focus()

#Number Buttons
Button(root, text="9", font=("Aparajita", 18),width=6, bg="#616569", fg="white", command=lambda: display(9)).place(x=10, y=120)
Button(root, text="8", font=("Aparajita", 18),width=6, bg="#616569", fg="white", command=lambda:display(8)).place(x=95, y=120)
Button(root, text="7", font=("Aparajita", 18),width=6, bg="#616569", fg="white", command=lambda:display(7)).place(x=180, y=120)
Button(root, text="6", font=("Aparajita", 18),width=6, bg="#616569", fg="white", command=lambda:display(6)).place(x=10, y=180)
Button(root, text="5", font=("Aparajita", 18),width=6, bg="#616569", fg="white", command=lambda:display(5)).place(x=95, y=180)
Button(root, text="4", font=("Aparajita", 18),width=6, bg="#616569", fg="white", command=lambda:display(4)).place(x=180, y=180)
Button(root, text="3", font=("Aparajita", 18),width=6, bg="#616569", fg="white", command=lambda:display(3)).place(x=10, y=240)
Button(root, text="2", font=("Aparajita", 18),width=6, bg="#616569", fg="white", command=lambda:display(2)).place(x=95, y=240)
Button(root, text="1", font=("Aparajita", 18),width=6, bg="#616569", fg="white", command=lambda:display(1)).place(x=180, y=240)
Button(root, text="0", font=("Aparajita", 18),width=6, bg="#616569", fg="white", command=lambda:display(0)).place(x=10, y=300)
Button(root, text="00", font=("Aparajita", 18),width=6, bg="#616569", fg="white", command=lambda:display('00')).place(x=95, y=300)

#Calculation Buttons
Button(root, text="/", font=("Aparajita", 18),width=10, bg="#616569", fg="white", command=lambda:display('/')).place(x=265, y=120)
Button(root, text="*", font=("Aparajita", 18),width=10, bg="#616569", fg="white", command=lambda:display('*')).place(x=265, y=180)
Button(root, text="-", font=("Aparajita", 18),width=10, bg="#616569", fg="white", command=lambda:display('-')).place(x=265, y=240)
Button(root, text="+", font=("Aparajita", 26, "bold"),width=5,height=2, bg="#616569", fg="white", command=lambda:display('+')).place(x=290, y=300)

#Output Button
Button(root, text="=", font=("Aparajita", 18),width=8, bg="#616569", fg="white", command=output).place(x=180, y=300)

#Clear Button
Button(root, text="C", font=("Aparajita", 18),width=11, bg="#616569", fg="white", command=clear).place(x=10, y=360)
Button(root, text="AC", font=("Aparajita", 18),width=11, bg="#616569", fg="white", command=allclear).place(x=150, y=360)


root.mainloop()