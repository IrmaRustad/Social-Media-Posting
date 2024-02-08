import pyautogui
import time
import pyperclip
import sqlite3

def autoPostMeta(video_id):
    conexion = sqlite3.connect('C:/Users/irma/OneDrive/Skrivebord/Instagram-Posting/ig/videos.db')  # Asegúrate de cambiar la ruta según sea necesario
    cursor = conexion.cursor()

    # Realizar las consultas y extraer los resultados uno por uno
    cursor.execute(f"SELECT description FROM videos WHERE id={video_id};")
    consulta_description = cursor.fetchone()  # Extraer descripción
    cursor.execute(f"SELECT name FROM videos WHERE id={video_id};")
    consulta_videoname = cursor.fetchone()  # Extraer nombre del video
    cursor.execute(f"SELECT type FROM videos WHERE id={video_id};")
    consulta_videoType = cursor.fetchone()  # Extraer tipo de video
    cursor.execute(f"SELECT hora FROM videos WHERE id={video_id};")
    consulta_hora = cursor.fetchone()  # Extraer hora de publicación
    cursor.execute(f"SELECT fecha FROM videos WHERE id={video_id}")
    consulta_fecha = cursor.fetchone()  # Extraer fecha de publicación

    # Verificar si se obtuvieron resultados
    if consulta_description and consulta_videoname and consulta_videoType and consulta_hora and consulta_fecha:
        description = consulta_description[0]
        videoname = consulta_videoname[0]
        videoType = consulta_videoType[0]
        hora = consulta_hora[0]
        horas, minutos = hora.split(':')
        fecha = consulta_fecha[0]
    else:
        print("Video no encontrado o falta información.")
        return
    


    # Lógica para abrir Chrome y navegar a Facebook Business
    abrirChromeYFacebookBusiness()

    # Lógica para seleccionar el tipo de publicación basada en video_type
    if videoType == 'story':
        publicarStory(videoname, description,horas,fecha,minutos)
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


def publicarStory(videoname, description,horas,fecha,minutos):
    pyautogui.press("tab",presses=9, interval=0.8)
    pyautogui.hotkey("enter")

    time.sleep(4)

    pyautogui.press("tab",presses=2, interval=0.8)
    pyautogui.hotkey("enter")

    time.sleep(4)

    pyautogui.hotkey("ctrl", "l")

    time.sleep(2)

    pyautogui.write("C:/Users/irma/Downloads/pyauto/instagram")
    pyautogui.hotkey("enter")

    time.sleep(2)

    pyautogui.press("tab",presses=5, interval=0.8)

    time.sleep(2)

    pyautogui.write(videoname)
    time.sleep(2)
    pyautogui.press("enter",presses=2, interval=0.8)


    
    time.sleep(3)


    pyautogui.press("tab",presses=6, interval=0.8)
    time.sleep(2)
    pyautogui.hotkey("enter")

    pyautogui.press("tab",presses=2, interval=0.8)

    pyautogui.press("backspace",presses=8, interval=0.8)
    time.sleep(2)
    pyautogui.write(fecha)
    time.sleep(2)
    pyautogui.hotkey("tab")
    time.sleep(2)
    pyautogui.write(horas)
    time.sleep(2)
    pyautogui.hotkey("tab")
    pyautogui.write(minutos)





def publicarPost(videoname, description):
    # Tu código para publicar un post
    pass

def publicarReel(videoname, description):
    # Tu código para publicar un reel
    pass

# Ejemplo de uso
autoPostMeta(4)
