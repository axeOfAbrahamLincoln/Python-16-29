from tkinter import *

window = Tk()
window.title("Mile To Km Converter")
window.minsize(width=400, height=150)
window.config(padx=100,pady=50)


#Labels
label_mi = Label(text = "Miles")
label_mi.grid(row=0, column=2)

label_km = Label(text="Km")
label_km.grid(row=1,column=2)

label_text = Label(text= "is equal to ")
label_text.grid(row=1,column=0)


label_result = Label(text= "0" ,bg="white",foreground= "Red",font=("Courier",14), width=10)
label_result.grid(row=1,column=1)
label_result.grid(padx=5, pady=20)

#button
def calculate():
    miles = float(input.get())
    result = round(miles * 1.60934,2)
    label_result.config(text=f"{result}")

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)
calculate_button.grid(pady=20)

#inputfield

input = Entry(width=9, fg= "Black", bg ="White", justify="right", insertbackground="black")
input.grid(row=0,column=1)








window.mainloop()

