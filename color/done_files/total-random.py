#!/data/data/com.termux/files/usr/bin/env python3
import sys
import random
import subprocess

def copy2clip(txt):
    cmd='echo '+txt.strip()+' | termux-clipboard-set'
    return subprocess.check_call(cmd, shell=True)

def randomas():
	s = 0
	new = ""
	msgb = ""
	while 1:
		r = lambda: random.randint(0,255)
		msg = input("Random_Message: ") # cnanged [swap]
		if len(msg) >= 88:
			msgb = msg[120:]
			msg = msg[:120]
		msg = list(msg)
		for _ in msg:
			if _ == "":
				new = new + ""
				s = s - 1
			else:
				new = new + '[%02X%02X%02X]' % (r(),r(),r()) + _
			s = s + 1
		copy2clip("[c][b][i]" + new + msgb)
		print("Text Copied ^" + "\n")
		new = ""
		msgb = ""
		s = 0
randomas()
