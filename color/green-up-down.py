#!/data/data/com.termux/files/usr/bin/env python3
print (" ____  _                           __        __         _        ")
print ("/ ___|| |__   __ _ __________ _    \ \      / /__  _ __| | _____ ")
print ("\___ \| '_ \ / _` |_  /_  / _` |____\ \ /\ / / _ \| '__| |/ / __|")
print (" ___) | | | | (_| |/ / / / (_| |_____\ V  V / (_) | |  |   <\__ \\")
print ("|____/|_| |_|\__,_/___/___\__,_|      \_/\_/ \___/|_|  |_|\_\___/")
print ("\nGreen_Up_Down\n")

try:
	def rainfade():
	        print(" - Press [Return] To Copy The Generated Messages - \n")
	        colors = ["#20","#40"]
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
	                print ("[c][i][b][aaff00]" + new + msgb + "\n")
	                new = ""
	                msgb = ""
	                s = 0
	rainfade()
except KeyboardInterrupt:
        exit()
