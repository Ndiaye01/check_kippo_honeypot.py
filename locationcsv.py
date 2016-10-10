import MySQLdb
import sys
import csv
import requests
import json

dbServer=''
dbPass=''
dbUser=''
dbQuery='SELECT DISTINCT ip FROM sessions ;'


def geolocation (ip):
    s=""
    result =requests.get("https://extreme-ip-lookup.com/json/" +ip)
    json_result=json.loads (result.text)
    s =  json_result["lat"]+";"+json_result["lon"]
    return s

myDB = MySQLdb.connect(host="",port=3306,user="",passwd="",db="")
cursor = myDB.cursor()
cursor.execute(dbQuery)
result=cursor.fetchall()
d = csv.writer(open("location.csv","w"))
for row in result:
    for line in row:
        d.writerow([geolocation(line)])



