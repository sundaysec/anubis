#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 # DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
 #                    Version 2, December 2004
 #
 # Copyright (C) 2018 Sunday Philemon philemonsunday202@gmail.com
 #
 # Everyone is permitted to copy and distribute verbatim or modified
 # copies of this license document, and changing it is allowed as long
 # as the name is changed.
 #
 #            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
 #   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
 #
 #  0. You just DO WHAT THE FUCK YOU WANT TO.

import os
from src import banner
import sys
import subprocess
import argparse as arg
import argcomplete

#vars
cwd = os.getcwd()
host = os.platform()

#arguments
parser = arg.ArgumentParser()
parser.add_argument("-i", "--interface", help="The active interface used (Default:wlan0)", default="wlan0")
parser.add_argument("-r", "--range", help="The range of scan(Default:24)", default=24)

#For argument autocomplete
argcomplete.autocomplete(parser)
q = parser.parse_args()

#Simple oop
class anubis:
	def __init__(self, interface, range):
		self.iface = interface
		self.rng = range

	def scan(self):
		pass
#Continue
