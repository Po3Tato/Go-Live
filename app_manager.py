# import modules
import os
import subprocess

def find_app(app_name):
    search_directories = [
        "C:\\Program Files",
        "C:\\Program Files (x86)",
        os.path.expanduser("~\\AppData\\Local\\Programs"),
        os.path.expanduser("~\\AppData\\Roaming")
    ]
    # search application in given directories
    for directory in search_directories:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower() == app_name.lower():
                    return os.path.join(root, file)
    return None

# open applications when found
def open_app(app_name):
    app_path = find_app(app_name)
    if app_path is None:
        print(f"The application '{app_name}' was not found.")
        return
    try:
        subprocess.Popen(app_path)
    except Exception as e:
        print(f"An error occurred: {e}")
