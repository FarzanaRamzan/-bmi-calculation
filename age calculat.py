import tkinter as tk 
#window
root= tk.Tk()
root.geometry("400x300",)
root.title("age calculate")
root.config(bg="indigo")
#lable defind
tk.Label(root,text="enter yuor date of birth").pack(pady=10) 
tk.Label(root,text="year(yyy)").pack()
yearentry=tk.Entry(root)
yearentry.pack()
tk.Label(root,text="month(mm)").pack()
monthentry=tk.Entry(root)
monthentry.pack()
tk.Label(root,text="day(dd)").pack()
dayentry = tk.Entry(root) 
#result defind
result_lable=tk.Label(root,text="",font=("arial",12))
result_lable.pack(padx=10)
#age defind
def Calculate_age(): 
    print("working...")
    try:
        y = int(yearentry.get())
        m = int(monthentry.get())
        d = int(dayentry.get())
        dob = date(y, m, d)
        today = date.today()
        if dob > today:
            
            messagebox.showerror("error",  "date of birth cannot be in the future")
            return
        #Calculate_age in year
        age_year = today.year - dob.year
        age_month = today.month - dob.month
        age_day   = today.day - dob.day
        if age_day <0:
            age_month -=1
            age_days += (date(today.year, today.month, 1) - date(today.year, today.month-1 if today.month>1 else 12, 1)).days
            if age_month < 0:
                age_year -=1
                age_month += 12
                result_lable.config(
                    text=f"age:{age_year}year,{age_month},month{age_days}day"
                )
    except: 
        message.showerror("Error", "Please enter valid numbers!")

# Button
tk.Button(root, text="Calculate Age", command = Calculate_age).pack(pady=10)

root.mainloop()

            





            




        

       
            


        
        
        

        






