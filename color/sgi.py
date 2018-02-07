#Shazza Edit
def sgi():
	print " - Just Copy & Paste The Generated Messages - \n"
	colors = ['#8E388E','#7171C6','#7D9EC0','#388E8E','#71C671','#8E8E38','#C5C1AA','#C67171','#555555']
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
		print "[c][b][i]" + new + msgb + "\n"
		new = ""
		msgb = ""
		s = 0
sgi()
