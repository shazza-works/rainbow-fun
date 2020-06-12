#!/data/data/com.termux/files/usr/bin/env python3
print (" ____  _                           __        __         _        ")
print ("/ ___|| |__   __ _ __________ _    \ \      / /__  _ __| | _____ ")
print ("\___ \| '_ \ / _` |_  /_  / _` |____\ \ /\ / / _ \| '__| |/ / __|")
print (" ___) | | | | (_| |/ / / / (_| |_____\ V  V / (_) | |  |   <\__ \\")
print ("|____/|_| |_|\__,_/___/___\__,_|      \_/\_/ \___/|_|  |_|\_\___/")
print ("\nSplash_Dog\n")

try:
	def splashdog():
		print (" - Just Copy & Paste The Generated Messages - \n")
		colors = ['#086f6f','#0f9e7e','#3eb898','#0eb6b1','#079bb7']
		s = 0
		new = ""
		msgb = ""
		while 1:
			msg = input("Message: ")
			if len(msg) >= 48:
				msgb = msg[48:]
				msg = msg[:48]
			msg = list(msg)
			for _ in msg:
				if s == len(colors):
					s = 0
				if _ == "":
					new = new + ""
					s = s - 1
				else:
					new = new + colors[s].replace("#","[") + "]" + _
				s = s + 1
			print ("[c][b][i]" + new + msgb + "\n")
			new = ""
			msgb = ""
			s = 0
	splashdog()
except KeyboardInterrupt:
        exit()
