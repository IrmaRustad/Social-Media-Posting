from imports import sqlite3, obtener_metadata_video, dividir_metadata, obtener_hora_fecha

def TiktokPost(video_id):
    #Post auto uploader for LinkedIn
    import pyautogui
    import time
    
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

    pyautogui.PAUSE = 2.5

    #Search for Tiktok creator center
    url = "https://www.tiktok.com/creator-center/upload?from=upload&lang=en"
    pyautogui.write(url)
    pyautogui.hotkey("enter")

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

    















