


def XPost(video_id):


    import pyautogui
    import time
    import sqlite3
    import tkinter as tk
    import pyperclip
    import re
    from datetime import datetime
    from conectar_bd import obtener_metadata_video, dividir_metadata, obtener_hora_fecha, cambiar_mes_a_texto
    from OpenChrome import abrirChromeYSeleccionarPerfil
    

    conexion = sqlite3.connect('C:/Users/irma/OneDrive/Skrivebord/Instagram-Posting/ig/videos.db')
    cursor = conexion.cursor()
    


    metadata_video = obtener_metadata_video(cursor,video_id)

    # Dividir metadata en variables
    description, videoname, videoType,videoTitle,VideoCover = dividir_metadata(metadata_video)


    fecha,horas, minutos, AMoPM = obtener_hora_fecha(cursor, video_id)


    mes_nombre,dia= cambiar_mes_a_texto(cursor, video_id)


    




    cursor.execute("SELECT tblClient.ChromeTabs, tblClient.ClName , videos.social_media FROM videos JOIN tblClient ON videos.ClName = tblClient.ClName WHERE videos.id = ?", (video_id,))
    ChromeTabs, ClName,social_media = cursor.fetchone()

    resultado = cursor.fetchone()
    if resultado:
        ChromeTabs, ClName, social_media = resultado


    abrirChromeYSeleccionarPerfil(ChromeTabs, social_media)


    pyautogui.press('tab', presses=14,interval=0.5)

    pyautogui.press("enter")

    time.sleep(2)


    pyautogui.write(description)
    
    time.sleep(2)

    pyautogui.press('tab', presses=2,interval=0.5)

    pyautogui.hotkey("enter")

    time.sleep(2)

    pyautogui.hotkey("ctrl", "l")

    pyautogui.write("C:/Users/irma/Downloads/pyauto/instagram")

    time.sleep(2)

    pyautogui.hotkey("enter")

    time.sleep(1)

    pyautogui.press("tab", presses=5,interval=0.5) 

    time.sleep(2)

    pyautogui.write(videoname)
    
    time.sleep(2)

    pyautogui.hotkey("down")

    pyautogui.hotkey("enter")

    time.sleep(1)

    pyautogui.press('tab', presses=3,interval=0.5)

    pyautogui.press("enter")

    pyautogui.press("tab", presses=3,interval=0.5)

    time.sleep(3)

    pyautogui.write(mes_nombre)

    time.sleep(4)


    pyautogui.press("tab")

    time.sleep(3)


    pyautogui.write(str(dia))

    time.sleep(3)

    pyautogui.press("tab", presses=6,interval=0.8)

    time.sleep(2)

    pyautogui.write(horas)

    time.sleep(2)

    pyautogui.press("tab")

    time.sleep(2)

    pyautogui.write(minutos)

    time.sleep(2)

    pyautogui.press("tab", presses=3,interval=0.5)

    pyautogui.hotkey("enter")

    time.sleep(150)

    pyautogui.press("tab", presses=16,interval=0.5)

    pyautogui.hotkey("enter")




   
    













