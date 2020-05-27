#!/data/data/com.termux/files/usr/bin/env python3
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
