from tkinter import *

#window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

#label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(row=0,column=0)

#button



def clicked():
    my_label["text"] = input.get() 
    

my_button = Button(text="Click Me", command=clicked)
my_button.grid(row=1, column=1)
my_button1 = Button(text="2nd Button")
my_button1.grid(row=0, column=2)
#entry

input = Entry(width=10)
input.grid(row=3, column=3)



window.mainloop()