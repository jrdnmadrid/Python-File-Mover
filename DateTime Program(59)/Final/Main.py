# Python: 3.5.2
#
#Author: Jordan Madrid
#
# Project: I am building a program that will evaluate the time 
# differences between Portland, Oregon, New York, New York and London, England.
# Then, I am comparing to see if the 3 imaginary business branches are open or closed
# between 9am-9pm PDT.
#
# OS: I used Windows 10 to build and test this program. 

import datetime
from datetime import time
import pytz
from Branches import *

##### First, I need to create the Portland, Oregon time
##def portlandTime():
##    currentTime = datetime.datetime.now(pytz.timezone('US/Pacific')).strftime("%I:%M:%S %p")
##    print (currentTime)
##
#### We will create a function that is New York time
##def newyorkTime():
##    currentTime = datetime.datetime.now(pytz.timezone('US/Eastern')).strftime("%I:%M:%S %p")
##    print (currentTime)
##
##
#### We will create a function that is London Time
##def londonTime():
##    currentTime = datetime.datetime.now(pytz.timezone('Europe/London')).strftime("%I:%M:%S %p")
##    print (currentTime)



def getBranchDateTime(timeZone):
    return datetime.datetime.now(pytz.timezone(timeZone))

def timechange(mytime):
    mytime = time(mytime.hour,mytime.minute)
    return (mytime)

def openclose(branchDateTime, name):
    branchTime = timechange(branchDateTime)
    openingTime = datetime.time(9,0)
    closingTime = datetime.time(21,0)
    if branchTime >= openingTime and branchTime <= closingTime:
        print (name + " office is currently open")
    else:
        print (name + " office is currently closed")

def main():
    for branch in Branches:
        name = branch
        timezone = branches[branch]
        dt = getBranchDateTime(timezone)
        openclose(dt, name)
##
##def main():
##    newLondonTime = timechange(londonTime)
##    newnewYorkTime = time(newYorkTime.hour,newYorkTime.minute)
##    openingTime = datetime.time(9,0)
##    closingTime = datetime.time(21,0)
##    print("Time in Portland is:", portlandTime.strftime("%I:%M:%S %p"))
##    if newLondonTime > openingTime and newLondonTime < closingTime:
##        print("The London office is Open")
##    else:
##        print("The London office is Closed")
##    if newnewYorkTime > openingTime and newnewYorkTime < closingTime:
##        print( "The New York office is Open")
##    else:
##        print("The New York office is Closed")
##    
if __name__ == "__main__":
    # execute only if run as a script
    main()   
