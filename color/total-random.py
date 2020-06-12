#!/data/data/com.termux/files/usr/bin/env python3
import sys
import random
import subprocess

print (" ____  _                           __        __         _        ")
print ("/ ___|| |__   __ _ __________ _    \ \      / /__  _ __| | _____ ")
print ("\___ \| '_ \ / _` |_  /_  / _` |____\ \ /\ / / _ \| '__| |/ / __|")
print (" ___) | | | | (_| |/ / / / (_| |_____\ V  V / (_) | |  |   <\__ \\")
print ("|____/|_| |_|\__,_/___/___\__,_|      \_/\_/ \___/|_|  |_|\_\___/")
print ("\nTotal_Random\n")

try:
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
except Keyboarditerrupt:
	exit()
