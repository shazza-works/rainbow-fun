#!/data/data/com.termux/files/usr/bin/env python3
def just_c_b_i_u_s():
	print (" - Just Copy & Paste The Generated Messages - \n")
	colors = ["#c","#/c","#i","#/i","#c",'#/c','#i','#/i','#c','#/c','#i','#/i','#c','#/c','#i','#/i','#c','#/c','#i','#/i']
	s = 0
	new = ""
	msgb = ""
	while 1:
		msg = input("I-B-U-S-C_Message: ")
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
just_c_b_i_u_s()
