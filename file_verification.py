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
import os

def openDirectory(variable, dirText="Select the folder where your files are located"):
    dirName = filedialog.askdirectory(parent=root, title=dirText)
    variable.set(str(dirName))

def findMissing(extension, local_loc, server_loc):
    # Need to create a new non-root window to display missing files (and option
    # to save the list)
    local_files = [file for file in os.listdir(local_loc) if file.endswith(extension)]
    server_files = [file for file in os.listdir(server_loc) if file.endswith(extension)]
    missing_file = [file for file in local_files if file not in server_files]

def findOverlap(extension, local_loc, server_loc):
    # Need to create a new non-root window to display overlap files (and option
    # to save, move, or delete the files)
    local_files = [file for file in os.listdir(local_loc) if file.endswith(extension)]
    server_files = [file for file in os.listdir(server_loc) if file.endswith(extension)]
    overlap_files = [file for file in local_files if file in server_files]

root = tk.Tk()
root.title("File Verification")
tk.Label(root, text="File extension:", anchor="e", justify="right").grid(sticky="e", row=1, column=0, padx=5, pady=5)
tk.Label(root, text="Location of local files:", anchor="e", justify="right").grid(sticky="e", row=2, column=0, padx=5, pady=5)
tk.Label(root, text="Location of server files:", anchor="e", justify="right").grid(sticky="e", row=3, column=0, padx=5, pady=5)
# Row 4 or 5 for buttons

e1default = tk.StringVar()
e2default = tk.StringVar()
e3default = tk.StringVar()

e1 = ttk.Combobox(root, textvariable=e1default, state='readonly', values=[".bdf", ".mat"], width=100).grid(row=1, column=1, columnspan=3)
e2 = tk.Entry(root, text=e2default, width=100, justify="left").grid(sticky="w", row=2, column=1, columnspan=3)
e3 = tk.Entry(root, text=e3default, width=100, justify="left").grid(sticky="w", row=3, column=1, columnspan=3)

e2_button = tk.Button(root, text="Choose Folder", command=lambda:openDirectory(e2default)).grid(row=2, column=4, padx=5)
e3_button = tk.Button(root, text="Choose Folder", command=lambda:openDirectory(e3default)).grid(row=3, column=4, padx=5)

missing = tk.Button(root, text="Missing Files", width=20).grid(row=4, column=1, columnspan=1, pady=4)
overlap = tk.Button(root, text="Overlapping Files", width=20).grid(row=4, column=2, columnspan=1, pady=4)
tk.Button(root, text="Close", command=root.destroy, width=20).grid(row=4, column=3, columnspan=1, pady=4)

root.mainloop()
