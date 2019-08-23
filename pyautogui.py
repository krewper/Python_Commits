#Author: Aditya Sethi
#Script to move the mouse pointer and select the first open tab

import pyautogui
print(pyautogui.size())
def position():
    print(pyautogui.position())

pyautogui.moveTo(50, 20, duration = 1)
position()

pyautogui.click()
