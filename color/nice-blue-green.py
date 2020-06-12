#!/data/data/com.termux/files/usr/bin/env python3
print (" ____  _                           __        __         _        ")
print ("/ ___|| |__   __ _ __________ _    \ \      / /__  _ __| | _____ ")
print ("\___ \| '_ \ / _` |_  /_  / _` |____\ \ /\ / / _ \| '__| |/ / __|")
print (" ___) | | | | (_| |/ / / / (_| |_____\ V  V / (_) | |  |   <\__ \\")
print ("|____/|_| |_|\__,_/___/___\__,_|      \_/\_/ \___/|_|  |_|\_\___/")
print ("\nNice_Blue_Green\n")

try:
	def bluegreen():
		print (" - Just Copy & Paste The Generated Messages - \n")
		colors = ["#0d38c0","#460eea","#a60ee9","#e80ecb",'#e70e6a','#e6110e','#e5700e','#e4ce0e','#9ae30e','#3ce20e','#0de13c']
		s = 0
		new = ""
		msgb = ""
		while 1:
			msg = input("Message: ")
			if len(msg) >= 100:
				msgb = msg[100:]
				msg = msg[:100]
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
	bluegreen()
except KeyboardInterrupt:
        exit()
