# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 20:52:24 2020

@author: sreevalli kurla ksv
"""

#string object and its methods

name="python programming"
print(name.capitalize()) #firstletter will become uppercase
print(name.upper())
print(name.lower())
print(name.isupper())
print(name.islower())
print(name.isalpha())
print(name.center(40)) #default is space
print(name.center(40,"*"))
print(name.count('p'))
print(name.endswith('z'))
print(name.endswith('ing'))
print(name.replace("python","ruby"))

string="I love {} and {}"
print(string.format("python","hadoop"))
print(string.format("1","2"))
print(string.format("apple","mango"))
#delimeter seperation (that can be ':',' ',';',..any thing that seperates the string)
line="python:oracle:java:db"
print(line.split(":"))
line="python oracle java db"
print(line.split(" "))


##### LENGTH FUNCTION

name= "python"
print(" length of string:", len(name))

name= "    python    "
print("length of the string:", len(name))

name= name.strip() #will remove spaces at both the ends
print("length of the string:", len(name))



#####   LIST OBJECT AND IT'S METHODS

alist = [10,35,345,54,67]
# add an object to the list
alist.append(450)
print("after appending:", alist)
alist.append(681)
print("after appending:", alist)
getcount= alist.count(345)
print("total count of 345:", getcount) # gives, how many times a number is present in a list
# extend : passing a set of values ata time
alist.extend([109,200,561])
print("after extending:", alist)
print("get index of 109:", alist.index(109))
#list.insert(where to insert, what to insert)
#               position    , value
alist.insert(7,100) 
print("after inserting:", alist) 
#pop : removing the value at that specific index
alist.pop(9) #9 is the index
print("after pop operation:", alist)
# remove : we'll pass the exact value that which we want to remove
alist.remove(681) #681 is the element
print("after removing list:", alist)
# reverse the list
alist.reverse()
print("after reversing:", alist)
#sort : ascending order by default
alist.sort()
print("after sorting:", alist)
#sort : reverse=True for descending order
alist.sort(reverse=True)
print("after sorting:", alist)


######## TUPLE METHODS
        
atup= (10,60,50,20,30,50,70,30,90,20,30,40)
# only two methods i.e, index and count
atup.index(20) #20 is the value in tuple
print("index of the value:", atup.index(40))
atup.count(30)
print("count of the value:", atup.count(70))


####### DICTIONARY METHODS

adict={"chap1":10,"chap2":20,"chap3":30}
print(adict)
print(adict["chap1"])
# ONLY keys
print(adict.keys())
#ONLY values
print(adict.values())
#ONLY items : gives the list of tuples
print(adict.items())
# pop : to remove an item
adict.pop("chap1")
print("after pop function, output:", adict) #removes both key and value
#get : returns "NONE" if the given key to remove is not present in the dictionary
output= adict.get("chap5")
print(output)


####### SET OBJECT METHODS

aset= {20,10,30,500}
bset={50,657,450}
# UNION function
aset.union(bset)
# INTERSECTION func.
aset.intersection(bset)
# DIFFERENCE func.
aset.difference(bset)
# SUBSET func. : ***** Remember, if a function starts with 'IS' then it returns the boolean function values i.e, TRUE/FALSE
aset.issubset(bset)



#******* these are only a few practiced, but there are many more methods for each object ********
