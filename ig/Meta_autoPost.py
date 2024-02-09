import pyautogui
import time
import pyperclip
import sqlite3
from instagramStory import publicarStory
from instagramReel import publicarReel
from instagramPost import publicarPost



def autoPostMeta(video_id):
    conexion = sqlite3.connect('C:/Users/irma/OneDrive/Skrivebord/Instagram-Posting/ig/videos.db')  # Asegúrate de cambiar la ruta según sea necesario
    cursor = conexion.cursor()

    # Realizar una sola consulta para obtener todos los campos necesarios
    cursor.execute(f"SELECT description, name, type FROM videos WHERE id={video_id};")
    metadata_video = cursor.fetchone()

    # Verificar si se obtuvieron resultados
    if metadata_video:
        description, videoname, videoType = metadata_video

    else:
        print("Video no encontrado o falta información.")
    
    # Cerrar la conexión
    conexion.close()


    # Lógica para abrir Chrome y navegar a Facebook Business
    abrirChromeYFacebookBusiness()

    # Lógica para seleccionar el tipo de publicación basada en video_type
    if videoType == 'story':
        publicarStory(videoname, description)
    elif videoType == 'post':
        publicarPost(videoname, description)
    elif videoType == 'reel':
        publicarReel(videoname, description)
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







# Ejemplo de uso
autoPostMeta(4)
