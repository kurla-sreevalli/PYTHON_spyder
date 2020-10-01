# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:31:11 2020

@author: sreevalli kurla ksv
"""
##########string slicing
#syntax of string 
#string[start:stop:step]
name="python programming"
print(name)
print(name[0])
print(name[1])
print(name[0:4]) #only taking 0,1,2,3 index not considered 4th
print(name[3:6])
print(name[0:17])
print(name[4:]) #if nothing mentioned in stop then the last index is also considered
print(name[::]) #everything of string is considered with step as 1 by default
print(name[:]) #same as :: considered whole string
print(name[0:17:2]) #from 0 to 16 with difference of one letter(as we gave 2 as step) 
print(name[1:17:2])
print(name[::2])
print(name[::3])
print(name[-1]) #from right to left we consider from -1 to required index 
print(name[-2])
print(name[-3:-1])
print(name[::-1]) #printing the whole string from right to left


########### LIST (mutable/changable)
alist=[10,20,30,40] 
blist=['perl','hadoop','spark','scala']
clist=[34,5,45.4,"java","oracle","unix"]
 
print(alist)
print("elements are:",alist)
print("first element :",alist[0])
print(alist[0:3])
 
print(alist[::-1])
print(alist[-3:-1])
print(alist[1:3]) #range

print(alist[0])
alist[0]=1000
print("after modifying:", alist)

### iterating the list
print(alist)
for num in alist:
    print(num)

## syntax to get any specific range of numbers from a list by iteration
print(alist)
for num in alist[1:3]:
    print(num)



########################## TUPLE (immutable/unchangable)
atup=(45,5,34,5)
btup=('java','python','c')
ctup=(45,67,54.4,"hadoop",45)

print(atup)
print(btup)
print(ctup)

print("first element:", atup[0])
print("second element:", atup[1])

### iterating with for loop
for item in atup:
    print(item)
    
atup[0]=3000
print("after modifying:", atup) ## its not changable so it throws an error called TYPE ERROR

