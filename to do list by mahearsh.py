from tkinter import *
window=Tk()
window.title("To Do List By Mahearsh")
window.configure(background="#aed0e8")
window.iconbitmap(r'todl.ico')


def add_task():
    task = e.get()
    if task:
        l.insert(END, task)
        e.delete(0,END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")



def delete_task():
    try:
        selected_task_index = l.curselection()[0]
        l.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")


f1=Frame(window,bg="#aed0e8")
e=Entry(f1,width=20,font=("calibri",20),bg="#ffc0cb")
e.pack(padx=18,pady=18,side=LEFT)
b=Button(f1,text="Add",padx=5,pady=5,bg="#ffecb8",command=add_task)
b.pack(padx=18,pady=18,side=LEFT)
f1.pack()


f2=Frame(window,bg="#aed0e8")
l=Listbox(f2,width=20,font=("calibri",20),bg="#ffc0cb")
l.pack(padx=18,pady=18,side=LEFT)
b=Button(f2,text="Delete",padx=5,pady=5,bg="#ffecb8",command=delete_task)
b.pack(padx=18,pady=18,side=LEFT)
f2.pack()


window.mainloop()
