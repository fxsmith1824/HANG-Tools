# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 12:22:40 2024

Attempting to create a more user-friendly file verification for .mat and .bdf
files.

NEXT:
    - Add buttons / functions for missing, overlapping files (see schematic)
    to basically save a list or potentially move/delete local files?

@author: Francis
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

def openDirectory(variable, dirText="Select the folder where your files are located"):
    dirName = filedialog.askdirectory(parent=root, title=dirText)
    variable.set(str(dirName))

def saveItems(items, file_name):
    with open(file_name, 'w') as f:
        for item in items:
            f.write(f"{item}\n")

def findMissing(extension, exp, local_loc, server_loc):
    if len(exp) > 0:
        file_name = exp + '_' + extension.strip('.') + '_MissingFiles.txt'
    else:
        file_name = 'NoExpTag_' + extension.strip('.') + '_MissingFiles.txt'
    local_files = [file for path, subdirs, files in os.walk(local_loc) for file in files if file.endswith(extension) and exp in file]
    server_files = [file for path, subdirs, files in os.walk(server_loc) for file in files if file.endswith(extension) and exp in file]
    missing_files = [file for file in local_files if file not in server_files]
    
    missing = tk.Toplevel(root)
    missing.title("Files Missing on Server")
    miss_list = tk.Text(missing, width=50)
    miss_list.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
    if len(missing_files) > 0:
        for item in missing_files:
            miss_list.insert(tk.END, item+"\n")
    else:
        miss_list.insert(tk.END, "No local files missing from server")
    miss_save = tk.Button(missing, text="Save as Text", command=lambda:saveItems(missing_files, file_name))
    miss_save.grid(row=1, column=0, pady=4)
    miss_close = tk.Button(missing, text="Close", command=missing.destroy, width=10)
    miss_close.grid(row=1, column=2, pady=4)
    
    missing.mainloop()

def findOverlap(extension, exp, local_loc, server_loc):
    # Need to create a new non-root window to display overlap files (and option
    # to save, move, or delete the files)
    if len(exp) > 0:
        file_name = exp + '_' + extension.strip('.') + '_OverlapFiles.txt'
    else:
        file_name = 'NoExpTag_' + extension.strip('.') + '_OverlapFiles.txt'
    local_files = [file for path, subdirs, files in os.walk(local_loc) for file in files if file.endswith(extension) and exp in file]
    server_files = [file for path, subdirs, files in os.walk(server_loc) for file in files if file.endswith(extension) and exp in file]
    overlap_files = [file for file in local_files if file in server_files]
    
    overlap = tk.Toplevel(root)
    overlap.title("Files on both Local and Server")
    over_list = tk.Text(overlap, width=50)
    over_list.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
    if len(overlap_files) > 0:
        for item in overlap_files:
            over_list.insert(tk.END, item+"\n")
    else:
        over_list.insert(tk.END, "No overlapping files between local and server")
    over_save = tk.Button(overlap, text="Save as Text", command=lambda:saveItems(overlap_files, file_name))
    over_save.grid(row=1, column=0, pady=4)
    over_close = tk.Button(overlap, text="Close", command=overlap.destroy, width=10)
    over_close.grid(row=1, column=2, pady=4)
    
    overlap.mainloop()
    # return overlap_files

root = tk.Tk()
root.title("File Verification")
e1_label = tk.Label(root, text="File extension:", anchor="e", justify="right").grid(sticky="e", row=1, column=0, padx=5, pady=5)
e2_label = tk.Label(root, text="Experiment Tag:", anchor="e", justify="right").grid(sticky="e", row=2, column=0, padx=5, pady=5)
e3_label = tk.Label(root, text="Location of local files:", anchor="e", justify="right").grid(sticky="e", row=3, column=0, padx=5, pady=5)
e4_label = tk.Label(root, text="Location of server files:", anchor="e", justify="right").grid(sticky="e", row=4, column=0, padx=5, pady=5)
# Row 4 or 5 for buttons

e1default = tk.StringVar()
e2default = tk.StringVar()
e3default = tk.StringVar()
e4default = tk.StringVar()

e1 = ttk.Combobox(root, textvariable=e1default, state='readonly', values=[".bdf", ".mat"], width=100).grid(row=1, column=1, columnspan=3)
e2 = tk.Entry(root, text=e2default, width=100, justify="left").grid(sticky="w", row=2, column=1, columnspan=3)
e3 = tk.Entry(root, text=e3default, width=100, justify="left").grid(sticky="w", row=3, column=1, columnspan=3)
e4 = tk.Entry(root, text=e4default, width=100, justify="left").grid(sticky="w", row=4, column=1, columnspan=3)

e3_button = tk.Button(root, text="Choose Folder", command=lambda:openDirectory(e3default)).grid(row=3, column=4, padx=5)
e4_button = tk.Button(root, text="Choose Folder", command=lambda:openDirectory(e4default)).grid(row=4, column=4, padx=5)

missing = tk.Button(root, text="Missing Files", command=lambda:findMissing(e1default.get(),e2default.get(),e3default.get(),e4default.get()), width=20)
missing.grid(row=5, column=1, columnspan=1, pady=4)
overlap = tk.Button(root, text="Overlapping Files", command=lambda:findOverlap(e1default.get(),e2default.get(),e3default.get(),e4default.get()), width=20)
overlap.grid(row=5, column=2, columnspan=1, pady=4)
tk.Button(root, text="Close", command=root.destroy, width=20).grid(row=5, column=3, columnspan=1, pady=4)

root.mainloop()
