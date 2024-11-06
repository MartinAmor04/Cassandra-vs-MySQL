import mysql.connector
import random
import string

# Configuración de conexión a MySQL
config = {
    'host': '127.0.0.1',
    'port': 3307,
    'user': 'root',
    'password': '1234',  
    'database': 'my_database'      
}

# Conectar a la base de datos
try:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Inserción de 1000 datos
    for i in range(1000):
        name = f'nombre {i}'
        value = i * 0.5
        sql_insert_query = "INSERT INTO sample_data (name, value) VALUES (%s,%s)"
        cursor.execute(sql_insert_query, (name, value))

    connection.commit()  # Asegúrate de aplicar todas las transacciones
    print("Se han insertado 1000 datos correctamente.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Cerrar la conexión
    if connection.is_connected():
        cursor.close()
        connection.close()

