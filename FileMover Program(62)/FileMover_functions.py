#Author: Jordan Madrid
#Project: File Mover: I am getting text files moved from one folder to another, this is the second problem in a series. 
#OS: Tested on Windows 10
#Date: 11/14/2016

import shutil
import os
import time
import FileMover_main
import FileMover_gui
from tkinter import *

#Moving Files

def neworold(fullpath):
        fileAge = os.path.getmtime(fullpath)
        Cutoff = time.time() - 86400
        if fileAge > Cutoff:
            return True
        else:
            return False

def moveFiles(self):
    src = self.src.get()
    dst = self.dst.get()
    allfiles = os.listdir(src)
    for files in allfiles:
        fullpath = os.path.join(src, files)
        endpath = os.path.join(dst, files)
        if files.endswith(".txt") and neworold(fullpath):
            shutil.move(fullpath, dst)
            print(endpath)
        else:
            pass

##GUI

def sourceCall(self):
    sourcepath = filedialog.askdirectory()
    print (type(self.src))
    self.src.set(sourcepath)
    #return sourcepath

def destinationCall(self):
    destpath = filedialog.askdirectory()
    self.dst.set(destpath)
    #return destpath

def callback(self):
    moveFiles(self)
    
if __name__ == "__main__":
    pass
    
