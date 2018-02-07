#Shazza Edit
def blueslash():
	print " - Just Copy & Paste The Generated Messages - \n"
	colors = ['#2b4141','#eed369','#083d77','#a11021','#004a6e']
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
blueslash()

