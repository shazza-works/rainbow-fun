#!/data/data/com.termux/files/usr/bin/env python3
import subprocess

print (" ____  _                           __        __         _        ")
print ("/ ___|| |__   __ _ __________ _    \ \      / /__  _ __| | _____ ")
print ("\___ \| '_ \ / _` |_  /_  / _` |____\ \ /\ / / _ \| '__| |/ / __|")
print (" ___) | | | | (_| |/ / / / (_| |_____\ V  V / (_) | |  |   <\__ \\")
print ("|____/|_| |_|\__,_/___/___\__,_|      \_/\_/ \___/|_|  |_|\_\___/")
print ("\nNet_Fade\n")

try:
	def copy2clip(txt):
		cmd='echo '+txt.strip()+' | termux-clipboard-set'
		return subprocess.check_call(cmd, shell=True)

	def rainfade():
	        print (" - Just Copy & Paste The Generated Messages - \n")
	        colors = ["#FF0000","#BF3F00","#7F7F00","#3FBF00","#00FF00","#00BF3F","#007F7F","#003FBF","#0000FF"]
	        s = 0
	        new = ""
	        msgb = ""
	        while 1:
	                msg = input("Rainfade_Message: ")
	                if len(msg) >= 55:
	                        msgb = msg[55:]
	                        msg = msg[:55]
	                msg = list(msg)
	                for _ in msg:
	                        if s == len(colors):
	                                s = 0
	                        if _ == " ":
	                                new = new + " "
	                                s = s - 1
	                        else:
	                                new = new + colors[s].replace("#","[") + "]" + _
	                        s = s + 1
	                copy2clip("[c][i][b]" + new + msgb + "\n")
	                print("Text Copied ^" + "\n")
	                new = ""
	                msgb = ""
	                s = 0
	rainfade()
except KeyboardInterrupt:
        exit()
