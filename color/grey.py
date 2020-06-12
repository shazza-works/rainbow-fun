#!/data/data/com.termux/files/usr/bin/env python3
print (" ____  _                           __        __         _        ")
print ("/ ___|| |__   __ _ __________ _    \ \      / /__  _ __| | _____ ")
print ("\___ \| '_ \ / _` |_  /_  / _` |____\ \ /\ / / _ \| '__| |/ / __|")
print (" ___) | | | | (_| |/ / / / (_| |_____\ V  V / (_) | |  |   <\__ \\")
print ("|____/|_| |_|\__,_/___/___\__,_|      \_/\_/ \___/|_|  |_|\_\___/")
print ("\nGrey\n")

try:
	def moonlight():
		print (" - Just Copy & Paste The Generated Messages - \n")
		colors = ["#10","#20","#30","#20",'#40','#30','#20','#10','#20','#30','#40','#50','#60','#50','#40','#30','#50','#20']
		s = 0
		new = ""
		msgb = ""
		while 1:
			msg = raw_input("Message: ").decode('utf8')
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
	moonlight()
except KeyboardInterrupt:
        exit()
