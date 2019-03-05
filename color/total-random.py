#Shazza edit
import random
import subprocess

def copy2clip(txt):
    cmd='echo '+txt.strip()+' | termux-clipboard-set'
    return subprocess.check_call(cmd, shell=True)

def randomas():
	print (" - Just Copy & Paste The Generated Messages - \n")
	#colors = ["#10","#20","#30","#20",'#40','#30','#20','#10','#20','#30','#40','#50','#60','#50','#40','#30','#50','#20']
	s = 0
	new = ""
	msgb = ""
	while 1:
		r = lambda: random.randint(0,255)
		msg = input("Random_Message: ")
		if len(msg) >= 88:
			msgb = msg[120:]
			msg = msg[:120]
		msg = list(msg)
		for _ in msg:
			#if s == len(colors):
			#	s = 0
			if _ == "":
				new = new + ""
				s = s - 1
			else:
				new = new + '[%02X%02X%02X]' % (r(),r(),r()) + _
			s = s + 1
		copy2clip("[c][b][i]" + new + msgb + "\n")
		print("Text Copied ^" + "\n")
		new = ""
		msgb = ""
		s = 0
randomas()
