from BusinessLayer import *



Run()

import subprocess

def OpenOutputFile():
    SW_MINIMIZE = 3
    info = subprocess.STARTUPINFO()
    info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = SW_MINIMIZE
    subprocess.call(['notepad','Output.txt'],startupinfo=info)

OpenOutputFile()

#os.startfile("Output.txt")
