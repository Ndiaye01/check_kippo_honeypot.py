# check_kippo_honeypot.py
check_kippo_honeypot.py is an Icinga custom plugin to monitor a Kippo honeypot .It

-checks every 5 minutes if  the honeypot has recorded a new attack.If so ,changes status to WARNING and gives  relevant information about this attacker (e.g. if the attack succeeded or failed, IP, country ,region, used password,used username,authentication method,timestamp..)
-checks in real-time the total number of attacks 
-checks in real-time the top 30 IPs attackers with  respective number of attempts
-checks in real-time the Top 10 most com mon passwords 
-checks in real-time Top 10 most common usernames
-checks in real-time Top 10 most common used commands
--checks in real-time Top 10 most common SSH client 

check_kippo_honeypot presents 2 statutes to Icinga2 :
OK : if no new attack has occured
WARNING :if a new attack has occured

check_kippo_honeypot presents the total number of attacks as performance data for later visualization with PNP4NAGIOS or Graphite.
The script locationcsv.py creates a CSV files of geogrphical coordinates of attackers for mapping with ?agvis-Geomap.

To integrate check\_kippo\_honeypot in Icinga Web2,

REQUIREMENTS : 
-PYTHON
-PYTHON -MySqldb
-Python requests
-Kippo
-Kippo MySql database
-Icinga2 
-Icinga Web 2

 download the plugin from the git repository and move it into  your PluginDir directory. To connect to your KIPPO  MySQL database, you should edit the file program and add your honeypot'IP to "host" and your  database credentials. The database credentials are the user,the password, created while setting up the KIPPO  MySQL  database to "user", "passwd", "db". Then you should make the plugin executable.
 
 chmod +x /usr/lib/nagios/plugins/check\_kippo\_honeypot.py
 
 The second step is to edit your commands.conf and services.conf files.check\_kippo\_honeypot command has as argument "timeout = 320".
 
 {object CheckCommand "check\_kippo\_honeypot.py" {

  import "plugin-check-command"
  
  command = [ PluginDir + "\/check\_kippo\_honeypot.py"]
  
  timeout = 320
}
 


