import tkinter as tk
from tkcalendar import Calendar

def see_date():
    selected_date = cal.get_date()
    print("Selected Date is:", selected_date)  # This will print the date to the console, or you can use it as needed

# Create the main window
root = tk.Tk()
root.title('Calendar Example')

# Create a Calendar widget
cal = Calendar(root, selectmode='day', year=2023, month=4, day=1)
cal.pack(pady=20)

# Button to display selected date
btn = tk.Button(root, text="Show Date", command=see_date)
btn.pack(pady=20)

root.mainloop()
