# import modules
import time
import app_manager
import app_win_resizer
import ctypes
import sys

# open apps by name
app_manager.open_app('Zoom.exe')
app_manager.open_app('OBS Studio (64bit).lnk')

# give some time for apps to open
time.sleep(8)

# resize apps
app_win_resizer.resize_app('Zoom', 1043, 406, 882, 639)
app_win_resizer.resize_app('obs64', 1043, 406, 882, 639)

# END STATEMENTS
# confirmation box
msg = 'Everything is good to go, Have a great Sunday!'
title = 'Go Live!'

# output
ctypes.windll.user32.MessageBoxW(0, msg, title, 0)

sys.exit()
