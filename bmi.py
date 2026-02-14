import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("BMI Calculator")

#entry
tk.Label(root,text ="weight(kg)").pack()
weightentry = tk.Entry(root)
weightentry.pack()
tk.Label(root,text ="hight(meters)").pack()
hightentry = tk.Entry(root)
hightentry .pack()
result_lable = tk.Label(root,text="")
result_lable.pack(pady=10)
def calculate_bmi():
    weight = float(weightentry.get())
    height = float(hightentry.get())

    bmi = weight / (height * height)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    result_label.config(
        text=f"BMI: {bmi:.2f}\nCategory: {category}"
    )

# Button
tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack()

root.mainloop()    
             
        
        

      


    
    
    