#Shazza Edit
def orangegreen():
	print (" - Just Copy & Paste The Generated Messages - \n")
	colors = ["#ec7b0e","#bf910e",'#92a80e','#65bf0e','#4fcace','#22e10e','#0ced0e']
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
orangegreen()
