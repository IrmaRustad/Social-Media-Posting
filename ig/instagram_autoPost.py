

import pyautogui
import time
import pyperclip

                                    

def subir_video_instagram() : 

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


    Video_name = pyautogui.prompt(text="", title="Ingresa el nombre del video")
    video_description = pyautogui.prompt(text="", title="Ingresa el nombre del video")

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

    pyautogui.write("C:/Users/Eze Martin/Downloads/pyauto/instagram/")

    time.sleep(2)

    pyautogui.press("tab",presses=5, interval=0.8)

    time.sleep(2)

    pyautogui.write(Video_name + ".mp4")
    pyautogui.hotkey("enter")

    time.sleep(4)

    #--------------------------------------------------------- esta bien  ^
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
    pyautogui.write(video_description)

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