# Anubis Captive Wifi Hotspot bypass

Captive Portal
==

[A Web page used on public-access networks that require a user to view and interact with before being granted access to the public network. Captive portals are widely used by businesses that offer free Wi-Fi hotspots to Internet users. Usually a captive portal requires users to read and accept the business' acceptable use policy (AUP).](https://www.webopedia.com/TERM/C/captive_portal.html)

Many institutions use this type of authentication in the WIFI as a 'sure' means of preventing unauthorised access.


Image Example
==

![alt text](https://exekias.me/wp-content/uploads/2011/08/login.png)

[___Carlos Pérez-Aradros Herce___](https://exekias.me/2011/08/28/zentyal-new-feature-captive-portal/)  Captive hotspot


How Anubis works
==

![alt text](https://github.com/philemonsunday/anubis/blob/master/src/images/netflow.png?raw=true)

Captive Wifi Hotspot network structure with the attacker standby
The captive hotspot accepts traffic only from the registered devices
anubis scans for all the devices connected on the same network
It then tries to change the device IDS into the identified deviced IDs

Installing anubis
==

Clone the anubis project files

`git clone --recursive https://github.com/sundaysec/anubis.git`


Navigate to the cloned folder

`cd ./anubis/`

Install dependencies
`pip install -r requirements.txt`

Run the installer
`pip install -r requirements.txt`
Run anubis

`python anubis.py`
