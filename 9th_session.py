# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 19:07:54 2020

@author: sreevalli kurla ksv
"""
#reading file with readlines()
#output is list format
#
find= open("program.txt","r")
print(find.readlines())
find.close()

# reading file with read()
# not preffered much
find= open("program.txt","r")
print(find.read())
find.close()

# to create empty file use write mode
findx= open("programming.txt","w")

find.close()

# realestate csv example
#read all lines or records all lines
find= open("C:\\Users\\sreevalli kurla ksv\\Desktop\\realestate.csv","r")
print(find.readlines())
find.close()

# read only street and city
find= open("C:\\Users\\sreevalli kurla ksv\\Desktop\\realestate.csv","r")
for newfile in find:
    #remove white spaces
    newfile=newfile.strip()
    output= newfile.split(",")
    print("street:", output[0])
    print("city:", output[1])
    print("----------------------------")

find.close()
# (OR)
find= open("C:\\Users\\sreevalli kurla ksv\\Desktop\\realestate.csv","r")
for newfile in find:
    #remove white spaces
    newfile=newfile.strip()
    print("----------------------------")
    print(newfile.split(",")[0:2])
    
    
find.close()

# read unique cities
find= open("C:\\Users\\sreevalli kurla ksv\\Desktop\\realestate.csv","r")
cityset= set()    
#processing the data
for getlines in find:
    getlines=getlines.strip()
    output = getlines.split(",")
    city = output[1]
    #adding each city to set to capture unique city
    cityset.add(city)

#display output
for city in cityset:
    print((city))
find.close()

#program to display records containing SACRAMENTO

find= open("C:\\Users\\sreevalli kurla ksv\\Desktop\\realestate.csv","r")
for newfile in find:
    newfile=newfile.strip()
    output= newfile.split(",")
    if output[1]=="SACRAMENTO":
        print(output[0:12])
    else:
        print("None")
        
find.close()
    
# FOR JUST DISPLAYING SACRAMENTO WITHOUT NONE

find= open("C:\\Users\\sreevalli kurla ksv\\Desktop\\realestate.csv","r")
for newfile in find:
    newfile=newfile.strip()
    output= newfile.split(",")
    print("street:", output[0])
    print("city:", output[1])
    print("zip:", output[2])
    print("state:", output[3])
    print("beds:", output[4])
    print("baths:", output[5])
    print("sq__ft:", output[6])
    print("type:", output[7])
    print("sale_date:", output[8])
    print("price:", output[9])
    print("latitude:", output[10])
    print("longitude:", output[11])
    if output[1]=="SACRAMENTO":
        print("----------------------------")
        print(output[0:12])
find.close()


# FOR JUST DISPLAYING SACRAMENTO WITHOUT NONE

find= open("C:\\Users\\sreevalli kurla ksv\\Desktop\\realestate.csv","r")
for newfile in find:
    newfile=newfile.strip()
    output= newfile.split(",")
    if output[1]=="SACRAMENTO":
        print("----------------------------")
        print(output[0:12])
find.close()







