import tkinter as tk
from tkinter import messagebox

#main window
root = tk.Tk()
root.title("simple list")
root.geometry("400x450")
root.config(bg="black")
 
 #------function------
#add task
def add_task():
    task = task_entry.get()
    if task!="":
        Listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Waning","pleas enter a task!")
    #delete task
    def delete_task():
    
       
        try:
            seleted = listbox.curselection()
            listbox.delete(seleted)
        except:
            confirm = messagebox.askyesno("confirm","Do you want delete all task!")

#delete all task
def delete_all():
    confirm = messagebox.askyesno("confirm","do you want to delete all task?")
    if confirm:
        listbox.delete(0,tk.END)
# entry hight and widget
task_entry = tk.Entry(root,width=30,font=("Arial",14),bg="blue")
task_entry.pack(pady=10)
#entry add button
add_btn = tk.Button(root,text="Add Task", width=20, command=add_task)
add_btn.pack(pady=5)
#entry listbox
listbox = tk.Listbox(root,width=35, height=10, font=("Arial", 12)) 
listbox.pack(pady=10)
#Delete button
delete_btn = tk.Button(root,text="delete selected",width=20,command=delete_all)
delete_btn.pack(pady=5)
#Delete_all button
delete_all_btn = tk.Button(root,text="Delete Selected",width=20,command=delete_all)
delete_all_btn.pack(pady=5)
root.mainloop()


