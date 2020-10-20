# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 17:54:06 2020

@author: sreevalli kurla ksv
"""

#LAMBDA FUNCTION

#######singleline func.

def increment(x):
    return x+1
print(increment(10)) #11

######   LAMBDA FUNCTION (introduction and syntax)
#instead of writing single line func. can use lambda 
#using one object
filename = lambda x: x+1
print((filename(19)))

#using two objects
add=lambda x,y:x+y
print(add(10,20))

#regular way
def getupper(name):
    return name.upper()
print(getupper("python"))

#using lambda
getupper=lambda x:x.upper()
print(getupper("python"))


###############   LIBRARIES

#importing all methods
import math
print(math.floor(45.3))#lovwerbound number
print(math.ceil(45.3))#upperbound value

#importing methods as alias
import math as m
print(m.floor(45.3))#lovwerbound number
print(m.ceil(45.3))#upperbound value
print(m.tan(45))

#importing libraries from method
from math import floor,ceil,tan #no dot(.) operation required here
print(floor(46.78))
print(ceil(56.8765))
print(tan(30))




#before writing a program learning a set of methods and libraries


#how to display all the files of D:\ 
import os
print(os.listdir("D:\\"))

######display todays time and date
from datetime import date

today = date.today()
print("Today's date:", today)
#
import datetime
print(datetime.datetime.now())

#how to delete a file in python
import os
print(os.remove("D:\\Screenshot_2018-04-18-22-53-55-63.png"))

#how to copy a file from C:\ to D:\
import shutil #shell utilities
shutil.copy("C:\\Users\\sreevalli kurla ksv\\even_nums.txt","D://")

#how to display all the directories in C:\
import os
print(os.listdir("C:\\"))

#how to display 2020 calender
import calendar
print(calendar.calendar(2020))

#how to delete the directory
import os
os.rmdir("H:\\deletefolder")

#what library is used for connecting mysql database
import pymysql

#what library is used for connecting mongo database
import pymongo


















