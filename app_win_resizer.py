# import modules
import ctypes
import ctypes.wintypes

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
