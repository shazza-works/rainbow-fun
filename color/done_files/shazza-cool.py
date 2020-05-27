#!/data/data/com.termux/files/usr/bin/env python3
def testao():
	print(" - Just Copy & Paste The Generated Messages - \n")
	colors = ["#550055","#ff0055","#880055","#660055","#440055","#220055","#110011","#330033","#550055","#770077","#990099","#ff00ff"]
	s = 0
	new = ""
	msgb = ""
	while 1:
		msg = input("Test_AO: ")
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
		print ("[b]" + new + msgb + "\n")
		new = ""
		msgb = ""
		s = 0
testao()
