# import pygetwindow as gw
import pyautogui
import time
import os

os.startfile("whatsapp://send?phone=19176126688")
time.sleep(5)



pyautogui.keyDown("ctrl")
pyautogui.press('f')
pyautogui.keyUp("ctrl")
# clears textbox
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')

# search for workout class
pyautogui.write("Woodmont Workouts")

# click into appropriate chat
pyautogui.press('tab')
pyautogui.press('enter')

# write message

