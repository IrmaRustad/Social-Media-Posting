import sqlite3
import schedule
import time
from datetime import datetime
from instagram_autoPost import subir_video_instagram

def cargar_video(video_id):
    print(f"Ejecutando script de carga de video para Video ID {video_id})") # Mensaje para depuración
    subir_video_instagram(video_id)
    
# Conectar a la base de datos (ajusta la ruta y el nombre de la base de datos según sea necesario)
conexion = sqlite3.connect('C:/Users/irma/Downloads/ig/videos.db')  # Cambiar la ruta y el nombre del archivo de base de datos según sea necesario
cursor = conexion.cursor()

# Consulta SELECT para obtener videos con estado 'NOT_POSTED' y hora programada
consulta_select = "SELECT id, name, description, social_media, posted_hour, posted FROM videos WHERE posted='NOT_POSTED';"
cursor.execute(consulta_select)

# Obtener los resultados
videos_por_programar = cursor.fetchall()

# Procesar cada video y programar su carga
for video in videos_por_programar:
    video_id, video_nombre, _, _, hora_programada_str, _ = video
    hora_programada = datetime.strptime(hora_programada_str, '%Y-%m-%d %H:%M:%S')  # Convertir a objeto datetime

    # Programar la carga de video a la hora programada
    schedule.every().day.at(hora_programada.strftime('%H:%M')).do(cargar_video, video_id=video_id)

# Ejecutar el loop principal para verificar y ejecutar tareas programadas
while True:
    schedule.run_pending()
    time.sleep(1)  # Esperar 1 segundo antes de verificar nuevamente

# Cerrar la conexión
conexion.close()
