import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title(" Farzana Afroz,Simple To-Do List") 
root.geometry("500x500") 
root.config(bg="white")

# ---------- Functions ----------

# Add Task
def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Delete Selected Task
def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task!")

# Delete All Tasks
def delete_all():
    confirm = messagebox.askyesno("Confirm", "Do you want to delete all tasks?")
    if confirm:
        listbox.delete(0, tk.END)

# ---------- Widgets ----------

# Entry Box
task_entry = tk.Entry(root, width=30, font=("Arial", 14),bg="red")
task_entry.pack(pady=10)

# Add Button
add_btn = tk.Button(
    root,
    text="Add Task",
    width=20,
    command=add_task,
    bg="red",      # background color
    fg="white",font = ("Arial", 12, "bold")
    
                # text color
)
add_btn.pack(pady=5)
# Listbox
listbox = tk.Listbox(root, width=35, height=10,bg="blue", font=("Arial", 12),activestyle="underline")
listbox.pack(pady=10)

# Delete Button
delete_btn = tk.Button(
    root,
    text="Deleted selected",width=20,command=delete_task,bg="red",fg="white",
    font=("Arial",12, "bold"), activebackground="dark red"
)
delete_btn.pack(pady=5)

# Delete All Button
delete_all_btn = tk.Button(
    root,
    text="Delete selected",width=20,command=delete_all,bg="red",
    fg="white",font=("Arial",12,"bold"),activebackground="dark red"
)
                           


delete_all_btn.pack(pady=5)

root.mainloop()