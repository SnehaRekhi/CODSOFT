import tkinter 
from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title("To-Do-list")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list= []

def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)

    if task:
        status_task = "[ ] " + task  # Mark it as incomplete initially
        with open("tasklist.txt",'a',encoding='utf-8') as taskfile:
            taskfile.write(f"\n{task}\t\t{status_task}\n")
        task_list.append(status_task)
        listbox.insert(END, status_task)

def deleteTask():
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w',encoding='utf-8') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete(ANCHOR)

def markComplete():
    task = str(listbox.get(ANCHOR))
    if "[ ]" in task:  # Only mark incomplete tasks
        updated_task = task.replace("[ ]", "[\u2714]")  # Mark as complete
        updateTaskStatus(task, updated_task)


def markIncomplete():
    task = str(listbox.get(ANCHOR))
    if "[\u2714]" in task:  # Only mark completed tasks
        updated_task = task.replace("[\u2714]", "[ ]")  # Mark as incomplete
        updateTaskStatus(task, updated_task)

def updateTaskStatus(old_task, new_task):
    if old_task in task_list:
        index = task_list.index(old_task)
        task_list[index] = new_task

        with open("tasklist.txt", 'w',encoding='utf-8') as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")

        listbox.delete(0, END)
        for task in task_list:
            listbox.insert(END, task)

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks=taskfile.readlines()
            
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file=open('tasklist.txt','w')
        file.close()


#icon
Image_icon=PhotoImage(file="Image/task.png")
root.iconphoto(False,Image_icon)

#BG
original_image = Image.open("Image/top2.png")
resized_image = original_image.resize((400,650), Image.Resampling.LANCZOS)
bgImage=ImageTk.PhotoImage(resized_image)
Label(root,image=bgImage).place(x=0,y=0)

#DockImage Section
original_image1 = Image.open("Image/Save.png")
resized_image1 = original_image1.resize((380,630), Image.Resampling.LANCZOS)
dockImage=ImageTk.PhotoImage(resized_image1)
Label(root,image=dockImage,bg="#664229").place(x=10,y=10)

#Heading Section
original_image2 = Image.open("Image/Head.png")
resized_image2 = original_image2.resize((300,45), Image.Resampling.LANCZOS)
noteImage=ImageTk.PhotoImage(resized_image2)
Label(root,image=noteImage).place(x=50,y=19)

heading=Label(root,text="ALL TASK",font="Aparajita 24 bold",fg="white",bg="#47271A")
heading.place(x=130,y=21)

#main
frame= Frame(root,width=350,height=50,bg="#D2B48C")
frame.place(x=30,y=150)

task=StringVar()
task_entry=Entry(frame,width=25,font="Aparajita 20",bg="#D2B48C",fg="white",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="ADD",font="Aparajita 22 bold",width=6,bg="#664229",fg="#fff",bd=0,command=addTask)
button.place(x=250,y=0)

#listbox
frame1=Frame(root,bd=3,height=680,width=350,bg="#D2B48C")
frame1.place(x=44, y=220) 

listbox= Listbox(frame1,font=('Aparajita',14),width=35,height=14,bg="#411900",fg="white",cursor="hand2",selectbackground="#D2B48C")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#Buttons to mark complete and incomplete
original_image4 = Image.open("Image/tick.png")
resized_image4 = original_image4.resize((30, 30), Image.Resampling.LANCZOS)
Tick_icon = ImageTk.PhotoImage(resized_image4)
Button(root,image=Tick_icon,bg="#D2B48C",bd=0,command=markComplete).place(x=140,y=580)

original_image5 = Image.open("Image/cross.png")
resized_image5 = original_image5.resize((30, 30), Image.Resampling.LANCZOS)
Cross_icon = ImageTk.PhotoImage(resized_image5)
Button(root,image=Cross_icon,bg="#D2B48C",bd=0,command=markIncomplete).place(x=240,y=580)

#delete
original_image3 = Image.open("Image/Delete2.png")
resized_image3 = original_image3.resize((30, 30), Image.Resampling.LANCZOS)
Delete_icon = ImageTk.PhotoImage(resized_image3)
Button(root,image=Delete_icon,bg="#D2B48C",bd=0,command=deleteTask).place(x=190,y=580)



root.mainloop()