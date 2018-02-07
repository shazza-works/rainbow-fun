# Version 8.1.4 Made for Pythonista 3 By: SavSec - I 
# Don't Give A Fuck License -
import random, sys, clipboard
def blood():
	# Blood Provides a Crimson Text That Changes Shade
	colors = ["#cc0000","#bb0000","#aa0000","#990000","#880000","#770000","#880000","#990000","#aa0000","#bb0000"]
	s = 0
	new = ""
	msgb = ""
	try:
		while 1:
			sys.stderr = msg = raw_input("Message: ")
			if len(msg) >= 22:
				msgb = msg[22:]
				msg = msg[:22]
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
					clipboard.copy("[c][b]" + new + msgb)
					new = ""
					msgb = ""
	except:
		sys.exit()
def waves():
	# Waves Provides a Cool Dark Blue Text That Changes Shade
	colors = ["#0000cc","#0000bb","#0000aa","#000099","#000088","#000077","#000088","#000099","#0000aa","#0000bb"]
	s = 0
	new = ""
	msgb = ""
	try:
		while 1:
			sys.stderr = msg = raw_input("Message: ")
			if len(msg) >= 22:
				msgb = msg[22:]
				msg = msg[:22]
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
					clipboard.copy("[c][b]" + new + msgb)
					new = ""
					msgb = ""
	except:
		sys.exit()
def rain():	# Rain Provides a Solid Set Of Rainbow Colors
	colors = ["#ff0000","#ffff00","#00ff00","#00ffff","#0000ff","#ff00ff"]
	s = 0
	new = ""
	msgb = ""
	try:
		while 1:
			sys.stderr = msg = raw_input("Message: ")
			if len(msg) >= 22:
				msgb = msg[22:]
				msg = msg[:22]
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
					clipboard.copy("[c][b]" + new + msgb)
					new = ""
					msgb = ""
	except:
		sys.exit()
def rainfade():
	# Rainfade Provides a Smooth Transition In Between Each Set Of Color
	colors = ["#ff0000","#ff4909","#ff7100","#ffac00","#eeff00","#b1ff00",'#27ff00','#09ff00','#00ff21','#00ff9b','#00ffd8','#00deff','#009bff','#0059ff','#0016ff','#5700ff','#b100ff','#f400ff','#ff00c8','#ff0085','#ff0043']
	s = 0
	new = ""
	msgb = ""
	try:
		while 1:
			sys.stderr = msg = raw_input("Message: ")
			msg = unicode(msg)
			if len(msg) >= 22:
				msgb = msg[22:]
				msg = msg[:22]
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
					clipboard.copy("[c][b]" + new + msgb)
					new = ""
					msgb = ""
					s = 0
	except:
		sys.exit()
def bloodforum():
	# BloodForum is used on Hacker's Forum Page To Make Blood Text
	try:
		colors = ["#e00000","#c70000","#af0000","#a10000","#8e0000","#7d0000","#a00000","#ad0000","#ca0000","#e00000"]
		new = ""
		s = 0
		a = 0
		n = 2
		while 1:
			msg = raw_input("Message: ")
			msg = [msg[i:i+n] for i in range(0, len(msg), n)]
			for _ in msg:
				if s == 10:
					s = a
					a = 1
					if a == 10:
						a = 0
				if _ == " ":
					new = new + _
					s = s - 1
				else:
					new = new + "[color=" + colors[s] + "]" + _ + "[/color]"
					s = s + 1
					clipboard.copy(new)
					new = ""
	except:
		sys.exit()
def updown():
	# UpDown Makes Your Text Go Up And Down
	colors = ["#sup","#/sup","#sub","#/sub"]
	s = 0
	new = ""
	msgb = ""
	try:
		while 1:
			sys.stderr = msg = raw_input("Message: ")
			if len(msg) >= 100:
				msgb = msg[100:]
				msg = msg[:100]
				msg = msg.split(" ")
			for _ in msg:
				if s == len(colors):
					s = 0
				if _ == " ":
					new = new + " "
					s = s - 1
				else:
					new = new + colors[s].replace("#","[") + "]" + _ + " "
					s = s + 1
					clipboard.copy("[c][b][00ffff]" + new + msgb)
					new = ""
					msgb = ""
	except:
		sys.exit()
def undercolor():
	# Undercolor Provides a Under Beam of Colour
	colors = ["#ff0000"]
	s = 0
	new = ""
	msgb = ""
	try:
		while 1:
			sys.stderr = msg = raw_input("Message: ")
			if len(msg) <= 11:
				n = 1
			elif 11 < len(msg) <= 18:
				n = 2
			elif 18 < len(msg) <= 32:
				n = 3
			elif 32 < len(msg) <= 50:
				n = 5
				msg = [msg[i:i+n] for i in range(0, len(msg), n)]
			if len(msg) >= 25:
				msgb = msg[25:]
				msg = msg[:35]
				msg = list(msg)
			for _ in msg:
				if s == len(colors):
					s = 0
					new = new + colors[s].replace("#","[") + "]" + u"\u0332" + "[efffff]" + _
					s = s + 1
					clipboard.copy("[c][b]" + new + msgb)
					new = ""
					msgb = ""
					s = s
	except:
		sys.exit()
