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
import sqlite3
from math import ceil

#Center Window

def center_window(self, w, h):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width/2) - (w/2))
        y = int((screen_height/2) - (h/2))
        centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
        return centerGeo

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


def dataStorage(self):
        src = self.src.get()
        dst = self.dst.get()
        timestamp = time.time()
        conn = sqlite3.connect('db_FileMover.db')
        with conn:
                c = conn.cursor()
                c.execute("""INSERT INTO tbl_FileMover(col_timestamp,col_source,col_destination) VALUES (?,?,?)""", (timestamp,src,dst))
                conn.commit()
        conn.close()

##GUI

def sourceCall(self):
    sourcepath = filedialog.askdirectory()
    self.src.set(sourcepath)
    #return sourcepath

def destinationCall(self):
    destpath = filedialog.askdirectory()
    self.dst.set(destpath)
    #return destpath

def callback(self):
    moveFiles(self)
    dataStorage(self)
    
##Database

def create_db(self):
        conn = sqlite3.connect('db_FileMover.db')
        with conn:
                c = conn.cursor()
                c.execute("""CREATE TABLE if not exists tbl_FileMover(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                        col_timestamp INT, 
                        col_source STR, 
                        col_destination STR 
                        );""")
                conn.commit()
        conn.close()
        first_run(self)

def first_run(self):
        conn = sqlite3.connect('db_FileMover.db')
        with conn:
                c = conn.cursor()
                c,count = count_records(c)
                if count < 1:
                        c.execute("""INSERT INTO tbl_FileMover(col_timestamp,col_source,col_destination) VALUES (?,?,?)""", ('1479343769','',''))
                        conn.commit()
        conn.close()

def count_records(c):
        count = ""
        c.execute("""SELECT COUNT(*) FROM tbl_FileMover""")
        count = c.fetchone()[0]
        return c,count



if __name__ == "__main__":
    pass
