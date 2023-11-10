# import modules
import os
import time
import ctypes
import subprocess
from dotenv import load_dotenv

# Before running the code make sure you update .env accordingly
# Load environment variables
load_dotenv()

# Retrieve Zoom meeting details
ZOOM_MEETING_ID = os.getenv("ZOOM_MEETING_ID")
ZOOM_MEETING_PASSWORD = os.getenv("ZOOM_MEETING_PASSWORD")

# launche OBS with correct working directory.
# this is because OBS doesn't like being ran from
# outside the current working directory.
def launch_obs():
    os.chdir(r"C:\\Program Files\\obs-studio\\bin\\64bit")
    subprocess.Popen('obs64.exe')

# Launch Zoom meeting using the meeting ID and password
def launch_zoom(meeting_id, password):
    zoom_url = f"zoommtg://zoom.us/join?action=join&confno={meeting_id}&pwd={password}"
    subprocess.Popen(["start", zoom_url], shell=True)

# Function to resize an app window
def resize_app(app_name, x, y, width, height):
    hwnds = []
    EnumWindows = ctypes.windll.user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

    def foreach_window(hwnd, lParam):
        hwnds.append(hwnd)
        return True

    EnumWindows(EnumWindowsProc(foreach_window), 0)
    for hwnd in hwnds:
        title_length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
        title = ctypes.create_unicode_buffer(title_length + 1)
        ctypes.windll.user32.GetWindowTextW(hwnd, title, title_length + 1)
        if app_name in title.value:
            ctypes.windll.user32.MoveWindow(hwnd, x, y, width, height, True)

# Main execution flow
def main():
    launch_obs()
    launch_zoom(ZOOM_MEETING_ID, ZOOM_MEETING_PASSWORD)

    time.sleep(5)

    resize_app('Zoom', -16, 400, 906, 639)
    resize_app('OBS', -8, 4, 889, 622)

    # Confirmation box
    msg = 'Everything is good to go, Have a great Sunday!'
    title = 'Go Live!'
    ctypes.windll.user32.MessageBoxW(0, msg, title, 0)

    sys.exit()

if __name__ == "__main__":
    main()
