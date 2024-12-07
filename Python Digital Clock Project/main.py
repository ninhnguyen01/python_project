# Import package
from tkinter import *
from tkinter.ttk import *
from time import strftime

# Creating window
root = Tk()
root.title('Digital Clock')

# Display time function
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

# Styling the label widget 
lbl = Label(root, font=('calibri', 40, 'bold'),
            background='black',
            foreground='green')

# Placing clock at the centre of the window
lbl.pack(anchor='center')

time()

mainloop()