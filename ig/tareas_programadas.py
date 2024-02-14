from conectar_bd import conectar_bd, cerrar_bd, obtener_metadata_video
from metaautoPost import autoPostMeta 
import logging



logging.basicConfig(filename='social_media_posting.log', 
                        filemode='a', 
                        format='%(asctime)s - %(levelname)s - [%(filename)s] - %(message)s', 
                        datefmt='%Y-%m-%d %H:%M:%S', 
                        level=logging.DEBUG)

def cargar_video(video_id, social_media, cursor):
    import sys
    sys.path.append('C:/Users/irma/OneDrive/Skrivebord/Social-Media-Posting-main 13022024/Social-Media-Posting-main/Apps')
    from tiktok import TiktokPost
    from linkedin import LinkedinPost
    from x import subir_video_x
    from youtube import YoutubePost



    # Obtener metadata del video
    metadata_video = obtener_metadata_video(cursor, video_id)

    description, videoname, videoType = metadata_video

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
    elif social_media == 'linkedin':
        LinkedinPost(video_id)
        logging.info(f'Video {video_id} titulo {videoname} subiendo a LinkedIn')
    elif social_media == 'X':
        logging.info(f'Video {video_id} titulo {videoname} subiendo a X')
        subir_video_x(video_id)

# Conectar a la base de datos
conexion, cursor = conectar_bd('C:/Users/irma/OneDrive/Skrivebord/Social-Media-Posting-main 13022024/Social-Media-Posting-main/ig/videos.db')   



# Continuar ejecutando hasta que todos los videos estén marcados como 'POSTED'
while True:
    # Consulta SELECT para obtener videos con estado 'NOT_POSTED'
    consulta_select = "SELECT id, name, description, social_media,hora,fecha, posted FROM videos WHERE posted='NOT_POSTED';"
    cursor.execute(consulta_select)

    # Obtener los resultados
    videos_por_programar = cursor.fetchall()

    # Salir del bucle si no hay más videos por programar
    if not videos_por_programar:
        logging.info('Todos los videos han sido programados. Saliendo del bucle.')
        break
        

    # Procesar cada video y marcar como 'POSTED'
    for video in videos_por_programar:
        video_id, name, description, social_media, hora, fecha, posted = video


        # Cargar el video en la red social correspondiente
        cargar_video(video_id, social_media, cursor)

        # Marcar el video como 'POSTED'
        cursor.execute(f"UPDATE videos SET posted='POSTED' WHERE id={video_id}")
        logging.info(f'Video {video_id} titulo {name} marcado como POSTED')
        conexion.commit()

# Cerrar la conexión
cerrar_bd(conexion)


                                                                