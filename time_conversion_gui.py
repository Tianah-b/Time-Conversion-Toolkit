import tkinter as tk
from tkinter import ttk
from helper import days_to_units, validate_and_execute

def convert():
    days = days_entry.get()
    unit = unit_var.get()
    days_and_unit_dictionary = {"days": days, "unit": unit}
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            result_label.config(text=calculated_value)
        elif user_input_number == 0:
            result_label.config(text="Please use a number above 0")
        else:
            result_label.config(text="Your input is a negative number")
    except ValueError:
        result_label.config(text="Your input is not valid!")


root = tk.Tk()
root.title("Time Conversion Utility")
root.geometry("300x200")

# Styling
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))

# Create and place widgets
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(expand=True, fill=tk.BOTH)

ttk.Label(main_frame, text="Enter number of days:", style="TLabel").pack()
days_entry = ttk.Entry(main_frame, style="TEntry")
days_entry.pack()

ttk.Label(main_frame, text="Select conversion unit:", style="TLabel").pack()
unit_var = tk.StringVar()
unit_var.set("hours")  # default value
units = {"hours", "minutes"}
unit_menu = ttk.OptionMenu(main_frame, unit_var, *units)
unit_menu.pack()

convert_button = ttk.Button(main_frame, text="Convert", command=convert, style="TButton")
convert_button.pack(pady=10)

result_label = ttk.Label(main_frame, text="Conversion Result", style="TLabel")
result_label.pack()


root.mainloop()
