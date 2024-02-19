  
def LinkedinPost(video_id):


    


    #Post auto uploader for LinkedIn
    import pyautogui
    import time
    import sqlite3
    from conectar_bd import obtener_metadata_video, dividir_metadata, obtener_hora_fecha
    from OpenChrome import abrirChromeYSeleccionarPerfil


    conexion = sqlite3.connect('C:/Users/irma/OneDrive/Skrivebord/Instagram-Posting/ig/videos.db')
    cursor = conexion.cursor()
    


    metadata_video = obtener_metadata_video(cursor,video_id)

    # Dividir metadata en variables
    description, videoname, videoType = dividir_metadata(metadata_video)


    fecha,horas, minutos, AMoPM = obtener_hora_fecha(cursor, video_id)

    cursor.execute("SELECT tblClient.ChromeTabs, tblClient.ClName , videos.social_media FROM videos JOIN tblClient ON videos.ClName = tblClient.ClName WHERE videos.id = ?", (video_id,))
    ChromeTabs, ClName,social_media = cursor.fetchone()

    resultado = cursor.fetchone()
    if resultado:
        ChromeTabs, ClName, social_media = resultado


    conexion.close()

    abrirChromeYSeleccionarPerfil(ChromeTabs, social_media)

    
    pyautogui.press('tab', presses=27)
    pyautogui.hotkey("enter")

   
    pyautogui.write(description)

    pyautogui.press('tab', presses=2)
    pyautogui.hotkey("enter")

    time.sleep(5)

    pyautogui.hotkey("ctrl", "l")
    time.sleep(2)
    pyautogui.write("C:/Users/irma/Downloads/pyauto/instagram")
    time.sleep(2)
    pyautogui.hotkey("enter")

    pyautogui.press('tab', presses=5, interval=0.8)
    
    time.sleep(2)

    pyautogui.write(videoname)
    time.sleep(2)
    pyautogui.hotkey("down")
    pyautogui.hotkey("enter")

    time.sleep(2)

    pyautogui.press('tab', presses=3 , interval=0.8)
    pyautogui.hotkey("enter")

    time.sleep(2)

    pyautogui.press('tab', presses=5, interval=0.8)
    pyautogui.hotkey("enter")

    pyautogui.press('tab', presses=2, interval=0.8)

    pyautogui.hotkey("backspace")

    pyautogui.write(fecha)

    pyautogui.hotkey("tab")

    pyautogui.write(horas)

    time.sleep(2)

    pyautogui.press('tab' , presses=4, interval=0.8)

    pyautogui.hotkey("enter")

    time.sleep(2)

    pyautogui.hotkey("tab")

    pyautogui.hotkey("enter")



