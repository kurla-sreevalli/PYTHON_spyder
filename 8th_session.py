# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:02:49 2020

@author: sreevalli kurla ksv
"""
#oepning a file
file = open("customers.txt","w")
#working with flat files(only writable)
file.write("python proggramming\n")
#closing a file
file.close()

#changing the path as, open("D:\\path\text\customers.txt")
file = open("D:\\customers.txt","w")
file.write("python proggramming\n")

file.close()


file = open("D:\\customers.txt","r")
file.write("python proggramming\n")

file.close()

"""
#write 1-100 numbers in a file display

file = open("numbers.txt","w")

for val in range(1,101):
    file.write(str(val)+"/n") ### ****** OBJECT SHOULD BE OF SAME TYPE, IF DIFF TYPE CONVERT USING STR() FUNCTION
    
    
#file.write("python proggramming\n")

file.close()
"""

fobg=open("nums.txt","w")

for val in range(1,101):
    fobg.write(str(val) + "\n")

fobg.close()

# write a program to capture your name from the keyboard and write he output to the file

name= open("yourname.txt","w")
display= input("enter name:")
name.write(display)
name.close()

# reverse the string python programming

string= open("rev_odr.txt","w")
order= "python programming"

for revodr in order[::-1]:
    string.write(revodr)
# reverseorder=print(str(order[::-1]))
# string.write(reverseorder)
string.close()

# odd numbers from 100 to 1 with diff. of 1 number [(-2) in reverse order]
fobg=open("odd_nums.txt","w")

for val in range(101,0,-2):
    fobg.write(str(val) + "\n")

fobg.close()

## even  numbers from 100 to 1 with diff. of 1 number (-2) in reverse order
fobj=open("even_nums.txt","w")

for num in range(100,0,-2):
    fobj.write(str(num) + "\n")

fobj.close()

############ READ OPERATION 

readop= open("nums.txt","r")
for sof in readop:
    print(sof)

readop.close()

# to strip or remove spaces in b/w numbers printed
readop= open("nums.txt","r")
for sof in readop:
    sof= sof.strip()
    print(sof)



readop.close()











