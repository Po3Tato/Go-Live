import os
import ctypes.wintypes
import pyautogui
import time

def search_and_open_app(app_name):
    # Search for the app in the C: drive
    for root, dirs, files in os.walk('C:\\'):
        if app_name in files:
            # Found the app - open it using the default application
            os.startfile(os.path.join(root, app_name))
            return

# Open applications
search_and_open_app("app_name.lnk") # this has to be an icon on the screen

time.sleep(5)

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

time.sleep(5)

# this clicks on the screen at the specified coordinates
pyautogui.click(959, 674, button="left")

time.sleep(5)

sys.exit()