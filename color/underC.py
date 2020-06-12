#!/data/data/com.termux/files/usr/bin/env python3
print (" ____  _                           __        __         _        ")
print ("/ ___|| |__   __ _ __________ _    \ \      / /__  _ __| | _____ ")
print ("\___ \| '_ \ / _` |_  /_  / _` |____\ \ /\ / / _ \| '__| |/ / __|")
print (" ___) | | | | (_| |/ / / / (_| |_____\ V  V / (_) | |  |   <\__ \\")
print ("|____/|_| |_|\__,_/___/___\__,_|      \_/\_/ \___/|_|  |_|\_\___/")
print ("\nUnder_Colour_NB<12 char MAX in Hackers Game>\n")

try:
	def undercolor():
		print (" - Just Copy & Paste The 11 Char Message; \n")
		colors = ["#ff0000","#ff4909","#ff7100","#ffac00","#eeff00","#b1ff00",'#27ff00','#09ff00','#00ff21','#00ff9b','#00ffd8','#00deff','#009bff','#0059ff','#0016ff','#5700ff','#b100ff','#f400ff','#ff00c8','#ff0085','#ff0043']
		s = 0
		new = ""
		msgb = ""
		while 1:
			msg = input("Message: ")
			if len(msg) >= 30:
				msgb = msg[30:]
				msg = msg[:30]
			msg = list(msg)
			for _ in msg:
				if s == len(colors):
					s = 0
				if _ == " ":
					new = new + " "
					s = s - 1
				else:
					new = new + colors[s].replace("#","[") + "]" + u"\u0332" + "[ffffff]" + _
				s = s + 1
			print ("[c][i][b]" + new + msgb + "\n")
			new = ""
			msgb = ""
			s = 0
	undercolor()
except KeyboardInterrupt:
        exit()
