
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
    from OpenChrome import abrirChromeYSeleccionarPerfil

    conexion = sqlite3.connect('C:/Users/irma/OneDrive/Skrivebord/Instagram-Posting/ig/videos.db')
    cursor = conexion.cursor()
    


    metadata_video = obtener_metadata_video(cursor,video_id)

    # Dividir metadata en variables
    description, videoname, videoType,VideoTitle = dividir_metadata(metadata_video)


    fecha,horas, minutos, AMoPM = obtener_hora_fecha(cursor, video_id)

    cursor.execute("SELECT tblClient.ChromeTabs, tblClient.ClName , videos.social_media FROM videos JOIN tblClient ON videos.ClName = tblClient.ClName WHERE videos.id = ?", (video_id,))
    ChromeTabs, ClName,social_media = cursor.fetchone()

    resultado = cursor.fetchone()
    if resultado:
        ChromeTabs, ClName, social_media = resultado

    


    abrirChromeYSeleccionarPerfil(ChromeTabs, social_media)

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

    pyautogui.press('delete', presses=20)
    time.sleep(2)
    pyautogui.write(VideoTitle)

    time.sleep(3)

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



    
    conexion.close()




    

    


   

    


