#Author: Jordan Madrid
#Project: File Mover: I am getting text files moved from one folder to another, this is the second problem in a series. 
#OS: Tested on Windows 10
#Date: 11/14/2016

from tkinter import *
import tkinter as tk
import shutil
import os
import time
import FileMover_functions
import FileMover_gui

class FileMover():
        def __init__(self, master):
                self.master = master #I don't understand this. It makes self a class variable.
                self.master.minsize(400,150)
                self.master.maxsize(400,150)
                FileMover_functions.center_window(self, 400, 150)
                self.master.title("File Mover 2.0")
                self.src = StringVar()
                self.dst = StringVar()
                self.Modified = StringVar()
                FileMover_gui.load_gui(self)


if __name__ == "__main__":
        root = tk.Tk()
        filemover = FileMover(root) #What is this? It instantiates the thing. 
        root.mainloop()
