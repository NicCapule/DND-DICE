from tkinter import *
from tkinter import ttk
from logic import roll_die, format_log_entry, choice_conversion

dice_options = ["D4", "D6", "D8", "D10", "D12", "D20"]

def create_ui(root):
    root.resizable(False, False)
    root.title("DND Dice Machine")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    dice_choice = StringVar(value=dice_options[5])
    button_label = StringVar(value=f"Roll {dice_options[5]}")
    rolled = StringVar()

    def update_button_label(*args):
        button_label.set(f"Roll {dice_choice.get()}")

    def roll(*args):
        die, result = roll_die(dice_choice.get())
        rolled.set(result)
        entry = format_log_entry(die, result)
        logWindow.config(state='normal')
        logWindow.insert(END, entry)
        logWindow.see(END)
        logWindow.config(state='disabled')

    dice_choice.trace_add("write", update_button_label)

    # Layout widgets
    ttk.Label(mainframe, text="Choose Dice: ").grid(column=1, row=1, sticky=W)
    dropdown = OptionMenu(mainframe, dice_choice, *dice_options)
    dropdown.grid(column=2, row=1, sticky=W)

    ttk.Label(mainframe, text="Modifier: ").grid(column=1, row=2, sticky=W)
    ttk.Label(mainframe, text="Result: ").grid(column=1, row=4, sticky=W)
    ttk.Label(mainframe, textvariable=rolled).grid(column=2, row=4, sticky=(W, E))

    ttk.Button(mainframe, textvariable=button_label, command=roll).grid(column=2, row=5, sticky=W)

    ttk.Label(mainframe, text="Log Window: ").grid(column=3, row=1, sticky=W)
    logWindow = Text(mainframe, height=8, width=50, state='disabled')
    logWindow.grid(column=3, row=2, rowspan=3, sticky=W)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.bind("<Return>", roll)