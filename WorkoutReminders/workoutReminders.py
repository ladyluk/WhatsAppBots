# import pygetwindow as gw
# import pyautogui
# import win32gui
# import win32con
# import subprocess

# subprocess.Popen(["cmd", "/C", "start whatsapp://send?phone=19178866195"], shell=True)

import os

os.startfile("whatsapp://send?phone=19176126688")

# def bring_to_front(window_title):
#     hwnd = win32gui.FindWindow(None, window_title)
#     if hwnd:
#         win32gui.SetForegroundWindow(hwnd)
#         win32gui.ShowWindow(hwnd, win32con.SW_RESTORE) # Restore if minimized
#     else:
#         print(f"Window with title '{window_title}' not found.")


# bring_to_front("WhatsApp") # Replace with your window's title

# windows = gw.getAllWindows()

# for window in windows:
#     print("activating "+ window.title)
#     if window.title == "WhatsApp":
#         bring_to_front(window.title) # Replace with your window's title
#         break