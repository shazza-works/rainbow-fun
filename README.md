#____Rainbow_Fun____ #
- Fade and Rainbow Scripts that have been messed with for ages. This is a 
SavSec origonal, it's been changed so many times and all you color sets i 
have made and use on hackers games are here.

- Hope You Enjoy As Much As I Have. Origonal Rainfade From SavSec_Ro The 
Russian Otter... Rainfade Provides a Smooth Transition In Between Each Set 
Of Color.

#____How To Use____
- [ADDED BY REQUEST]
- To use this on your phone you will need to install a terminal or 
an idle, I use termux from the Android Play Store, Please install Termux 
and give these commands.

```sh
pkg install python*
pkg update
pkg upgrade -y
```

- After this you will be able to download the bow.py script with.

```sh
git clone https://github.com/shazza-works/Rainbow_Fun/
cd Rainbow_Fun
python2 bow.py
```

- You should now see the request for a message, Just type and press 
Return, and copy and past to Hackers.
- [HOPE THIS HELPS?]

You will be asked for a msg to enter
-  Just Copy & Paste The Generated Messages

colors = ["#ff0000","#ff4909","#ff7100","#ffac00","#eeff00","#b1ff00",'#27ff00','#09ff00','#00ff21','#00ff9b','#00ffd8','#00deff','#009bff','#0059ff','#0016ff','#5700ff','#b100ff','#f400ff','#ff00c8','#ff0085','#ff0043']
- A list of your colous to use for text...   <CHANGE AS NEEDED>

msg = raw_input("Rainfade_Message: ")
- msg is your msg text, graabbed by raw_input

new = new + colors[s].replace("#","[") + "]" + _
- Will fit the codes in and remove '#000000' to [000000]

#print "[c][i][b]" + new + msgb + "\n"#
- This prints all the pre-tag
