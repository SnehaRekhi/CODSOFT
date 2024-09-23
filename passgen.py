from tkinter import *
from PIL import Image, ImageTk
import random
import string

root=Tk()
root.title("Pass Generator")
root.geometry("700x400+400+100")
root.resizable(False,False)

result=""

def gen():
    try:
        length = int(len.get())  # Get the length from the entry field and convert it to an integer
        if length < 1:
            result_label.config(text="Length should be at least 1")
        else:
            characters = string.ascii_letters + string.digits + string.punctuation  # Use letters, digits, and special characters
            password = ''.join(random.choice(characters) for _ in range(length))  # Generate a password of the specified length
            result_label.config(text=f" {password}")
    except ValueError:
        result_label.config(text="Please enter a valid number for length")

#icon
Image_icon=PhotoImage(file="Image/passgen.png")
root.iconphoto(False,Image_icon)

#BG
original_image = Image.open("Image/bg2.png")
resized_image = original_image.resize((720,400), Image.Resampling.LANCZOS)
bgImage=ImageTk.PhotoImage(resized_image)
Label(root,image=bgImage).place(x=0,y=0)

#Heading
heading=Label(root,text="PASSWORD GENERTOR",font="Aparajita 24 bold",fg="white",bg="#0e4c92")
heading.place(x=210,y=21)

#Input
Length=Label(root,text="Enter Length: ",font="Aparajita 16",fg="white",bg="#0e4c92")
Length.place(x=100,y=130)

frame= Frame(root,width=350,height=30,bg="white")
frame.place(x=210,y=130)

len = StringVar()
len_entry = Entry(frame, width=35, font="Aparajita 15", bg="white", fg="#0e4c92", bd=0, textvariable=len)
len_entry.grid(row=0, column=0, padx=5, pady=5)
len_entry.focus()

btn = Button(frame, text="Generate", font="Aparajita 15 bold", bg="#0e4c92", fg="white", bd=0, command=gen)
btn.grid(row=0, column=1, padx=10)

#output
frame1= Frame(root,width=350,height=30,bg="white")
frame1.place(x=210,y=230)

result_label = Label(frame1, text="", font="Aparajita 15", bg="white", fg="#0e4c92", width=35)
result_label.pack(padx=5, pady=5)

root.mainloop()