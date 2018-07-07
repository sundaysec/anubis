 # DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
 #                    Version 2, December 2004
 #
 # Copyright (C) 2018 Sunday Philemon <philemonsunday202@gmail.com>
 #
 # Everyone is permitted to copy and distribute verbatim or modified
 # copies of this license document, and changing it is allowed as long
 # as the name is changed.
 #
 #            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
 #   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
 #
 #  0. You just DO WHAT THE FUCK YOU WANT TO.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from src import banner
import sys
import subprocess
#vars
cwd = os.getcwd()

#confirm dependencies
#For netdiscover
if os.path_isdir("/usr/share/doc/netdiscover"):
	pass
else:
	subprocess.Popen("apt install netdiscover").wait()
	
# For macchanger
if os.path_isfile("/usr/bin/macchanger"):
		pass
	else:
		subprocess.Popen("apt install macchanger").wait()

#file manupulation function
def man():
	with open(cwd + "/src/dump.txt") as data:
		pass
		
		
	
def main():
    try:
        banner.burn()
        #to create the dump.txt file
        os.system("netdiscover > " + cwd + "/src/dump.txt")
    except:
        Exception
			#Print("Ok Goodbye")
			
			
			
			
if __name__ == '__main__':
    main()
