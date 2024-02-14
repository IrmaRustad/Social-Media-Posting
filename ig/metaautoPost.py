import pyautogui
import time
import pyperclip
import sqlite3
from datetime import datetime
from conectar_bd import obtener_metadata_video, cerrar_bd, dividir_metadata
from conectar_bd import obtener_hora_fecha




def autoPostMeta(video_id):

    from MetaStory import publicarStory
    from MetaReel import publicarReel
    from MetaPost import publicarPost
    


    # Lógica para abrir Chrome y navegar a Facebook Business
    abrirChromeYFacebookBusiness()

    conexion = sqlite3.connect('C:/Users/irma/OneDrive/Skrivebord/Social-Media-Posting-main 12022024/Social-Media-Posting-main/ig/videos.db')
    cursor = conexion.cursor()

    metadata_video = obtener_metadata_video(cursor,video_id)

    # Dividir metadata en variables
    description, videoname, videoType = dividir_metadata(metadata_video)


    fecha,horas, minutos, AMoPM = obtener_hora_fecha(cursor, video_id)


   

    # Verificar si se obtuvieron resultados

    # Lógica para seleccionar el tipo de publicación basada en video_type
    if videoType == 'story':
        publicarStory(videoname,fecha,horas,minutos,AMoPM)
        print(fecha)
        print(horas)
        print(minutos) 
    elif videoType == 'post':
        publicarPost(videoname, description,fecha,horas,minutos,AMoPM)
    elif videoType == 'reel':
        publicarReel(videoname, description,fecha,horas,minutos,AMoPM)
    else:
        print("Tipo de video no soportado.")

def abrirChromeYFacebookBusiness():
    
    #abrir barra de busqueda y buscar "Google Chrome"
    pyautogui.hotkey("winleft", "s")
    time.sleep(1)

    #Escribe chrome y abre  
    pyautogui.write("Chrome")
    pyautogui.hotkey("enter")
    time.sleep(3)

    #Si hay varios usuarios, selecciona el primero y enter
    pyautogui.hotkey("tab", "enter")
    time.sleep(1)
    #abre nueva ventana de navegador
    pyautogui.hotkey("ctrl", "t")
    time.sleep(1)



    #buscar youtube
    url = "https://business.facebook.com/latest/home"

    pyautogui.write(url)
    pyautogui.hotkey("enter")
    time.sleep(4)






