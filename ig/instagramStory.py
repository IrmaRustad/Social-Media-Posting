import pyautogui
import time


def publicarStory(videoname, description,horas,fecha,minutos):
    
    pyautogui.press("tab",presses=8, interval=0.8)
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

    pyautogui.press("tab",presses=5, interval=0.8)

    time.sleep(2)

    pyautogui.write(videoname)
    time.sleep(2)
    pyautogui.press("enter",presses=2, interval=0.8)

    time.sleep(60)

    pyautogui.press("tab",presses=8, interval=0.8)
    pyautogui.hotkey("enter")


    