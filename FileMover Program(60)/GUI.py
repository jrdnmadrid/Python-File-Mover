#Author: Jordan Madrid
#Project: File Mover: I am getting text files moved from one folder to another. 
#OS: Tested on Windows 10
#Date: 11/14/2016

from tkinter import *
from tkinter import ttk
import main

root = Tk()
root.wm_title("File Mover Program")

#Window placement
root.geometry('280x60')
#Label
label = ttk.Label(root, text = 'Please click the button to move files to Folder B')
label.pack()
label.config(wraplength = 150)


#Button
button = ttk.Button(root, text = 'Move Files')
button.pack()
def callback():
    main.movefiles()
button.config(command = callback)
