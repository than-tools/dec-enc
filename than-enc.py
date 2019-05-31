#!/usr/bin/python

############################### TOOLS MAKED BY G3D1T
import os
import urllib2
import json
from termcolor import colored, cprint
from base64 import *
############################### RECODE AUTO JAHANNAM

os.system("reset")

print ("\033[93m  ____  ____  _____     ___  _____ _____   _____ _   _    _    _   _")
print ("\033[93m |  _ \|  _ \|_ _\ \   / / \|_   _| ____| |_   _| | | |  / \  | \ | |")
print ("\033[93m | |_) | |_) || | \ \ / / _ \ | | |  _|     | | | |_| | / _ \ |  \| |")
print ("\033[93m |  __/|  _ < | |  \ V / ___ \| | | |___    | | |  _  |/ ___ \| |\  |")
print ("\033[93m |_|   |_| \_\___|  \_/_/   \_\_| |_____|   |_| |_| |_/_/   \_\_| \_|")
print ("\033[93m     THAN ENCRYPT\n")

text = raw_input("Input Text : ")
enc = b64encode(text)
print "Encrypted Text :",enc

text = colored('Thanks For Using This Tools :3, dont forget follow my instagram @nathandeft' , 'white', attrs=['reverse', 'blink'])
print(text)