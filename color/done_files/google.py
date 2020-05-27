#!/data/data/com.termux/files/usr/bin/env python3
#Shazza Edit
def google():
	print (" - Just Copy & Paste The Generated Messages - \n")
	colors = ['#4885ed','#db3236','#f4c20d','#4885ed','#3cba54','#db3236','#4885ed','#db3236','#f4c20d','#4885ed','#3cba54','#db3236']
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
google()
