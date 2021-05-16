# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 01:26:25 2020

@author: sreevalli kurla ksv
"""
"""
import pymysql (in console)
#to check whether it is installed or not
"""

import pymysql
#connect to db
db= pymysql.connect(host='localhost',port=3306,user='root',password='611422',database='testdb')
print(db) #it should display some connection string

query="select*from realestate"

#preparing the cursor
cursor=db.cursor()

#execute the query
cursor.execute(query)

#display the output
for record in cursor.fetchall():
    print(record)

db.close()

######### insertion

import pymysql
#connect to db
db= pymysql.connect(host='localhost',port=3306,user='root',password='611422',database='testdb')
print(db) #it should display some connection string

street="hitechcity"
city="hyderabad"

query="insert into realestate values('{}','{}')".format(street,city)

#preparing the cursor
cursor=db.cursor()

#execute the query
cursor.execute(query)

#display the output
print(cursor.rowcount,"inserted")

db.commit()

db.close()







