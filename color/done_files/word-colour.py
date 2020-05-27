#!/data/data/com.termux/files/usr/bin/env python3
import subprocess

def copy2clip(txt):
	msg = txt.replace("'", "\\'").strip()
	cmd = 'echo ' + msg + ' | termux-clipboard-set'
	return subprocess.check_call(cmd, shell=True)

def word_color():
	print(" - Press [Enter] To Copy The Generated Messages - \n\n")
	colors = ["#ff0000","#ff4909","#ff7100","#ffac00","#eeff00","#b1ff00",'#27ff00','#09ff00','#00ff21','#00ff9b','#00ffd8','#00deff','#009bff','#0059ff','#0016ff','#5700ff','#b100ff','#f400ff','#ff00c8','#ff0085','#ff0043']
	#colors = ["#FF0000","#BF3F00","#7F7F00","#3FBF00","#00FF00","#00BF3F","#007F7F","#003FBF","#0000FF"]
	s = 0
	new = ""
	msgb = ""
	while 1:
		msg = input("Each_Word_Message: ")
		msg = msg.replace("'", "\'")
		#msg = msg.replace("@", " ")
		if len(msg) >= 150:
			msgb = msg[150:]
			msg = msg[:150]
		msg = msg.split()
		for _ in msg:
			if s == len(colors):
				s = 0
			if _ == " ":
				new = new + " "
				s = s - 1
			else:
				new = new + colors[s].replace("#","[") + "]" + _ + " "
				s = s + 1
		copy2clip("[c][i][b]" + new + msgb + "\n\n")
		print ("Text Copied ^" + "\n")
		new = ""
		msgb = ""
		s = 0
word_color()
