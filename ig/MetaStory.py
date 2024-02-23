from imports import pyautogui, time

def publicarStory(videoname,fecha,horas,minutos,AMoPM):
    
    pyautogui.press("tab",presses=9, interval=0.8)
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
    pyautogui.hotkey("down")
    pyautogui.hotkey("enter")

    time.sleep(30)

    pyautogui.press("tab",presses=6, interval=0.8)
    pyautogui.hotkey("enter")   

    time.sleep(2)

    pyautogui.hotkey("tab")
    pyautogui.press("backspace",presses=9, interval=0.8)
    time.sleep(2)
    pyautogui.write(fecha)
    time.sleep(2)
    pyautogui.hotkey("tab")
    time.sleep(2)
    pyautogui.write(horas)
    time.sleep(2)
    pyautogui.hotkey("tab")
    pyautogui.write(minutos)
    pyautogui.hotkey("tab")
    pyautogui.write(AMoPM)
    pyautogui.hotkey("tab")

    pyautogui.press("backspace",presses=9, interval=0.8)
    time.sleep(2)
    pyautogui.write(fecha)
    time.sleep(2)
    pyautogui.hotkey("tab")
    time.sleep(2)
    pyautogui.write(horas)
    time.sleep(2)
    pyautogui.hotkey("tab")
    pyautogui.write(minutos)
    pyautogui.hotkey("tab")
    pyautogui.write(AMoPM)
    time.sleep(2)

    time.sleep(15)
    pyautogui.press("tab",presses=5, interval=0.8)
    pyautogui.hotkey("enter")