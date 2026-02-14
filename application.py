import tkinter as tk
root= tk.Tk()
root.geometry("400x300")
root.title("my first bmi")
root.config(bg="purple")
#entry
tk.Label(root,text="weightentry(kg)").pack()
weightentry = tk.Entry(root)
weightentry.pack()
tk.Label(root,text="height (m)").pack()
heightentry = tk.Entry(root)
heightentry.pack()
resultlable = tk.Label(root,text="")
resultlable.pack(pady=10)
def calculate_bmi():
    weight = float(weightentry.get())
    height = float(heightentry.get())
    bmi = weight / (height*height)

    if bmi < 15.5:
        category="underweight"
    elif bmi < 30:
        category="normal"
    elif bmi < 40:
        category="over weight"
    else: 
        category="Obese"
        resultlable.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )
        
# Button
tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack()

root.mainloop()    
                    





    
        
     
        
