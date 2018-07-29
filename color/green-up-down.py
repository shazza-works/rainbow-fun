def rainfade():
        # Rainfade Provides a Smooth Transition In Between Each Set Of Color
        print(" - Press [Return] To Copy The Generated Messages - \n")
        colors = ["#20","#40"]
        s = 0
        new = ""
        msgb = ""
        while 1:
                msg = input("Rainfade_Message: ")
                if len(msg) >= 55:
                        msgb = msg[55:]
                        msg = msg[:55]
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
                copy2clip("[c][i][b][aaff00]" + new + msgb + "\n")
		print("Text Copied ^" + "\n")
                new = ""
                msgb = ""
                s = 0
rainfade()
