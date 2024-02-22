import pyautogui
import time

def publicarReel(videoname, description,fecha,horas,minutos,AMoPM):

    pyautogui.press("tab",presses=8, interval=0.8)
    pyautogui.hotkey("enter")

    time.sleep(3)

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
    time.sleep(2)
    pyautogui.hotkey("down")
    pyautogui.hotkey("enter")

    time.sleep(20)

    pyautogui.press("tab",presses=2, interval=0.8)
    
    time.sleep(2)

    pyautogui.write(description)

    time.sleep(2)

    pyautogui.press("tab",presses=4, interval=0.8)
    time.sleep(10)
    pyautogui.hotkey("enter")

    time.sleep(5)

    pyautogui.press("tab",presses=10, interval=0.8)

    pyautogui.hotkey("enter")

    time.sleep(2)

    pyautogui.press("tab",presses=2, interval=0.8)

    pyautogui.hotkey("enter")

    pyautogui.hotkey("tab")

    time.sleep(2)

    pyautogui.hotkey("pageup",presses=3, interval=0.8)
    time.sleep(1)

    pyautogui.hotkey("ctrl","l")
    time.sleep(1)

    pyautogui.press("tab",presses=8, interval=0.8)

    pyautogui.hotkey("enter")

    time.sleep(2)
    pyautogui.press("tab",presses=2, interval=0.8)

    pyautogui.press("backspace",presses=8, interval=0.8)

    time.sleep(1)

    pyautogui.write(fecha)

    pyautogui.press("left" ,presses=10, interval=0.8)

    pyautogui.hotkey("backspace")

    time.sleep(2)

    pyautogui.hotkey("tab")

    pyautogui.write(horas)

    time.sleep(2)

    pyautogui.hotkey("tab")

    time.sleep(2)

    pyautogui.write(minutos)

    time.sleep(2)

    pyautogui.hotkey("tab")

    time.sleep(2)

    pyautogui.write(AMoPM)

    time.sleep(2)

    pyautogui.press("tab",presses=13, interval=0.8)

    pyautogui.hotkey("enter")








