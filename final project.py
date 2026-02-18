import tkinter as tk
from tkinter import messagebox

#main window
root = tk.Tk()
root.title(" Farzana Afroz,simple list")
root.geometry("500x500")
root.config(bg="white")
 
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
            seleted = listbox.curselection
            listbox.delete(seleted)
        except:
            confirm = messagebox.askyesno("confirm","Do you want delete all task!")

#delete all task
def delete_all():
    confirm = messagebox.askyesno("confirm","do you want to delete all task?")
    if confirm:
        listbox.delete(0,tk.END)
# entry hight and widget
task_entry = tk.Entry(root,width=25,font=("Arial",14),bg="green")
task_entry.pack(pady=10)
#entry add button
add_btn = tk.Button(
    root,
    text="Add task",width=20,command=add_task,bg="green",fg="white",
    font=("Arial",12,"bold")

)
add_btn.pack(pady=5)
#entry listbox
listbox = tk.Listbox(
    root,width=37,bg="blue",font=("Arial",12,"bold")
) 
listbox.pack(pady=10)
#Delete button
delete_btn = tk.Button(
    root,text="Deleted selected",width=20,command=delete_all,bg="green",fg="white",
    font=("Arial",12,"bold"),activebackground="sky blue"
)
delete_btn.pack(pady=5)
#Delete_all button
delete_all_btn = tk.Button(
    root,text="Deleted Selectd",width=20,command=delete_all,bg="green",fg="white",
    font=("Arial",12,"bold"),activebackground="blue"
)
delete_all_btn.pack(pady=5)
root.mainloop()




 
    
   
    

 



