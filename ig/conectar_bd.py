from imports import sqlite3
from imports import datetime

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
        consulta_select = f"SELECT description, name, type,VideoTitle,VideoCover FROM videos WHERE id={video_id};"
        cursor.execute(consulta_select)
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error al obtener metadata del video: {e}")
        return None
    

def dividir_metadata(metadata):
    if metadata:
        description, videoname,videoType,VideoTitle,VideoCover = metadata
        return description, videoname, videoType, VideoTitle,VideoCover
    else:
        return None, None, None,None,None
    
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
    

def cambiar_mes_a_texto(cursor, video_id):
    cursor.execute(f"SELECT fecha FROM videos WHERE id = {video_id}")
    fila = cursor.fetchone()

    if fila:
        fecha_texto = fila[0]  # Obtener la cadena de texto con la fecha

        try:
            # Convertir la cadena de texto a un objeto datetime
            fecha_objeto = datetime.strptime(fecha_texto, '%Y/%m/%d')

            # Extraer el mes y el día
            mes = fecha_objeto.month
            dia = fecha_objeto.day

            # Convertir el número del mes a su nombre en inglés
            mes_nombre = fecha_objeto.strftime('%B')
            print(mes_nombre)
            return mes_nombre, dia

        except ValueError:
            print("Error: El formato de fecha en la base de datos no es válido.")
            return None

    else:
        print("No se encontró la fecha.")
        return None

