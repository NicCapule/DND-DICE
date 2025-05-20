from tkinter import Tk
from ui import create_ui

def main():
    root = Tk()
    roll_function = create_ui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
