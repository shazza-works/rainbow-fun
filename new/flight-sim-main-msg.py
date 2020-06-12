#!/data/data/com.termux/files/usr/bin/python3
import random
import subprocess
import time

print (" ____  _                           __        __         _        ")
print ("/ ___|| |__   __ _ __________ _    \ \      / /__  _ __| | _____ ")
print ("\___ \| '_ \ / _` |_  /_  / _` |____\ \ /\ / / _ \| '__| |/ / __|")
print (" ___) | | | | (_| |/ / / / (_| |_____\ V  V / (_) | |  |   <\__ \\")
print ("|____/|_| |_|\__,_/___/___\__,_|      \_/\_/ \___/|_|  |_|\_\___/")
print ("\n")

try:
	def copy2clip(txt):
	        cmd = 'echo \"' + txt + '\" | termux-clipboard-set'
	        return subprocess.check_call(cmd, shell=True)

	b_tag = '<color='
	b_end = '>'
	e_tag = '</color>'

	while 1:
		#msg = input("Enter MSG> ")
		#msg = msg[:104]
		out = []
		r = lambda: random.randint(0,255)
		code = '#%02X%02X%02X' % (r(),r(),r())
		out.append(b_tag + str(code) + b_end + "  " + e_tag) #took msg out
		txt = ''.join(out)
		copy2clip(txt)
		print ("Coppied..." + code + "--")
		time.sleep(2)
except KeyboardInterrupt:
        sys.exit(1)
