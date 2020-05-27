#!/data/data/com.termux/files/usr/bin/env python3
def sunset():
	print (" - Just Copy & Paste The Generated Messages - \n")
	colors = ["#ff0000","#ff2200","#ff4400","#ff6600",'#ff8800','#ff9900','#ff9922','#ff9944','#ff9966','#ff9966','#ff9988'] #,'#ff2299','#ff3399','#ff4499','#ff5599','#ff6699','#ff7799']
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
sunset()
