# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 12:22:40 2024

Attempting to create a more user-friendly file verification for .mat and .bdf
files.

NEXT:
    - Add buttons / functions for missing, overlapping files and quit (see
      schematic)

@author: Francis
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def openDirectory(variable, dirText="Select the folder where your files are located"):
    dirName = filedialog.askdirectory(parent=root, title=dirText)
    variable.set(str(dirName))

root = tk.Tk()
root.title("File Verification")
tk.Label(root, text="File extension:", anchor="e", justify="right").grid(sticky="e", row=1, column=0)
tk.Label(root, text="Location of local files:", anchor="e", justify="right").grid(sticky="e", row=2, column=0)
tk.Label(root, text="Location of server files:", anchor="e", justify="right").grid(sticky="e", row=3, column=0)
# Row 4 or 5 for buttons

e1default = tk.StringVar()
e2default = tk.StringVar()
e3default = tk.StringVar()

e1 = ttk.Combobox(root, textvariable=e1default, state='readonly', values=[".bdf", ".mat"], width=100).grid(row=1, column=1)
e2 = tk.Entry(root, text=e2default, width=100, justify="left").grid(sticky="w", row=2, column=1)
e3 = tk.Entry(root, text=e3default, width=100, justify="left").grid(sticky="w", row=3, column=1)

e2_button = tk.Button(root, text="...", command=lambda:openDirectory(e2default)).grid(row=2, column=2)
e3_button = tk.Button(root, text="...", command=lambda:openDirectory(e3default)).grid(row=3, column=2)

root.mainloop()
