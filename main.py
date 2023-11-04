# import modules
import os
import time
import app_manager
import app_win_resizer
import ctypes
import sys
import subprocess

# launche OBS with correct working directory. this is because OBS doesn't like being ran from outside the current working directory.
def launch_obs():
    # change the working directory to the OBS installation directory and open it
    os.chdir(r"C:\\Program Files\\obs-studio\\bin\\64bit")
    subprocess.Popen('obs64.exe')

# call the function to launch OBS
launch_obs()

# open apps by name
app_manager.open_app('Zoom.exe')

# resize apps
app_win_resizer.resize_app('Zoom', -16, 400, 906, 639)  # Bottom-right
app_win_resizer.resize_app('OBS', -8, 4, 889, 622)     # top-right

time.sleep(5)

# END STATEMENTS
# confirmation box
msg = 'Everything is good to go, Have a great Sunday!'
title = 'Go Live!'

# output
ctypes.windll.user32.MessageBoxW(0, msg, title, 0)

sys.exit()
