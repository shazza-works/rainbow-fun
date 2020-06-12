#!/data/data/com.termux/files/usr/bin/env python3
import subprocess

print (" ____  _                           __        __         _        ")
print ("/ ___|| |__   __ _ __________ _    \ \      / /__  _ __| | _____ ")
print ("\___ \| '_ \ / _` |_  /_  / _` |____\ \ /\ / / _ \| '__| |/ / __|")
print (" ___) | | | | (_| |/ / / / (_| |_____\ V  V / (_) | |  |   <\__ \\")
print ("|____/|_| |_|\__,_/___/___\__,_|      \_/\_/ \___/|_|  |_|\_\___/")
print ("\nSlasher\n")

try:
	def copy2clip(txt):
	    cmd='echo \"'+ str(txt) +'\"| termux-clipboard-set ; termux-vibrate'
	    return subprocess.check_call(cmd, shell=True)
	while 1:
	    msg = input("Enter Msg ;")
	    my_list = msg.split()
	    string = '/'
	    my_new_list = [string + x for x in my_list]
	    string = ' '.join(my_new_list)
	    copy2clip(string)
	    print ("Text Copied ^" + "\n")
except KeyboardInterrupt:
        exit()
