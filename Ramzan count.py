import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.geometry("400x350")
root.title("Colorful Countdown Timer")
root.config(bg="#1e1e2f")   # Window background color

title_label = tk.Label(
    root,
    text="Countdown Timer",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="cyan"
)
title_label.pack(pady=10)

# Entry Labels
def create_label(text):
    tk.Label(root, text=text, bg="#1e1e2f", fg="white",
             font=("Arial", 10)).pack()

create_label("Year")
year_entry = tk.Entry(root, bg="lightyellow")
year_entry.pack()

create_label("Month")
month_entry = tk.Entry(root, bg="lightyellow")
month_entry.pack()

create_label("Day")
day_entry = tk.Entry(root, bg="lightyellow")
day_entry.pack()

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#1e1e2f",
    fg="lime"
)
result_label.pack(pady=20)


def update_countdown():
    try:
        
        target = datetime(
            int(year_entry.get()),
            int(month_entry.get()),
            int(day_entry.get())
        )

        now = datetime.now()
        remaining = target - now

        if remaining.total_seconds() > 0:
            days = remaining.days
            seconds = remaining.seconds

            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            secs = seconds % 60

            result_label.config(
                text=f"{days} Days {hours} Hours\n{minutes} Minutes {secs} Seconds"
            )
            root.after(1000, update_countdown)
        else:
            result_label.config(text="Time's Up!")

    except:
        result_label.config(text="working")
        result_label.config(text="Enter Valid Date")


tk.Button(
    root,
    text="Start Countdown",
    command=update_countdown,
    bg="orange",
    fg="black",
    font=("Arial", 12, "bold")
).pack(pady=10)

root.mainloop()
