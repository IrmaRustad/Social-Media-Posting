from imports import pyautogui, time

def publicarPost(videoname, description,fecha,horas,minutos,AMoPM):

    pyautogui.press("tab",presses=6, interval=0.8)
    pyautogui.hotkey("enter")

    time.sleep(4)

    pyautogui.press("tab",presses=2, interval=0.8)
    pyautogui.hotkey("enter")
    pyautogui.hotkey("enter")

    time.sleep(4)

    pyautogui.hotkey("ctrl", "l")

    time.sleep(2)

    pyautogui.write("C:/Users/irma/Downloads/pyauto/instagram")
    pyautogui.hotkey("enter")


    pyautogui.press("tab",presses=5, interval=0.8)

    pyautogui.write(videoname + ".PNG")
    pyautogui.hotkey("enter")


    time.sleep(2)

    pyautogui.press("tab",presses=2, interval=0.8)

    pyautogui.write(description)

    time.sleep(2)

    pyautogui.press("tab",presses=11, interval=0.8)
    pyautogui.hotkey("enter")