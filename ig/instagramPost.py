import pyautogui
import time

def publicarPost(videoname, description):

    pyautogui.press("tab",presses=5, interval=0.8)
    pyautogui.hotkey("enter")

    time.sleep(4)

    pyautogui.press("tab",presses=2, interval=0.8)
    pyautogui.hotkey("enter")

    time.sleep(4)

    pyautogui.hotkey("ctrl", "l")

    time.sleep(2)

    pyautogui.write("C:/Users/irma/Downloads/pyauto/instagram")
    pyautogui.hotkey("enter")

    time.sleep(2)
