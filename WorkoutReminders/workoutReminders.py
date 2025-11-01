# import pygetwindow as gw
import pyautogui
import time
import os

os.startfile("whatsapp://send?phone=19176126688")
time.sleep(5)
# searchBoxPic = "Data\\chats.png"
# searchBoxLoc = pyautogui.locateCenterOnScreen(searchBoxPic)
# pyautogui.click(searchBoxLoc)

pyautogui.keyDown("ctrl")
pyautogui.press('f')
pyautogui.keyUp("ctrl")
pyautogui.write("Woodmont Workouts")