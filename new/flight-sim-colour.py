#!/data/data/com.termux/files/usr/bin/python3
import random
import subprocess

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
	#col = ["#badd11", "#00ff00", "#0000ff", "#ff00ff"]

	while 1:
		msg = input("Enter MSG> ")
		lst = msg.split()
		out = []
		for x in lst:
			#y = random.choice(col)
			r = lambda: random.randint(0,255)
			code = '#%02X%02X%02X' % (r(),r(),r())
			out.append(b_tag + str(code) + b_end + str(x + ' ') + e_tag)
			txt = ''.join(out)
		copy2clip(txt)
		print ("Coppied..." + "\n")
except KeyboardInterrupt:
        sys.exit(1)
