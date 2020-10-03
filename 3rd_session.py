# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 19:41:41 2020

@author: sreevalli kurla ksv
"""

####################### DICTIONARY
book = {"chap1": 10, "chap2": 20, "chap3":30}

print(book)
print(book["chap1"])
print(book["chap2"])
print(book["chap3"])

book = {"chap1": 10, "chap2": 20, "chap3":30, "chap1":1000}
#______if the key is repeated, it will take the latest value______
print(book["chap1"])

#some more examples where strings, lists and dictionaries include in dictionary
info={"chap1":[10,'Rita','US'], "chap2":[20,'Gita', 'UK'], "chap3":[30,'Paul','AUS']} #dictionary of lists
print(info)
print(info["chap1"])
print(info["chap2"])
print(info["chap3"])




#####____dictionary of dictionaries____#####

################## SAMPLE JSON (storing a data in exmple XML format) EXAMPLE
data= {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}


print(data['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossTerm'])
#### when we update new value it takes the latest value given
data['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossTerm']= "new language"
print(data['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossTerm'])
print(data)

#to get the below output
print(data['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['para'])
#A meta-markup language, used to create markup languages such as DocBook.





###____just trying to replace and get the output
#data['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossTerm']= "standard generalized markup language"
#print(data['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossTerm'])
#print(data)

#data['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossTerm']= "A meta-markup language, used to create markup languages such as DocBook"
#print(data['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossTerm'])
#print(data)




#### EXAMPLES ######
DATANEW={"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}

print(DATANEW['menu']['popup']['menuitem'][0]['value'])




#####____ SET______#####
# unordered collection of unique elements of same type
aset={10,10,10,10,20,20,20,30,30,30}
print(aset)
#{10, 20, 30}