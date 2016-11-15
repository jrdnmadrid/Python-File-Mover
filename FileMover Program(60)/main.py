#Author: Jordan Madrid
#Project: File Mover: I am getting text files moved from one folder to another. 
#OS: Tested on Windows 10
#Date: 11/14/2016

import shutil
import os
##import GUI



def movefiles(src,dst):
    allfiles = os.listdir(src)
    for files in allfiles:
        fullpath = os.path.join(src, files)
        endpath = os.path.join(dst, files)
        if files.endswith(".txt"):
            shutil.move(fullpath,dst)
            print(endpath)


def main():
    src = os.path.join('C:',os.sep, 'Users', 'jrdnm', 'DevelopmentProjects', 'TechAcademy_Python', 'Item 59-63 Drills', 'FileMover Program(60)', 'Folder A')
    dst = os.path.join('C:',os.sep, 'Users', 'jrdnm', 'DevelopmentProjects', 'TechAcademy_Python', 'Item 59-63 Drills', 'FileMover Program(60)', 'Folder B')
    movefiles(src,dst)
    
if __name__ == "__main__":
    main()
    
