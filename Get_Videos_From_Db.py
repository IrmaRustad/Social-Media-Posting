import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('C:/Users/irma/Dropbox/db/videos.db')   # Asegúrate de que el archivo 'videos.db' está en el directorio correcto

# Crear un cursor
cur = conn.cursor()

# Ejecutar la consulta SQL para obtener videos no publicados
cur.execute('SELECT * FROM videos WHERE posted = "NOT_POSTED"')

# Procesar cada fila individualmente
for fila in cur:
    # Asumiendo que tu tabla 'videos' incluye columnas como 'id', 'nombre', y 'posted'
    # Ajusta la siguiente línea según la estructura exacta de tu tabla
    id_var, nombre_var, url_var, hashtags_var, social_media_var, posted_var = fila
    print(f"ID: {id_var}, Nombre: {nombre_var}, URL: {url_var}, Hashtags: {hashtags_var}, Social Media: {social_media_var}, Posted: {posted_var}")

# Cerrar la conexión
conn.close()


for video in fila:
    print(id_var[0])

