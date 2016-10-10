import MySQLdb
import sys
import csv
import requests
import json

dbServer='kippo'
dbPass='test'
dbUser='test'

dbQuery='SELECT DISTINCT ip FROM sessions ;'

#db=dbapi.connect(host=dbServer,user=dbUser,passwd=dbPass)
#cur=db.cursor()
#cur.execute(dbQuery)
#result=cur.fetchall()

def geolocation (ip):
    s=""
    result =requests.get("https://extreme-ip-lookup.com/json/" +ip)
    json_result=json.loads (result.text)
    s =  json_result["lat"]+";"+json_result["lon"]
    return s



myDB = MySQLdb.connect(host="52.38.126.135",port=3306,user="test",passwd="test",db="kippo")
cursor = myDB.cursor()
cursor.execute(dbQuery)
result=cursor.fetchall()
d = csv.writer(open("location.csv","w"))
for row in result:
    for line in row:
        d.writerow([geolocation(line)])



#for row in result:
#    c.writerow(row)
#c.writerow(result)

#file=open("ip.csv","r")
#test=csv.reader(file)
#d = csv.writer(open("location.csv","w"))
#for row in test:
#    for line in row:
#        d.writerow([geolocation(line)])
