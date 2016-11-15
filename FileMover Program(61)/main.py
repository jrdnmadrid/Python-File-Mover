#Author: Jordan Madrid
#Project: File Mover: I am getting text files moved from one folder to another, this is the second problem in a series. 
#OS: Tested on Windows 10
#Date: 11/14/2016

import shutil
import os
import time
##import GUI


def neworold(fullpath):
        fileAge = os.path.getmtime(fullpath)
        Cutoff = time.time() - 86400
        if fileAge > Cutoff:
            return True
        else:
            return False

def moveFiles(src,dst):
    allfiles = os.listdir(src)
    for files in allfiles:
        fullpath = os.path.join(src, files)
        endpath = os.path.join(dst, files)
        if files.endswith(".txt") and neworold(fullpath):
            shutil.move(fullpath,dst)
            print(endpath)
        else:
            pass


def main():
    src = os.path.join('C:',os.sep, 'Users', 'jrdnm', 'DevelopmentProjects', 'TechAcademy_Python', 'Item 59-63 Drills', 'FileMover Program(61)', 'NeworModified')
    dst = os.path.join('C:',os.sep, 'Users', 'jrdnm', 'DevelopmentProjects', 'TechAcademy_Python', 'Item 59-63 Drills', 'FileMover Program(61)', 'Destination')
    moveFiles(src,dst)
    
if __name__ == "__main__":
    main()
    

