import tkinter as tk
root = tk.Tk()
root.title("grading marks")
root.geometry("400x300") 
root.config(bg="black") 
 #entry
tk.Label(root,text="enter marks(0-100)").pack(pady=10)
marks_entry = tk.Entry()
marks_entry.pack() 
#lable for result
result_lable= tk.Label(root,text="")
result_lable.pack(pady=10)
def gradeing_marks():
    
    try:
        if marks_entry > 100 or marks_entry < 0:
        
            tk.label.config(text="Inter valide marks(0-100)")
            return
        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks>= 50:
            grade = "E"
        else:grade = "F"
        result_label.config (text=f"grade:{grade}")
    except ValueError: 
        tk.Label(root,text="enter marks").pack(pady=10)
        marks_entry = tk.entry(root)
        marks_entry.pack()
tk.Button(root, text="Calculate Grade", command=calculate_grade).pack(pady=10)

root.mainloop()
  
         
             




    