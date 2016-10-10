import MySQLdb
import sys
import csv
import requests
import json

dbQuery='SELECT DISTINCT ip FROM sessions ;'

def geolocation (ip):
    s=""
    result =requests.get("https://extreme-ip-lookup.com/json/" +ip)
    json_result=json.loads (result.text)
    s =  json_result["country"]
    return s


def listcountry():
    myDB = MySQLdb.connect(host="52.38.126.135",port=3306,user="test",passwd="test",db="kippo")
    cursor = myDB.cursor()
    cursor.execute(dbQuery)
    result=cursor.fetchall()
    list = []
    for row in result:
        #print row
        for field in row:
            #print field
            list += (geolocation(field))
        return list

print listcountry()



#d = csv.writer(open("country.csv","w"))
#for row in result:
#    for line in row:
#        d.writerow([geolocation(line)])
