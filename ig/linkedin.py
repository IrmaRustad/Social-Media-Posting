  
def LinkedinPost(video_id):


    


    #Post auto uploader for LinkedIn
    import pyautogui
    import time
    import sqlite3
    from conectar_bd import obtener_metadata_video, dividir_metadata, obtener_hora_fecha


    

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

    #Search for LinkedIn
    pyautogui.hotkey("ctrl", "t")

    url = "https://www.linkedin.com/feed/"
    pyautogui.write(url)
    pyautogui.hotkey("enter")


    conexion = sqlite3.connect('C:/Users/irma/OneDrive/Skrivebord/Social-Media-Posting-main 13022024/Social-Media-Posting-main/ig/videos.db')
    cursor = conexion.cursor()
    


    metadata_video = obtener_metadata_video(cursor,video_id)

    # Dividir metadata en variables
    description, videoname, videoType = dividir_metadata(metadata_video)


    fecha,horas, minutos, AMoPM = obtener_hora_fecha(cursor, video_id)

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



