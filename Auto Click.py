#import modules
import subprocess
import os
import time
import ctypes
import ctypes.wintypes
import pyautogui


# This function is designed to open an application given its root-folder and application name.
# If the file does not exist, a 'FileNotFoundError' is raised and a user-friendly message is shown.
# Any errors will be caught and its error message shown.
def open_app(folder_path, app_name):
    app_path = os.path.join(folder_path, app_name)
    try:
        subprocess.Popen(app_path)
    except FileNotFoundError:
        print(f"The application '{app_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# specify folder where all .exe are found
folder_path1 = " "#folder path
# First App
app_name1 = " "#app name goes here. It is the .exe file you want to run
open_app(folder_path1, app_name1)

# Second App
folder_path2 = " " #folder path
# specify the second app to be opened
app_name2 = " "#app name goes here. It is the .exe file you want to run
open_app(folder_path2, app_name2)

time.sleep(4)

# Get the active window handles.
hwnds = []
EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

def foreach_window(hwnd, lParam):
    hwnds.append(hwnd)
    return True

EnumWindows(EnumWindowsProc(foreach_window), 0)

for hwnd in hwnds:
    # Get the window title
    title_length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
    title = ctypes.create_unicode_buffer(title_length + 1)
    ctypes.windll.user32.GetWindowTextW(hwnd, title, title_length + 1)

    # Check if the 'app_name' word is in the title
    if 'app_name' in title.value:
        # Resize the window to fit the title
        rect = ctypes.wintypes.RECT()
        ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
        ctypes.windll.user32.MoveWindow(hwnd, 1043, 406, 882, 639, True)

time.sleep(2)

# this clicks on the screen at the specified coordinates
pyautogui.click(959, 674, button="left")

time.sleep(2)

#END STATEMENTS
#Confirmation box
msg = "Everything is good to go, Have a great Sunday!"
title = "Go Live!"

#output
ctypes.windll.user32.MessageBoxW(0, msg, title, 0)

sys.exit()