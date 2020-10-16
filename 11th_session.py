# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:49:39 2020

@author: sreevalli kurla ksv
"""
# BLOG examples (EXCEPTION HANDLING IN PYTHON)
print("exception handling demo")
print("------------------------")
i = int(input("Enter fno :"))
j = int(input("Enter sno :"))
try:
    k = i/j
    print(k)
except ZeroDivisionError as error:
    print("second value cannot be zero")
    print("System defined error :", error)
    
    

###########

print("exception handling demo")
print("------------------------")
try:
    i = int(input("Enter first number  :"))
    j = int(input("Enter second number :"))
    k = i/j
    print(k)
except ZeroDivisionError as error:
    print("second value cannot be zero")
    print("System defined error :", error)
except ValueError as error:
    print("please enter string values ")
    print("System defined error :", error )
    

###########

# nested try block demonstration
 
try:
    print("In try block 1")
    try:
        print("In try block 2")
        try:
            print("In try block 3")
        except:
            print("In except block 3")
    except:
        print("In except block 2")
except:
    print("In except block 1")




#######    USER DEFINED FUNCTIONS 

###      PASSING ARGUMENTS

# 1. fixed arguments
def display(a,b):
    print(a.b)
    
display(10,20,30)

def display(a,b,c):
    #always fixed in length
    print(a.b)
    
display(10,20)
#
list(range((10)))#by default it takes range from 1 to 10 with step of 1 (default), so it displays 1to9 values.


# 2. default arguments
def display(a=0,b=1,c=2):
    print(a,b,c)
display() #by default it takes the given values in defination line 

#so many examples where  the default is used like list and range... etc

#valiable length arguments
# if we want to pass multiple values the prefix the object with '*'.
#if any object is prefixed with * it becomes a TUPLE
def display(*values):
    #print values
    for val in values:
        print(val)

display(10,27,47,37,86,3456,76483,89,8765)

#######singleline func.

def increment(x):
    return x+1
print(increment(10)) #11

######   LAMBDA FUNCTION (introduction and syntax)
#instead of writing single line func. can use lambda 
filename = lambda x: x+1
print((filename(19)))












