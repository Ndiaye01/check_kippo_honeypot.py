# check_kippo_honeypot.py
check_kippo_honeypot.py is an Icinga custom plugin to monitor a Kippo honeypot .It

-checks every 5 minutes if  the honeypot has recorded a new attack.If so ,changes status to WARNING and gives  relevant information about this attacker (e.g. if the attack succeeded or failed, IP, country ,region, used password,used username,authentication method,timestamp..)
-checks in real-time the total number of attacks 
-checks in real-time the top 30 IPs attackers with  respective number of attempts
-checks in real-time the Top 10 most com mon passwords 
-checks in real-time Top 10 most common usernames
-checks in real-time Top 10 most common used commands
--checks in real-time Top 10 most common SSH client 

check_kippo_honeypot presents 2 statuses to Icinga2 :
OK : if no new attack has occured
WARNING :if a new attack has occured

check_kippo_honeypot presents the total number of attacks as performance data for later visualization with PNP4NAGIOS or Graphite.
The script country.csv gives a CSV files of geogrphical coordinates of attackers for eventual mapping with ?agvis-Geomap.


