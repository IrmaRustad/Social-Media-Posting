from imports import sqlite3, obtener_metadata_video, dividir_metadata, obtener_hora_fecha
from OpenChrome import abrirChromeYSeleccionarPerfil

def TiktokPost(video_id):
    #Post auto uploader for LinkedIn
    import pyautogui
    import time
    

    cursor.execute("SELECT tblClient.ChromeTabs, tblClient.ClName , videos.social_media FROM videos JOIN tblClient ON videos.ClName = tblClient.ClName WHERE videos.id = ?", (video_id,))
    ChromeTabs, ClName,social_media = cursor.fetchone()

    resultado = cursor.fetchone()
    if resultado:
        ChromeTabs, ClName, social_media = resultado

    abrirChromeYSeleccionarPerfil(ChromeTabs, social_media)

    conexion = sqlite3.connect('C:/Users/irma/OneDrive/Skrivebord/Instagram-Posting/ig/videos.db')
    cursor = conexion.cursor()

    pyautogui.press('tab', presses=12,interval=0.5)

    pyautogui.press("enter")
    

    metadata_video = obtener_metadata_video(cursor,video_id)

    # Dividir metadata en variables
    description, videoname, videoType = dividir_metadata(metadata_video)

    fecha,horas, minutos, AMoPM = obtener_hora_fecha(cursor, video_id)

    pyautogui.hotkey("ctrl", "l")

    pyautogui.write("C:/Users/irma/Downloads/pyauto/instagram")

    pyautogui.hotkey("enter")

    pyautogui.press('tab', presses=5)

    pyautogui.write(videoname)

    pyautogui.hotkey("down")

    pyautogui.press("enter")

    pyautogui.press('tab', presses=2)

    time.sleep(15)

    pyautogui.press('delete', presses=10)

    pyautogui.write(description)

    pyautogui.press('tab', presses=6)

    pyautogui.hotkey("space")

    















