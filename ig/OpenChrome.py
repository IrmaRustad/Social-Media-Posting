import pyautogui
import sqlite3
import time

def abrirChromeYSeleccionarPerfil(ChromeTabs, social_media):
    # Suponiendo que 'db_path' es la ruta a tu archivo de base de datos SQLite
    db_path = 'C:/Users/irma/OneDrive/Skrivebord/Instagram-Posting/ig/videos.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Recuperar la URL de la red social
    cursor.execute("SELECT RedSocialUrl FROM TblSocialMediaUrls WHERE RedSocialName = ?", (social_media,))
    url = cursor.fetchone()[0]
    
    # Abre la barra de búsqueda y busca "Google Chrome"
    pyautogui.hotkey("winleft", "s")
    time.sleep(1)
    pyautogui.write("Chrome")
    pyautogui.hotkey("enter")
    time.sleep(3)

    # Utiliza el valor de ChromeTabs para seleccionar el perfil correcto
    for _ in range(ChromeTabs):
        pyautogui.press('tab')
        time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)

    # Abre una nueva ventana de navegador y navega a la URL
    pyautogui.hotkey("ctrl", "t")
    time.sleep(1)
    pyautogui.write(url)
    pyautogui.press('enter')
    time.sleep(4)

    conn.close()