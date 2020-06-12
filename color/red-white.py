#!/data/data/com.termux/files/usr/bin/env python3
print (" ____  _                           __        __         _        ")
print ("/ ___|| |__   __ _ __________ _    \ \      / /__  _ __| | _____ ")
print ("\___ \| '_ \ / _` |_  /_  / _` |____\ \ /\ / / _ \| '__| |/ / __|")
print (" ___) | | | | (_| |/ / / / (_| |_____\ V  V / (_) | |  |   <\__ \\")
print ("|____/|_| |_|\__,_/___/___\__,_|      \_/\_/ \___/|_|  |_|\_\___/")
print ("\nRed_White\n")

try:
	def just_red_white():
		print (" - Just Copy & Paste The Generated Messages - \n")
		colors = ["#ff0000","#ffffff","#ff0000","#ffffff","#ff0000",'#ffffff','#ff0000','#ffffff','#ff0000','#ffffff','#ff0000','#ffffff','#ff0000','#ffffff','#ff0000','#ffffff','#ff0000','#ffffff']
		s = 0
		new = ""
		msgb = ""
		while 1:
			msg = input("Red_White_Message: ")
			if len(msg) >= 80:
				msgb = msg[80:]
				msg = msg[:80]
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
			print ("[c][b]" + new + msgb + "\n")
			new = ""
			msgb = ""
			s = 0
	just_red_white()
except KeyboardInterrupt:
        exit()
