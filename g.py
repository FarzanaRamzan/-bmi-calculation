import tkinter as tk

root = tk.Tk()
root.title("Grading Marks")
root.geometry("400x300")

# Entry for marks
tk.Label(root, text="Enter Marks (0-100)").pack(pady=10)
marks_entry = tk.Entry(root)
marks_entry.pack(pady=5)

# Label to show result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Function to calculate grade
def calculate_grade():
    try:
        marks = int(marks_entry.get())
        if marks > 100 or marks < 0:
            result_label.config(text="Enter valid marks (0-100)")
            return
        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 50:
            grade = "E"
        else:
            grade = "F"
        result_label.config(text=f"Grade: {grade}")
    except ValueError:
        result_label.config(text="Please enter a number!")

# Button to calculate
tk.Button(root, text="Calculate Grade", command=calculate_grade).pack(pady=10)

root.mainloop()