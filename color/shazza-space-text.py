#!/data/data/com.termux/files/usr/bin/env python3
import subprocess

print (" ____  _                           __        __         _        ")
print ("/ ___|| |__   __ _ __________ _    \ \      / /__  _ __| | _____ ")
print ("\___ \| '_ \ / _` |_  /_  / _` |____\ \ /\ / / _ \| '__| |/ / __|")
print (" ___) | | | | (_| |/ / / / (_| |_____\ V  V / (_) | |  |   <\__ \\")
print ("|____/|_| |_|\__,_/___/___\__,_|      \_/\_/ \___/|_|  |_|\_\___/")
print ("\nSpace_Text\n")

try:
	def copy2clip(txt):
	    cmd='echo \"'+ str(txt) +'\"| termux-clipboard-set ; termux-vibrate'
	    return subprocess.check_call(cmd, shell=True)

	def space_text():
		print(" - Press [Return] To Copy The Generated Messages - \n")
		msg = ""
		msg1 = ""
		msgb =""
		new = ""
		while 1:
			msg = input("Space_Text_Message: ")
			msg1 = ['{0} '.format(elem) for elem in msg]
			msg = ''.join(str(e) for e in msg1)
			new = new + msg.replace("#","[") + "]"
			#copy2clip('[c][i][b][ff0000]ร[aa0055]ɦ[5500aa]α[0000ff]ƶ[0055aa]ɱ[00aa55]µ[00ff00]ร[ffffff] [' + new + msgb + '\n')
			copy2clip('[c][i][b]Python 3.6.6 >>> [ff4400][' + new + msgb + '\n')
			print ("Text Copied ^" + "\n")
			new = ""
			msgb = ""
	space_text()
except KeyboardInterrupt:
        exit()
