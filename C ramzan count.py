import tkinter as tk
root = tk.Tk()
root.geometry("400x300")
root.title(" countdown Timer ")
root.config(bg="blue")
#lable entry
tk.Label(root,text="enter target date time").pack(pady=5) 
#year_entry
tk.Label(root,text="year",bg="black",fg="white").pack()
year_entry = tk.Entry(root)
year_entry.pack()
#month_entry
tk.Label(root,text="month",bg="black",fg="white").pack(padx=5)
month_entry =tk.Entry(root)
month_entry .pack()
#day entry
tk.Label(root,text="day",bg="black",fg="white").pack(pady=5)
day_entry = tk.Entry(root)
day_entry .pack()
#hours_entry
tk.Label(root,text="hours",bg="black",fg="white").pack()
hours_entry = tk.Entry(root)
hours_entry.pack()
#minuts entry
tk.Label(root,text="minuts",bg="black",fg="white").pack(pady=5)
minuts_entry = tk.Entry(root)
minuts_entry .pack()
result_label = tk.Label(root,text="",font=("arial",12))
result_label.pack(pady=20)
def lates_counter():
    try:
        target = datetime(
            int(year_entry.get()),
            int(month_entry.get()),
            int(day_entry.get()),
            int(hours_entry.get()),
            int(minuts_entry.get()),

        )
        #calculation
        now = datetime.now()
        remaining = target - now
        if remaining.total_second() > 0:
            day = remaining.days
            second = remaining.seconds 
            hours = second // 3600
            minuts = (second % 3600) // 60
            second = second % 60 
            result_label.config(
                text=f"{days} days\n{hours} hours\n{minutes} minutes\n{seconds} seconds\n"
            )

            root.after(1000, lates_counter)
        else:
            result_label.config(text="Time's up!")

    except:
        result_label.config(text="Enter a valid time")

tk.Button (root, text ="Start Countdown", command = lates_counter,bg="lightyellow").pack(pady=10)
root.mainloop()

    


                
            
                












