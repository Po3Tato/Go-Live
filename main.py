# import modules
import os
import time
import ctypes
import sys
import subprocess

# launche OBS with correct working directory.
# this is because OBS doesn't like being ran from
# outside the current working directory.
def launch_obs():
    os.chdir(r"C:\\Program Files\\obs-studio\\bin\\64bit")
    subprocess.Popen('obs64.exe')

# Function to find and open an app
def find_app(app_name):
    search_directories = [
        "C:\\Program Files",
        "C:\\Program Files (x86)",
        os.path.expanduser("~\\AppData\\Local\\Programs"),
        os.path.expanduser("~\\AppData\\Roaming")
    ]
    for directory in search_directories:
        for root, dirs, files in os.walk(directory):
            if app_name.lower() in (file.lower() for file in files):
                return os.path.join(root, file)
    return None

def open_app(app_name):
    app_path = find_app(app_name)
    if app_path is None:
        print(f"The application '{app_name}' was not found.")
        return
    try:
        subprocess.Popen(app_path)
    except Exception as e:
        print(f"An error occurred: {e}")

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
    open_app('Zoom.exe')
    time.sleep(5)  # Wait for apps to open
    resize_app('Zoom', -16, 400, 906, 639)  # Bottom-right
    resize_app('OBS', -8, 4, 889, 622)      # top-right

    # Confirmation box
    msg = 'Everything is good to go, Have a great Sunday!'
    title = 'Go Live!'
    ctypes.windll.user32.MessageBoxW(0, msg, title, 0)

    sys.exit()

if __name__ == "__main__":
    main()
