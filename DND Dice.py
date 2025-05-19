import random
from tkinter import * 
from tkinter import ttk

dice_options = [
   "D4", 
   "D6", 
   "D8", 
   "D10", 
   "D12", 
   "D20"
]

root = Tk()
root.title("DND Dice Machine")

mainframe = ttk.Frame(root, padding=" 3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky =(N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

# Dropdown Menu for the Dice Choices
dice_choice = StringVar(mainframe)
dice_choice.set(dice_options[5]) # default value

dropdown = OptionMenu(mainframe, dice_choice, *dice_options)
dropdown.grid(column=2, row=1, sticky=W)

# Dynamically change roll button on dropdown selection change
button_label = StringVar()
button_label.set(f"Roll {dice_options[5]}")
def update_button_label(*args):
    button_label.set(f"Roll {dice_choice.get()}")

# Dropdown change event listener
dice_choice.trace_add("write", update_button_label)

#roll dice based on dropdown choice
rolled = StringVar()
def roll(*args):
   die = choice_conversion()
   sides = die
   rolled.set(random.randint(1,sides))

# Convert dice_choice to integer and remove "D"
def choice_conversion():
    choice = dice_choice.get().replace("D","")
    int_choice = int(choice)
    return int_choice

ttk.Button(mainframe, textvariable=button_label, command=roll).grid(column=2, row=3, sticky=W)

ttk.Label(mainframe, textvariable=rolled).grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Choose Dice: ").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Result: ").grid(column=1, row=2, sticky=W)


for child in mainframe.winfo_children():
   child.grid_configure(padx = 5, pady = 5)

root.bind("<Return>", roll)

root.mainloop()