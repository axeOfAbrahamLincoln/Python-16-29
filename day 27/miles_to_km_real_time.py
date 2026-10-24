"""
Miles to Kilometers Converter

A simple GUI application built with Tkinter that converts miles to
kilometers in real time as the user types into the input field.
"""

from tkinter import *

# ----------------------------
# Window setup
# ----------------------------

window = Tk()
window.title("Mile To Km Converter")
window.minsize(width=400, height=150)

# Add padding around the window content
window.config(padx=100, pady=50)


# ----------------------------
# Labels
# ----------------------------

# Label showing the unit "Miles"
label_mi = Label(text="Miles")
label_mi.grid(row=0, column=2)

# Label showing the unit "Km"
label_km = Label(text="Km")
label_km.grid(row=1, column=2)

# Text label describing the conversion
label_text = Label(text="is equal to")
label_text.grid(row=1, column=0)

# Label where the calculated result will appear
label_result = Label(
    text="0",
    bg="white",
    foreground="Red",
    font=("Courier", 14),
    width=10
)
label_result.grid(row=1, column=1)
label_result.grid(padx=5, pady=20)


# ----------------------------
# Conversion function
# ----------------------------

def calculate(*args):
    """
    Convert miles to kilometers and update the result label.
    Runs automatically when the Entry content changes.
    """
    try:
        miles = float(input_var.get())
        result = round(miles * 1.60934, 2)
        label_result.config(text=f"{result}")
    except ValueError:
        label_result.config(text="0")

# ----------------------------
# Real-time input tracking
# ----------------------------

# StringVar stores the Entry value and allows change tracking
input_var = StringVar()

# Trigger the calculate function whenever the Entry text changes
input_var.trace_add("write", calculate)


# ----------------------------
# Input field
# ----------------------------

# Entry widget where the user types miles
miles_entry = Entry(
    width=9,
    textvariable=input_var,
    fg="Black",
    bg="White",
    justify="right",
    insertbackground="black"
)

miles_entry.grid(row=0, column=1)


# ----------------------------
# Start the GUI event loop
# ----------------------------

window.mainloop()