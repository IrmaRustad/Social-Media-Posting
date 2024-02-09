import sqlite3
import schedule
import time
from datetime import datetime
from instagram_autoPost import subir_video_instagram
from tiktok import subir_video_tiktok
from linkedin import subir_video_linkedin
from x import subir_video_x 

def cargar_video(video_id, social_media):
    print(f"Ejecutando script de carga de video para Video ID {video_id} en {social_media}") # Mensaje para depuración
    if social_media == 'Meta':
        subir_video_instagram(video_id)
    elif social_media == 'TikTok':
        subir_video_tiktok(video_id)
    elif social_media == 'LinkedIn':
        subir_video_linkedin(video_id)
    elif social_media == 'X':
        subir_video_x(video_id)

# Conectar a la base de datos
conexion = sqlite3.connect('C:/Users/irma/OneDrive/Skrivebord/Instagram-Posting/ig/videos.db')
cursor = conexion.cursor()

# Consulta SELECT para obtener videos con estado 'NOT_POSTED' y hora programada
consulta_select = "SELECT id, name, description, social_media, posted_hour, posted FROM videos WHERE posted='NOT_POSTED';"
cursor.execute(consulta_select)

# Obtener los resultados y filtrar por estado NOT_POSTED
videos_por_programar = [video for video in cursor.fetchall() if video[-1] == 'NOT_POSTED']

# Procesar cada video y programar su carga
for video in videos_por_programar:
    video_id, video_nombre, _, social_media, hora_programada_str, _ = video
    hora_programada = datetime.strptime(hora_programada_str, '%Y-%m-%d %H:%M:%S')

    # Programar la carga de video a la hora programada utilizando el script adecuado según la red social
    schedule.every().day.at(hora_programada.strftime('%H:%M')).do(cargar_video, video_id=video_id, social_media=social_media)

# Ejecutar el loop principal para verificar y ejecutar tareas programadas
while True:
    schedule.run_pending()
    time.sleep(1)

# Cerrar la conexión
conexion.close()




