
#(from csv to db)

import csv
import pymysql

#connect to db
db= pymysql.connect(host='localhost',port=3306,user='root',password='611422',database='testdb')
fobj=open("C:\\Users\\sreevalli kurla ksv\\Desktop\\realestate.csv","r")
#convert file object to csv object
reader=csv.reader(fobj)
cursor = db.cursor()
for line in reader:
    street=line[0]
    city=line[1]
    query="insert into realestate values('{}','{}')".format(street,city)
    #execute the query
    cursor.execute(query)
db.commit()

db.close()

######### with exception handling

try:
    db= pymysql.connect(host='localhost',port=3306,user='root',password='611422',database='testdb')
    fobj=open("C:\\Users\\sreevalli kurla ksv\\Desktop\\realestate.csv","r")
#convert file object to csv object
    reader=csv.reader(fobj)
    cursor = db.cursor()
    for line in reader:
     street=line[0]
     city=line[1]
     query="insert into realestate values('{}','{}')".format(street,city)
    #execute the query
     cursor.execute(query)
    db.commit()
    db.close()
except (FileNotFoundError,IndexError,TypeError) as err:
    print(err)
except Exception as err:
    print(err)
    

#from (read from db and insert into csv file)

import pymysql

#connect to db
db= pymysql.connect(host='localhost',port=3306,user='root',password='611422',database='testdb')
print(db) #it should display some connection string

query= "select * from realestate"

#preparing the cursor
cursor = db.cursor()

#execute the query
for record in cursor.fetchall():
    print(record)

db.close()


############    WEB SCRAPING

import requests #to download the source code
from bs4 import BeautifulSoup 


response = requests.get("https://www.techworldguru.com/")
if response.status_code==200:
    soup=BeautifulSoup(response.text,'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))




