import pyautogui
import time

def publicarReel(videoname, description):

    pyautogui.press("tab",presses=7, interval=0.8)
    pyautogui.hotkey("enter")

    time.sleep(2)

    pyautogui.press("tab",presses=3, interval=0.8)
    pyautogui.hotkey("enter")

    time.sleep(2)

    pyautogui.hotkey('ctrl', 'l')

    pyautogui.write("C:/Users/irma/Downloads/pyauto/instagram")
    pyautogui.hotkey("enter")
   

    time.sleep(2)

    pyautogui.press("tab",presses=5, interval=0.8)

    time.sleep(2)

    pyautogui.write(videoname)
    pyautogui.hotkey("enter")
    pyautogui.hotkey("enter")

    time.sleep(2)

    pyautogui.press("tab",presses=3, interval=0.8)
    
    time.sleep(2)

    pyautogui.write(description)

    time.sleep(2)

    pyautogui.press("tab",presses=3, interval=0.8)
    pyautogui.hotkey("enter")

    time.sleep(4)

    pyautogui.press("tab",presses=10, interval=0.8)

    pyautogui.hotkey("enter")

    time.sleep(4)


    pyautogui.press("tab",presses=2, interval=0.8)

    pyautogui.hotkey("enter")

    time.sleep(4)

    pyautogui.press("tab",presses=1, interval=0.8)

    pyautogui.hotkey("enter")

    


