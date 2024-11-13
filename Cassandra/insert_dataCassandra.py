from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import csv

# Configura la conexión a Cassandra (ajusta estos valores según tu entorno)
cluster = Cluster(['127.0.0.1'])  # IP del nodo de Cassandra
session = cluster.connect()  # Conéctate sin especificar una base de datos inicial

# Crear la base de datos y la tabla (si no existen)
def crear_tabla():
    # Crear la keyspace 'test_db' si no existe
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS test_db WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
    """)
    
    # Usar la keyspace 'test_db'
    session.set_keyspace('test_db')
    
    # Crear la tabla 'usuarios' si no existe
    session.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT PRIMARY KEY,
        nombre TEXT,
        numero INT
    );
    """)

# Función para cargar datos del archivo CSV a Cassandra
def cargar_datos_csv(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)  # Omite el encabezado del CSV si lo tiene
        
        for row in csv_reader:
            # Asume que el CSV tiene el formato: id, nombre, número
            id = int(row[0])
            nombre = row[1]
            
            # Asegúrate de que 'numero' es un número entero
            try:
                numero = int(row[2])
            except ValueError:
                # Si no se puede convertir a int, manejar el error (por ejemplo, asignar un valor por defecto)
                print(f"Valor inválido para 'numero': {row[2]} (se omitirá esta fila)")
                continue  # Omite la fila si el valor es inválido

            # Inserta los datos en la tabla de Cassandra
            query = "INSERT INTO usuarios (id, nombre, numero) VALUES (%s, %s, %s)"
            session.execute(query, (id, nombre, numero))
            print(f"Insertado: {id}")


# Llamada a la función de creación de tabla
crear_tabla()

# Llamada a la función de carga de CSV
csv_file = 'dataset.csv'  # Cambia esto al nombre de tu archivo CSV
cargar_datos_csv(csv_file)

# Cierra la conexión
cluster.shutdown()

