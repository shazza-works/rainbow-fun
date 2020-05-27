#!/data/data/com.termux/files/usr/bin/env python3
import subprocess

def copy2clip(txt):
    cmd='echo \"'+ str(txt) +'\"| termux-clipboard-set ; termux-vibrate'
    return subprocess.check_call(cmd, shell=True)
while 1:
    msg = input("Enter Msg ;")
    my_list = msg.split()
    string = '/'
    my_new_list = [string + x for x in my_list]
    string = ' '.join(my_new_list)
    copy2clip(string)
    print ("Text Copied ^" + "\n")
