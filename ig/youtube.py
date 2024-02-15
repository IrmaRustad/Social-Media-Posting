
def YoutubePost(video_id):

    #pip install pyautogui
    #-----------------------------------------------
    import pyautogui
    import time
    import sqlite3
    import tkinter as tk
    import pyperclip
    import re
    from conectar_bd import obtener_metadata_video, dividir_metadata, obtener_hora_fecha

    conexion = sqlite3.connect('C:/Users/irma/OneDrive/Skrivebord/Social-Media-Posting-main 13022024/Social-Media-Posting-main/ig/videos.db')
    cursor = conexion.cursor()
    


    metadata_video = obtener_metadata_video(cursor,video_id)

    # Dividir metadata en variables
    description, videoname, videoType = dividir_metadata(metadata_video)


    fecha,horas, minutos, AMoPM = obtener_hora_fecha(cursor, video_id)

    #Open search bar
    pyautogui.hotkey("winleft", "s")    
    time.sleep(1)

    #Write "Chrome" and press enter
    pyautogui.write("Chrome")
    pyautogui.hotkey("enter")
    time.sleep(3)

    #If there is different users, select the user                             
    pyautogui.hotkey("tab", "enter")
    time.sleep(2)

    #Open new tab
    pyautogui.hotkey("ctrl", "t")
    time.sleep(1)

    #Search for Youtube
    url = "https://www.youtube.com/"

    pyautogui.write(url)
    pyautogui.hotkey("enter")
    time.sleep(6)

    pyautogui.press('tab', presses=7)
    pyautogui.press("space", presses=2, interval=1)

    time.sleep(3)

    pyautogui.press('tab', presses=3)
    pyautogui.press("space")
    time.sleep(3)

    pyautogui.press("tab", presses=5)
    time.sleep(3)
    pyautogui.press("space")


    #Search for specific url in file manager
    pyautogui.write("C:/Users/irma/Downloads/pyauto/instagram")
    pyautogui.hotkey("enter")
                                
    time.sleep(3)

    pyautogui.press("tab", presses=5)

    time.sleep(3)

   
    pyautogui.write(videoname)
    time.sleep(3)


    pyautogui.hotkey("down")

    time.sleep(3)

    pyautogui.press("enter")

    time.sleep(5)

    pyautogui.press('tab', presses=2,interval=0.5)

    time.sleep(3)

    pyautogui.write(description)
    time.sleep(3)

    pyautogui.press("tab", presses=5,interval=0.5)

    time.sleep(3)

    pyautogui.hotkey("down")

    time.sleep(3)

    pyautogui.press("tab", presses=5,interval=0.5)

    pyautogui.hotkey("enter")
    pyautogui.hotkey("enter")
    time.sleep(3)

    pyautogui.hotkey("enter")

    pyautogui.press("tab", presses=13,interval=0.5)


    time.sleep(3)

    pyautogui.press("down", presses=2,interval=0.5)

    time.sleep(3)

    pyautogui.hotkey("enter")

    pyautogui.press("tab", presses=3,interval=0.5)

    pyautogui.hotkey("enter")

    time.sleep(3)

    pyautogui.hotkey("tab")
    pyautogui.hotkey("enter")

    time.sleep(3)

    pyautogui.press("backspace", presses=11,interval=0.5)

    pyautogui.write(fecha)

    time.sleep(3)

    pyautogui.hotkey("enter")

    time.sleep(3)

    pyautogui.press("tab", presses=4,interval=0.5)

    pyautogui.press("backspace", presses=10,interval=0.5)

    pyautogui.write(horas)

    pyautogui.write(":")

    pyautogui.write(minutos)

    pyautogui.hotkey("enter")

    time.sleep(20)

    pyautogui.press("tab", presses=13,interval=0.5)

    pyautogui.hotkey("enter")

    time.sleep(3)


    pyautogui.press("tab", presses=2,interval=0.5)

    pyautogui.hotkey("enter")

    time.sleep(2)

    YoutubePostUrl = pyperclip.paste()

    cursor.execute(f"UPDATE videos SET url='{YoutubePostUrl}' WHERE id={video_id};")








    

    


   

    


