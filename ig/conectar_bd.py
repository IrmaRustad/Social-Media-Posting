import sqlite3
from datetime import datetime

def conectar_bd(ruta):
    try:
        conexion = sqlite3.connect(ruta)
        cursor = conexion.cursor()
        return conexion, cursor
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None, None

def cerrar_bd(conexion):
    if conexion:
        conexion.close()

def obtener_videos_no_posteados(cursor):
    try:
        consulta_select = "SELECT id, name, description, social_media, posted_hour, posted FROM videos WHERE posted='NOT_POSTED';"
        cursor.execute(consulta_select)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener videos no posteados: {e}")
        return []

def obtener_metadata_video(cursor, video_id):
    try:
        consulta_select = f"SELECT description, name, type FROM videos WHERE id={video_id};"
        cursor.execute(consulta_select)
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error al obtener metadata del video: {e}")
        return None
    

def dividir_metadata(metadata):
    if metadata:
        description, videoname, videoType = metadata
        return description, videoname, videoType
    else:
        return None, None, None
    
def obtener_hora_fecha(cursor, video_id):
    cursor.execute(f"SELECT hora FROM videos WHERE id={video_id};")
    consulta_hora = cursor.fetchone()  # Extraer hora de publicación
    cursor.execute(f"SELECT fecha FROM videos WHERE id={video_id}")
    consulta_fecha = cursor.fetchone()  # Extraer fecha de publicación
    cursor.execute(f"SELECT AMoPM FROM videos WHERE id={video_id}")
    consulta_AMoPM = cursor.fetchone()  

    if consulta_hora and consulta_fecha:
        hora = consulta_hora[0]
        fecha = consulta_fecha[0]
        horas, minutos = hora.split(':')
        AMoPM = consulta_AMoPM[0]
        return fecha, horas, minutos, AMoPM

    else:
        print("Video no encontrado o falta información.")
        return