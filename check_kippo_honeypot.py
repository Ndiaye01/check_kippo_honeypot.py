#!/usr/bin/env python
#!/usr/bin/python
import MySQLdb,sys,requests,json

myDB = MySQLdb.connect(host="",port=,user="",passwd="",db="")
cursor = myDB.cursor()


SEP = "|"
SEP1 = ", "

i=0
cursor.execute("SELECT id FROM auth;")
for row in cursor.fetchall():
        i += 1
#print i



def numberattack():
    i=0
    cursor.execute("SELECT id FROM auth;")
    for row in cursor.fetchall():
        i += 1
    return i

def list():
    s =""
    cursor.execute("select count(ip), ip from sessions group by ip order by count(ip) desc")
    listocc= []
    listip = []
    for row in cursor.fetchall():
        for field in row [::2]:
            listocc.append(field)
            #print listocc
    cursor.execute("select count(ip), ip from sessions group by ip order by count(ip) desc")
    for row in cursor.fetchall():
        for field in row [1::2]:
            listip.append(field)
            #print listip
    for i in range (len(listip)):
        s +=  str(listip[i]) + " (" + str(listocc[i]) +")"+ ", "
    return s

def numberip():
    cursor.execute("SELECT ip FROM sessions;")
    list= []
    for row in cursor.fetchall():
        for field in row:
            if field not in list:
                list.append(field)
    s = len(list)
    return s

def top30ip():
    s=""
    cursor.execute("select count(ip), ip from sessions where ip <> '' group by ip order by count(ip) desc limit 30;")
    listocc= []
    listip=[]
    for row in cursor.fetchall():
        for field in row [::2]:
            listocc.append(field)
            #print listocc
    cursor.execute("select count(ip), ip from sessions where ip <> '' group by ip order by count(ip) desc limit 30;")
    for row in cursor.fetchall():
        for field in row [1::2]:
            listip.append(field)
    for i in range (len(listip)):
        s +=  str(listip[i]) + " (" + str(listocc[i]) +")"+ ", "
    return s


def top10password():
    s=""
    cursor.execute("select count(password), password from auth where password <> '' group by password order by count(password) desc limit 10;")
    listocc= []
    listpassword = []
    for row in cursor.fetchall():
        for field in row [::2]:
            listocc.append(field)
            #print listocc
    cursor.execute("select count(password), password from auth where password <> '' group by password order by count(password) desc limit 10;")
    for row in cursor.fetchall():
        for field in row [1::2]:
            listpassword.append(field)
    for i in range (len(listpassword)):
        s +=  str(listpassword[i]) + " (" + str(listocc[i]) +")"+ ", "
    return s



def top10username():
    s=""
    cursor.execute("select count(username), username from auth where username <> '' group by username order by count(username) desc limit 10;")
    listocc= []
    listusername = []
    for row in cursor.fetchall():
        for field in row [::2]:
            listocc.append(field)
            #print listocc
    cursor.execute("select count(username), username from auth where username <> '' group by username order by count(username) desc limit 10;")
    for row in cursor.fetchall():
        for field in row [1::2]:
            listusername.append(field)
    for i in range (len(listusername)):
        s +=  str(listusername[i]) + " (" + str(listocc[i]) +")"+ ", "
    return s

def top10commands():
    s=""
    cursor.execute("select count(input), input from input where input <> '' group by input order by count(input) desc limit 10;")
    listocc= []
    listinput= []
    for row in cursor.fetchall():
        for field in row [::2]:
            listocc.append(field)
    cursor.execute("select count(input), input from input where input <> '' group by input order by count(input) desc limit 10;")
    for row in cursor.fetchall():
         for field in row [1::2]:
             listinput.append(field)
    for i in range (len(listinput)):
        s +=  str(listinput[i]) + " (" + str(listocc[i]) +")"+ ", "
    return s

def top10sshclients():

    s=""
    cursor.execute("SELECT  count(version) ,version FROM  sessions ,clients  WHERE sessions.client = clients.id  group by sessions.client order by count(version) desc limit 10;")
    listocc= []
    listclient = []
    for row in cursor.fetchall():
        for field in row [::2]:
            listocc.append(field)
    cursor.execute("SELECT  count(version) ,version FROM  sessions ,clients  WHERE sessions.client = clients.id  group by sessions.client order by count(version) desc limit 10;;")
    for row in cursor.fetchall():
        for field in row [1::2]:
            listclient.append(field)
    for i in range (len(listclient)):
        s +=  str(listclient[i]) + " (" + str(listocc[i]) +")"+ ", "
    return s

def successratio():
    s = ""
    cursor.execute("select count(success), success from auth group by success order by success;")
    listocc= []
    listsuccess = []
    for row in cursor.fetchall():
        for field in row [::2]:
            listocc.append(field)
            #print listocc
    s += str (listocc[1]) + " succeeded " + ", " + str(listocc[0]) + " failed"
    return s


def geolocation (ip):
    s=""
    result =requests.get("https://extreme-ip-lookup.com/json/" +ip)
    json_result=json.loads (result.text)
    #print json_result
    #for key  in json_result:
            #s += key + ": " + str(json_result[key]) +" ,"
    #s = json_result
    s = "Country : " + json_result["country"]  + SEP1 + "Region : " + json_result["region"] + SEP1 +"City : " + json_result["city"]  + SEP1 + "ISP : " + json_result["isp"]+ SEP1 + "IP Type :" + json_result["ipType"]
    return s
#print geolocation("175.102.6.52" )

def success(s):
    if s == 0:
        return "FAILED"
    elif s== 1:
        return "SUCCEEDED"


def new_entry():
    s = ""
    cursor.execute("SELECT  ip , success , password ,username,version , DATE_FORMAT(starttime,'%b %d %Y %h:%i %p'),DATE_FORMAT(endtime,'%b %d %Y %h:%i %p'), auth.id FROM auth , sessions ,clients  WHERE timestamp > DATE_SUB(NOW(), INTERVAL 5 MINUTE) AND auth.session = sessions.id AND sessions.client = clients.id;")
    #print cursor.fetchall()
    for row in cursor.fetchall():
        #print row
        s += "NEW ATTEMPT " + success(row[1]) +". " + "Attempt " + str(row[7]) + " : " + "IP : " + str(row[0])+ SEP1+ geolocation(str(row[0]))+ SEP1 +"Password : "+ str(row[2]) + SEP1 + "Username : " + str(row[3]) + SEP1 + "Authentication method : " + str(row[4]) + SEP1 + "Starttime : " + str(row[5]) + SEP1 + "Endtime : " + str(row[6]) +  "\n"
    return s


################## Main #############################
if new_entry():
        print "WARNING - " + new_entry()
        sys.exit(1)
else:
        print "OK - NO NEW ATTEMPT . " + str(numberip()) + " malicious ip, "+ str(numberattack()) + " attacks" +", " + successratio() + " " + SEP + "\n" +  "Top 30 IPs Attackers : " + str(top30ip()) + "\n" + "Top 10 passwords : " + top10password() +  "\n" + "Top 10 usernames : " + top10username() + "\n" + "Top 10 commands : " + top10commands() + "\n" + "Top 10 SSH clients : " + top10sshclients() + SEP + "'Attacks'=" + str(i) + "0;0;0;20000"
        sys.exit(0)
