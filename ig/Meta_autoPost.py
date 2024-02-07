
import pyautogui
import time
import pyperclip
import sqlite3



def autoPostMeta(video_id):


    conexion = sqlite3.connect('C:/Users/irma/Downloads/ig/videos.db')  # Cambiar la ruta y el nombre del archivo de base de datos  según sea necesario
    cursor = conexion.cursor()

    

    consulta_description = f"SELECT description FROM videos WHERE id={video_id};"
    consulta_videoname = f"SELECT name FROM videos WHERE id={video_id};"
    

    cursor.execute(consulta_description)

    consulta_description = cursor.fetchone() 

    cursor.execute(consulta_videoname)

    consulta_videoname = cursor.fetchone()

    # Extraer los valores de las tuplas
    description = consulta_description[0] if consulta_description else ""
    videoname = consulta_videoname[0] if consulta_videoname else ""

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

    pyautogui.press("tab",presses=9, interval=0.8)
    pyautogui.hotkey("enter")

    time.sleep(4)

    pyautogui.press("tab",presses=2, interval=0.8)
    pyautogui.hotkey("enter")

    time.sleep(4)

    pyautogui.hotkey("ctrol", "l")

    time.sleep(2)

    pyautogui.write("C:/Users/irma/Downloads/pyauto/instagram")
    pyautogui.hotkey("enter")

    time.sleep(2)

    pyautogui.press("tab",presses=5, interval=0.8)

    pyautogui.write("C:/Users/irma/Downloads/pyauto/instagram")
   
    




autoPostMeta()                


