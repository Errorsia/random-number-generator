import tkinter as tk
import r10s_logic
from r10s_gui import App

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root, r10s_logic)
    root.mainloop()
