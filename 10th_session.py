# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:51:05 2020

@author: sreevalli kurla ksv
"""

# using csv library

import csv

#fobj can also be called as file object or file handler or file reference
cityset = set()
fobj = open("C:\\Users\\sreevalli kurla ksv\\Desktop\\realestate.csv","r")
#converting file object to csv object
reader= csv.reader(fobj)
#each line will be converted to list automatically
for line in reader:
    #adding each city to the set
    cityset.add(line[1])
for city in cityset:
    print((city))

fobj.close()


############    exception handling

try:
    filename=input("enter any filename:")
    fobj =open(filename,"r")
    
    for getline in fobj:
        #remove whitespaces
        getline=getline.strip()
        print(getline)
    fobj.close()
except FileNotFoundError as err:
    print("file not found error:",err)
except TypeError as err:
    print("invalid operation:",err)
except ValueError as err:
    print("invalid input:",err)
except (IndexError,ArithmeticError,IOError) as err:
    print("exception occured:",err)
except  Exception as err:
    print("unknown exception:",err)
else: 
    output="python" + "programming"
    print(output)
finally:
    print("this block will be executed all the times")
    


















