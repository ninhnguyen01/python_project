# Import Package
from tkinter import *

# Create root window
root = Tk()

# Root window title and dimension
root.title("Interface")
root.geometry('700x500')

# Adding menu bar in root window
# New item in menu bar labelled as 'New'
# Adding more items in the menu bar 
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

# Adding a label to the root window
lbl = Label(root, text = "Shield Status: Normal")
lbl.grid()

# Function to display text 
def clicked():
    lbl.configure(text = "Shield Status: Overcharged")

# Button widget with red color text 
btn = Button(root, text = "Charge Shield" ,
             fg = "blue", command=clicked)
# Set Button grid
btn.grid(column=1, row=0)

# Adding Entry Field
txt = Entry(root, width=10)
txt.grid(column=0, row=1)

# Function to display user text
def clicked():
    res = "Shield Status: Reset " + txt.get()
    lbl.configure(text = res)

# Button widget with red color text 
btn = Button(root, text = "Reset Shield" ,
             fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=1, row=1)

# Execute Tkinter
root.mainloop()