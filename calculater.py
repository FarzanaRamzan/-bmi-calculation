import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date

# Window
root = tk.Tk()
root.geometry("400x300")
root.title("Age Calculator")

# Input Labels
tk.Label(root, text="Enter your Date of Birth").pack(pady=5)

tk.Label(root, text="Year (YYYY)").pack()
year_entry = tk.Entry(root)
year_entry.pack()

tk.Label(root, text="Month (MM)").pack()
month_entry = tk.Entry(root)
month_entry.pack()

tk.Label(root, text="Day (DD)").pack()
day_entry = tk.Entry(root)
day_entry.pack()

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Function to calculate age
def calculate_age():
    try:
        y = int(year_entry.get())
        m = int(month_entry.get())
        d = int(day_entry.get())

        dob = date(y, m, d)
        today = date.today()

        if dob > today:
            messagebox.showerror("Error", "Date of birth cannot be in the future!")
            return

        # Calculate age in years
        age_years = today.year - dob.year
        age_months = today.month - dob.month
        age_days = today.day - dob.day

        if age_days < 0:
            age_months -= 1
            age_days += (date(today.year, today.month, 1) - date(today.year, today.month-1 if today.month>1 else 12, 1)).days

        if age_months < 0:
            age_years -= 1
            age_months += 12

        result_label.config(
            text=f"Age: {age_years} Years, {age_months} Months, {age_days} Days"
        )

    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Button
tk.Button(root, text="Calculate Age", command = calculate_age).pack(pady=10)

root.mainloop()
