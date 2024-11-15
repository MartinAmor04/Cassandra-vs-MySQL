import mysql.connector

# Configuración de conexión a MySQL
config = {
    'host': '127.0.0.1',
    'port': 3307,
    'user': 'root',
    'password': '1234',
    'database': 'my_database'
}

# Conectar a la base de datos
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

# Leer y ejecutar el archivo SQL
sql_script = "CREATE TABLE IF NOT EXISTS dataset (id INT PRIMARY KEY,nombre VARCHAR(100),numero INT);"


# Ejecutar el script de creación de tabla
try:
    cursor.execute(sql_script)
    connection.commit()  # Aplicar los cambios
    print("Tabla creada correctamente.")
except mysql.connector.Error as err:
    print(f"Error al crear la tabla: {err}")

# Cerrar la conexión
cursor.close()
connection.close()

