# check_kippo_honeypot.py

## Synopsis

check_kippo_honeypot.py is an Icinga custom plugin to monitor a Kippo honeypot .It performs at each check:

- Detection of a new attack with relevant information as used password/username combination during the session, the fail or the success , the ssh client version, the location of the attack, the ISP and the type of the ISP (residential/business/education)
- If no new attack:The total number of attacks, the connections per ip, and the success ratio ,List of top 30 attackers, top 10 passwords, top 10 usernames, top 10 commands ,top 10 ssh clients
- graphing of attacks
- mapping of attacks

check_kippo_honeypot presents 2 statutes to Icinga2 :
OK : if no new attack has occured
WARNING :if a new attack has occured.

check_kippo_honeypot presents the total number of attacks as performance data for later visualization with PNP4NAGIOS or Graphite. The script locationcsv.py creates a CSV files of geogrphical coordinates of attackers for mapping with ?agvis-Geomap.

## Installation
To integrate check\_kippo\_honeypot in Icinga Web2:

REQUIREMENTS : 
- PYTHON
- PYTHON -MySqldb
- Python requests
- Kippo
- Kippo MySql database
- Icinga2 
- Icinga Web 2

Download the plugin from the git repository and move it into  your PluginDir directory. To connect to your KIPPO  MySQL database, you should edit the file program and add your honeypot'IP to "host" and your  database credentials. The database credentials are the user, the password, created while setting up the KIPPO  MySQL  database to "user", "passwd", "db". Then you should make the plugin executable.
 
 chmod +x /usr/lib/nagios/plugins/check\_kippo\_honeypot.py
 
 The second step is to edit your commands.conf and services.conf files.c heck\_kippo\_honeypot command has as argument "timeout = 320".
 
 {object CheckCommand "check\_kippo\_honeypot.py" {

  import "plugin-check-command"
  
  command = [ PluginDir + "\/check\_kippo\_honeypot.py"]
  
  timeout = 320
}
 


