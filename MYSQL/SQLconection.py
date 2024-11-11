import mysql.connector
from mysql.connector import Error

# Parámetros de configuración
host = "127.0.0.1"
port = 3307             
user = "root"           
password = "1234"       
database = "my_database" 

# Intento de conexión
try:
    # Conexión a la base de datos
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Conexión exitosa a la base de datos MySQL")
        # Información del servidor
        db_info = connection.get_server_info()
        print("Versión del servidor MySQL:", db_info)

except Error as e:
    print("Error al conectar a MySQL:", e)

connection.close()
