# Anubis Captive Wifi Hotspot bypass

[A Web page used on public-access networks that require a user to view and interact with before being granted access to the public network. Captive portals are widely used by businesses that offer free Wi-Fi hotspots to Internet users. Usually a captive portal requires users to read and accept the business' acceptable use policy (AUP).](https://www.webopedia.com/TERM/C/captive_portal.html)

Many institutions use this type of authentication in the WIFI as a 'sure' means of preventing unauthorised access.


Image Example
==

![alt text](https://exekias.me/wp-content/uploads/2011/08/login.png)

[___Carlos Pérez-Aradros Herce___](https://exekias.me/2011/08/28/zentyal-new-feature-captive-portal/)  Captive hotspot


How Captive Hotspot works
==

![alt text](https://github.com/philemonsunday/anubis/blob/master/src/images/netflow.png?raw=true)

Captive Wifi Hotspot network structure

Installing anubis
==

Clone the anubis project files
`git clone https://github.com/philemonsunday/anubis.git`


Navigate to src in the cloned folder

`cd ./anubis/src`

Run the installer to check dependencies

`chmod +x ./installer.sh ; ./installer.sh`

Run the main python file

`cd .. ; python anubis.py`
