import mysql.connector
from mysql.connector import Error
import time

# Parámetros de configuración
host = "127.0.0.1"      
port = 3307             
user = "root"           
password = "1234"       
database = "my_database" 

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

        # Crear un cursor para ejecutar la consulta
        cursor = connection.cursor()

        # Consulta que calcula la media de una columna
        query = "SELECT AVG(numero) FROM dataset"

        # Medir el tiempo de inicio
        start_time = time.time()
        
        # Ejecutar la consulta
        cursor.execute(query)
        
	# Medir el tiempo de finalización
        end_time = time.time()

        # Obtener el resultado
        result = cursor.fetchone()[0]

        # Calcular el tiempo de ejecución
        elapsed_time = end_time - start_time

        # Mostrar el resultado y el tiempo de ejecución
        print(f"Resultado de la media: {result}")
        print(f"Tiempo de ejecución de la consulta: {elapsed_time:.4f} segundos")

except Error as e:
    print("Error al conectar a MySQL:", e)

cursor.close()
connection.close()
