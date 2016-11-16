#Author: Jordan Madrid
#Project: File Mover: I am getting text files moved from one folder to another. I am building the UI in this challenge. 
#OS: Tested on Windows 10
#Date: 11/14/2016

from tkinter import *
from tkinter import ttk
import FileMover_main
import FileMover_functions


def load_gui (self):
    #Description of Tool
    description = ttk.Label(self.master, text = 'Please use Src button to select a folder to be scanned. Use the Dst button to select a folder for the new or modified files.')
    description.grid(row = 0, column = 0, columnspan = 3, pady=5)
    description.config(wraplength = 340)

    #Source file path field
    sourceField = ttk.Entry(self.master, width = 50, textvariable = self.master.var)
    sourceField.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)
    sourceField.insert(0, "Source Folder")
    sourceField.state(['readonly'])

    #Source Button
    sourceButton = ttk.Button(self.master, text = 'Browse Src')
    sourceButton.grid(row = 1, column = 2, padx=5)
    sourceButton.config(command = lambda: FileMover_functions.sourceCall(self.master.var))

    #Destination file path field
    destinationField = ttk.Entry(self.master, width = 50, textvariable= self.master.var1)
    destinationField.grid(row = 2, column = 0, columnspan = 2, padx=5, pady=5)
    destinationField.insert(0, "Destination Folder")
    destinationField.state(['readonly'])

    #Destination Button
    destinationButton = ttk.Button(self.master, text = 'Browse Dst')
    destinationButton.grid(row = 2, column = 2, padx=5)
    destinationButton.config(command = lambda: FileMover_functions.destinationCall(self.master.var1))

    #Move Button
    moveButton = ttk.Button(self.master, text = 'Check Files')
    moveButton.grid(row = 3, column = 1, pady=5)
    moveButton.config(command = lambda: FileMover_functions.callback(self))
    
if __name__ == "__main__":
    pass
    
