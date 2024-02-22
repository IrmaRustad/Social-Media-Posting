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
    from OpenChrome import abrirChromeYSeleccionarPerfil

    # Lógica para abrir Chrome y navegar a Facebook Business
    conexion = sqlite3.connect('C:/Users/irma/OneDrive/Skrivebord/Instagram-Posting/ig/videos.db')
    cursor = conexion.cursor()

    metadata_video = obtener_metadata_video(cursor,video_id)

    # Dividir metadata en variables
    description, videoname, videoType,VideoTitle,VideoCover = dividir_metadata(metadata_video)

    fecha,horas, minutos, AMoPM = obtener_hora_fecha(cursor, video_id)

    cursor.execute("SELECT tblClient.ChromeTabs, tblClient.ClName , videos.social_media FROM videos JOIN tblClient ON videos.ClName = tblClient.ClName WHERE videos.id = ?", (video_id,))
    ChromeTabs, ClName,social_media = cursor.fetchone()

    resultado = cursor.fetchone()
    if resultado:
        ChromeTabs, ClName, social_media = resultado

    abrirChromeYSeleccionarPerfil(ChromeTabs, social_media)

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

    conexion.close()