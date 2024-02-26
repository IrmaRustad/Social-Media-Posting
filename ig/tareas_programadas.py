from imports import conectar_bd, cerrar_bd, obtener_metadata_video, autoPostMeta, TiktokPost, LinkedinPost, XPost, YoutubePost, LinkedinPostTannami, LinkedinPostNettskred  
from imports import logging, autoPostMeta
from datetime import datetime

logging.basicConfig(filename='social_media_posting.log', 
                        filemode='a', 
                        format='%(asctime)s - %(levelname)s - [%(filename)s] - %(message)s', 
                        datefmt='%Y-%m-%d %H:%M:%S', 
                        level=logging.DEBUG)

def cargar_video(video_id, social_media, cursor):

    metadata_video = obtener_metadata_video(cursor, video_id) 
    description, videoname, videoType,VideoTitle,VideoCover = metadata_video                

    # Verificar y cargar en la red social correspondiente
    if social_media == 'Meta':
        autoPostMeta(video_id)
        logging.info(f'Video {video_id} titulo {videoname} subiendo a Meta')
    elif social_media == 'Youtube':         
        YoutubePost(video_id)
        logging.info(f'Video {video_id} titulo {videoname} subiendo a Youtube')
    elif social_media == 'Tiktok':                          
        TiktokPost(video_id)        
        logging.info(f'Video {video_id} titulo {videoname} subiendo a TikTok')
    elif social_media == 'Linkedin':
        LinkedinPost(video_id)
    elif social_media == 'X':       
        logging.info(f'Video {video_id} titulo {videoname} subiendo a X')
        XPost(video_id)
    elif social_media == 'LinkedinTannami':
        LinkedinPostTannami(video_id)                   
        logging.info(f'Video {video_id} titulo {videoname} subiendo a LinkedinTannami')
    elif social_media == 'LinkedinNettskred':
        LinkedinPostNettskred(video_id)
        logging.info(f'Video {video_id} titulo {videoname} subiendo a LinkedinNettskred')

def parse_fecha(fecha_str):
    for formato in ["%d/%m/%Y", "%m/%d/%Y"]:
        try:
            return datetime.strptime(fecha_str, formato).date()
        except ValueError:
            continue
    raise ValueError(f"La fecha '{fecha_str}' no coincide con los formatos esperados 'dd/mm/yyyy' o 'mm/dd/yyyy'")

# Conectar a la base de datos
conexion, cursor = conectar_bd('C:/Users/irma/OneDrive/Skrivebord/Instagram-Posting/ig/videos.db')   

while True:
    consulta_select = "SELECT id, name, description, social_media, hora, fecha, posted FROM videos WHERE posted='NOT_POSTED';"
    cursor.execute(consulta_select)
    videos_por_programar = cursor.fetchall()

    if not videos_por_programar:
        logging.info('Todos los videos han sido programados. Saliendo del bucle.')
        break

    fecha_actual = datetime.now().date()

    for video in videos_por_programar:
        video_id, name, description, social_media, hora, fecha, posted = video

        try:
            fecha_video = parse_fecha(fecha)
        except ValueError as e:
            logging.error(f"Error al analizar la fecha para el video {video_id}: {e}")
            continue

        if social_media in ['X', 'Youtube']:
            if fecha_actual >= fecha_video:
                cargar_video(video_id, social_media, cursor)
                cursor.execute(f"UPDATE videos SET posted='POSTED' WHERE id={video_id}")
                logging.info(f'Video {video_id} titulo {name} marcado como POSTED')
                conexion.commit()
        else:
            cargar_video(video_id, social_media, cursor)
            cursor.execute(f"UPDATE videos SET posted='POSTED' WHERE id={video_id}")
            logging.info(f'Video {video_id} titulo {name} marcado como POSTED')
            conexion.commit()

cerrar_bd(conexion) 