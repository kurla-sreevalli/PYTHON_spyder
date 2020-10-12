# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 00:31:45 2020

@author: sreevalli kurla ksv
"""

########   ASSIGNMENT DISCUSSION 


ytag = {
  "kind": "youtube#searchListResponse",
  "etag": "m2yskBQFythfE4irbTIeOgYYfBU",
  "nextPageToken": "CAUQAA",
  "regionCode": "KE",
  "pageInfo": {
    "totalResults": 4249,
    "resultsPerPage": 5
  },
  "items": [
    {
      "kind": "youtube#searchResult",
      "etag": "m2yskBQFythfE4irbTIeOgYYfBU",
      "id": {
        "kind": "youtube#channel",
        "channelId": "UCJowOS1R0FnhipXVqEnYU1A"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "m2yskBQFythfE4irbTIeOgYYfBU",
      "id": {
        "kind": "youtube#video",
        "videoId": "Eqa2nAAhHN0"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "m2yskBQFythfE4irbTIeOgYYfB",
      "id": {
        "kind": "youtube#video",
        "videoId": "IirngItQuVs"
      }
    }
  ]
}


for key in ytag:
    if key=="etag":
        print(ytag[key])
    elif isinstance(ytag[key],list):
        for skey in ytag[key]:
            print(skey['etag'])

# (OR) to display all the keys and values 

# for key,values in ytag.items():
#     if isinstance(values,str):
#         print(key,values)
#     elif isinstance(values,dict):
#         for skey,svalue in values.items():
#             print(skey,svalue)
#         elif isinstance(values,list):
#             for inneritem in values:
#                 #print(inneritem)
#                 for skey,svalue in inneritem.items():
#                     print(skey,svalue)


# 7. Write a Python program to capture any filename from the keyboard and display its filename and extension separately.

"""
write a program to read some filename from the keyboard (customers.csv) and 

input: 
enter any filename: customers.csv

output: 
filename: custonmer
extension: csv

"""

filename=input("enter any filename:")
print("you entered:",filename)
output=filename.split(".")
print(output)

print("filename:", output[0])
print("extension:", output[1])

###########
#write a program to remove the duplicates from the list
#output:[10,20,30,40]
alist=[10,10,10,20,30,40,40,40]
aset=set(alist)
print(list(aset))

# or in a single line
print(list(set(alist)))

#############

alist=[10,10,10,20,30]
blist=[30,40,50,50,50]
#write a program to display
#-all unique elements of both alist and blist
#- common elements of both alist and blist

aset=set(alist)
bset=set(blist)

res = list(set(alist+blist))
res.sort() # if to display list in ascending order
print(res)

# intersection()
list(set(alist).intersection(blist))

#for common element of two lists
if (aset & bset):
    print(list(aset & bset))
else:
    print("no common elements")

#############

# 41. Write a Python program to display the below IP addresses

# 192.168.0.1
# 192.168.0.2
# 192.168.0.3
# ..
# ..
# 192.168.0.10

#concantenation happens with same object
fixed="192.168.0."
for val in range(1,11):
    ip=fixed+str(val)
    print(ip)

########### task 38

#Define some list as below

alist = ["google","oracle","microsoft"]

for item in alist:
    otpt="http://www."+item+".com"
    print(otpt)
    
"""
Output:
http://www.google.com
http://www/.oracle.com
http://www.microsoft.com
"""


"""
24. Write a Python program to capture filename from the keyboard and display the type of the file

if the filename is ending with .py …. display “Its python file”
if the filename is ending with .pl …. display “Its perl file”
If the filename is ending with .c … display “Its C lang file”
if the filename is ending with .json … display “Its json file”
"""

FILEname= input("enter any file name:")
print("you entered:",FILEname)
if FILEname.endswith(".py"):
    print("Its python file")
elif FILEname.endswith(".pl"):
    print("Its perl file")
elif FILEname.endswith(".c"):
    print("Its C lang file")
elif FILEname.endswith(".json"):
    print("Its json file")
else:
    print("unknown format")






