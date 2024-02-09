

import pyautogui
import time
import pyperclip
import sqlite3



def subir_video_instagram(video_id) : 

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
    url = "https://www.instagram.com/"

    pyautogui.write(url)
    pyautogui.hotkey("enter")
    time.sleep(4)

    pyautogui.press("tab",presses=8, interval=0.8)
    pyautogui.hotkey("enter")

    time.sleep(2)

    pyautogui.press("tab",presses=1, interval=0.8)
    pyautogui.hotkey("enter")

    time.sleep(2)

    pyautogui.hotkey("ctrl","l")

    time.sleep(2)

    pyautogui.write("C:/Users/irma/Downloads/pyauto/instagram/")
    pyautogui.hotkey("enter")       

    time.sleep(2)

    pyautogui.press("tab",presses=6, interval=0.8)

    time.sleep(2)

    pyautogui.write(videoname + ".mp4")
    pyautogui.hotkey("enter")

    time.sleep(4)

    pyautogui.press("tab",presses=3, interval=0.8)
    pyautogui.hotkey("enter")

    time.sleep(4)           

    pyautogui.press("tab",presses=7, interval=0.8)
    pyautogui.hotkey("enter")

    time.sleep(4)

    pyautogui.press("tab",presses=6, interval=0.8)
    pyautogui.hotkey("enter")

    time.sleep(4)
    #--------------------------------------------------------------
    pyautogui.press("tab",presses=2, interval=0.8)
    pyautogui.hotkey("enter")

    time.sleep(4)
    pyautogui.press("tab",presses=4, interval=0.8)
    pyautogui.write(description)

    time.sleep(4)

    pyautogui.press("tab",presses=6, interval=0.8)
    pyautogui.hotkey("enter")


    time.sleep(4)           


    time.sleep(60)         

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





    #buscar youtube
    url = "https://www.instagram.com/"

    pyautogui.write(url)
    pyautogui.hotkey("enter")
    time.sleep(4)


    pyautogui.press("tab",presses=9,interval=0.8)               
    pyautogui.hotkey("enter")

    time.sleep(6)

    pyautogui.press("tab",presses=10,interval=0.6)
    pyautogui.hotkey("enter")




    # Espera unos segundos antes de empezar (ajusta según sea necesario)
    time.sleep(5)

    # Simula la combinación de teclas para seleccionar la barra de direcciones del navegador
    pyautogui.hotkey('ctrl', 'l')

    # Espera un breve momento antes de realizar la combinación para copiar al portapapeles
    time.sleep(1)

    # Simula la combinación de teclas para copiar al portapapeles (Ctrl + C)
    pyautogui.hotkey('ctrl', 'c')

    # Espera un momento para que se copie al portapapeles
    time.sleep(1)

    # Obtiene el contenido del portapapeles con pyperclip
    enlace_copiado = pyperclip.paste()

    # Imprime el enlace copiado en la consola
    print("Enlace copiado:", enlace_copiado)

    update_enlace = f"UPDATE videos SET posted='POSTED' , url = enlace_copiado WHERE id={video_id};"


    conexion.close()


