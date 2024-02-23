from imports import sqlite3, pyautogui, time

conexion = sqlite3.connect('C:/Users/irma/OneDrive/Skrivebord/Instagram-Posting/ig/videos.db')
cursor = conexion.cursor()
def LinkedinPost(video_id):
    
    from imports import obtener_metadata_video, dividir_metadata, obtener_hora_fecha, abrirChromeYSeleccionarPerfil

    cursor.execute("SELECT tblClient.ChromeTabs, tblClient.ClName , videos.social_media FROM videos JOIN tblClient ON videos.ClName = tblClient.ClName WHERE videos.id = ?", (video_id,))
    ChromeTabs, ClName,social_media = cursor.fetchone()

    resultado = cursor.fetchone()
    if resultado:
        ChromeTabs, ClName, social_media = resultado

    abrirChromeYSeleccionarPerfil(ChromeTabs, social_media)

    metadata_video = obtener_metadata_video(cursor,video_id)

    # Dividir metadata en variables
    description, videoname, videoType,VideoTitle,VideoCover = dividir_metadata(metadata_video)

    fecha,horas, minutos, AMoPM = obtener_hora_fecha(cursor, video_id)

    
    pyautogui.press('tab', presses=25,interval=0.5)
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

    pyautogui.press('tab', presses=6 , interval=0.5)

    time.sleep(2)
    pyautogui.hotkey("enter")
    time.sleep(2)
    pyautogui.press('tab', presses=2 , interval=0.8)
    time.sleep(2)
    pyautogui.hotkey("enter")

    time.sleep(2)

    pyautogui.hotkey("ctrl", "l")
    time.sleep(2)
    pyautogui.write("C:/Users/irma/Downloads/pyauto/instagram")
    time.sleep(2)
    pyautogui.hotkey("enter")

    pyautogui.press('tab', presses=5, interval=0.8)
    
    time.sleep(2)

    pyautogui.write(VideoCover)
    time.sleep(2)
    pyautogui.hotkey("down")
    time.sleep(2)   
    pyautogui.hotkey("enter")

    time.sleep(2)

    pyautogui.press('tab', presses=2 , interval=0.8)
    pyautogui.hotkey("enter")

    time.sleep(2)

    pyautogui.press('tab', presses=2 , interval=0.8)
    pyautogui.hotkey("enter")     


    time.sleep(2)
    pyautogui.write(description)

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

    conexion.close()

