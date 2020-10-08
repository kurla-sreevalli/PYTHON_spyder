# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:50:03 2020

@author: sreevalli kurla ksv
"""

#  FOR LOOP STATEMENT

book={"chap1":10,"chap2":20,"chap3":30}

#1st method
for key in book.keys():
    print(key)
    
#2nd method
for values in book.values():
    print(values)
    
#3rd method
for items in book.items():
    print(items)


#   (structured data)
colors = [
   {
     "colors": "red",
     "values": "#f00"
   },
   {
     "colors": "green",
     "values": "#0f0"
   },
   {
     "colors": "blue",
     "values": "#00f"
   },
   {
     "colors": "cyan",
     "values": "#0ff"
   },
   {
     "colors": "magenta",
     "values": "#f0f"
   },
   {
     "colors": "yellow",
     "values": "#ff0"
   },
   {
     "colors": "black",
     "values": "#000"
     }]


for item in colors:
    print(item['colors'],item['values'])

####################### (UNSTRUCTURED DATA)

data = {
"id": "0001",
"type": "donut",
"name": "Cake",
"image": {
"url": "images/0001.jpg",
"width": 200,
"height": 200
},
"thumbnail": {
"url": "images/thumbnails/0001.jpg",
"width": 32,
"height": 32
}
}

for key,value in data.items():
    if isinstance(value,str):
        print(key.ljust(30),":",values)
    elif isinstance(value,dict):
        for skey,svalue in value.items():
            ikey = key+(".")+skey
            print(ikey.ljust(30),":",svalue)



## ( worked on for loop with structured and unstructured data, and theory on types of operators)








