

""" #Encuentra la posicion de la imagen en la pantalla; eje X, Y
image = pyautogui.locateOnScreen('capture.png', confidence=0.8)

#Intenta encontrar la posicion de esa imagen en la pantalla
move_mouse = pyautogui.center(image)

#locateCenterOnScreen hace el 2x1 de las ambas de arriba
response = pyautogui.locateCenterOnScreen('capture.png', confidence=0.8)

#Mueve el puntero hacia la posicion guardada en move_mouse
pyautogui.moveTo(move_mouse)

print(image)
print(response)
print(move_mouse) """

 

#-----------------------------------------------

import pyautogui
import time
import pyperclip


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

#llevar al input
#channel_name= pyautogui.prompt(text="", title="Ingresa el nombre del canal")
#print(channel_name)

#Escribir canal
#pyautogui.hotkey("tab", "tab", "tab", "tab")
""" time.sleep(2)
pyautogui.write("Nettskred")
pyautogui.hotkey("enter") """

Video_name = pyautogui.prompt(text="", title="Ingresa el nombre del video")
time.sleep(2)
#Variables de botones
create_video_button = pyautogui.locateCenterOnScreen('C:/Users/Eze Martin/Downloads/pyauto/instagram/Captura.png', confidence=0.9)
time.sleep(2)
print(create_video_button)
time.sleep(2)
pyautogui.moveTo(create_video_button)
pyautogui.click()
time.sleep(2)

upload_video_button = pyautogui.locateCenterOnScreen('C:/Users/Eze Martin/Downloads/pyauto/instagram/subir_button.png', confidence=0.6)

pyautogui.moveTo(upload_video_button)
pyautogui.click()
time.sleep(4)




barra_windows = pyautogui.locateCenterOnScreen('C:/Users/Eze Martin/Downloads/pyauto/instagram/Captura2.png', confidence=0.9)
time.sleep(2)
pyautogui.moveTo(barra_windows)
print(pyautogui.size())
print(pyautogui.position())
pyautogui.click()

time.sleep(4)

pyautogui.write("C:/Users/Eze Martin/Downloads/pyauto/instagram/")
pyautogui.hotkey("enter")
busqueda_archivo = pyautogui.locateCenterOnScreen('C:/Users/Eze Martin/Downloads/pyauto/instagram/Captura3.png', confidence=0.9)
pyautogui.moveTo(busqueda_archivo)
pyautogui.click()
time.sleep(2)
pyautogui.write(Video_name)
pyautogui.hotkey("enter")
time.sleep(4)


pyautogui.press("tab",presses=3,interval=0.8)               
pyautogui.hotkey("enter")
time.sleep(2)
pyautogui.press("tab",presses=2,interval=0.8)               
pyautogui.hotkey("enter")


time.sleep(2)
Boton_Compartir = pyautogui.locateCenterOnScreen('C:/Users/Eze Martin/Downloads/pyauto/instagram/compartir.png', confidence=0.9)
pyautogui.moveTo(Boton_Compartir)
pyautogui.click()

time.sleep(150) 

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




##Accion de buscar en la barra de busqueda
""" search_button = pyautogui.locateCenterOnScreen('search_button.png', confidence=0.9)
print(search_button)
pyautogui.moveTo(search_button)
pyautogui.click()
pyautogui.write("NettSkred")
pyautogui.hotkey("enter")

#pyautogui.moveTo(search_button, 1)
 """





#-----------------------------------------------

""" import time
from selenium import webdriver
import pyautogui


# Input para nombre de canal
channel_name = pyautogui.prompt(text="", title="Ingresa el nombre del canal")
print("Nombre del canal:", channel_name)

# Abre navegador
driver = webdriver.Chrome()
driver.maximize_window() 
time.sleep(1)

# Ir a YouTube
driver.get("https://www.youtube.com/")

# Realizar alguna acción en YouTube (puedes personalizar esto según tus necesidades)
# Por ejemplo, buscar el canal especificado
search_box = driver.find_element("name", "search_query")
search_box.send_keys(channel_name)
search_box.submit()

# Puedes agregar más acciones aquí según lo que quieras hacer en YouTube

# Cerrar el navegador después de un tiempo (puedes ajustar según tus necesidades)
time.sleep(5)
driver.quit()
 """