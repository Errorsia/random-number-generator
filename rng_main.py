# -*- coding: utf-8 -*-
# Author: Ariskanyaa <Ariskanyaa@outlook.com>
# Author: Errorsia <Errorsia@outlook.com>
# License: GPL v3

# Version 10.0

import tkinter as tk
import rng_logic
from rng_gui import App

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root, rng_logic)
    root.mainloop()
