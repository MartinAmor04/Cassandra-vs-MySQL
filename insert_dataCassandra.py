from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import random
import string

# Conectar al clúster de Cassandra
cluster = Cluster(['127.0.0.1'])  # Cambia esto si tu Cassandra está en otro host
session = cluster.connect()

# Seleccionar el keyspace donde vamos a trabajar
session.set_keyspace('datos')

# Función para generar un nombre aleatorio
def random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Eliminar la tabla id_counter si ya existe (para recrearla correctamente)
session.execute("""
    DROP TABLE IF EXISTS id_counter
""")

# Crear la tabla id_counter con la columna counter_value definida como COUNTER
session.execute("""
    CREATE TABLE IF NOT EXISTS id_counter (
        table_name TEXT PRIMARY KEY,
        counter_value COUNTER
    )
""")

# Inicializar el contador (solo si no existe)
def initialize_counter():
    # Verificar si ya existe una fila en la tabla id_counter para 'sample_data'
    result = session.execute("""
        SELECT counter_value FROM id_counter WHERE table_name = 'sample_data'
    """)
    
    # Si no existe, establecer el contador en 0
    if not result.one():
        # Usamos UPDATE en lugar de INSERT para la columna COUNTER
        session.execute("""
            UPDATE id_counter
            SET counter_value = counter_value + 0  -- Esto inicializa el contador a 0
            WHERE table_name = 'sample_data'
        """)

# Llamar a la función para inicializar el contador
initialize_counter()

# Función para obtener el siguiente id autoincremental
def get_next_id():
    # Incrementar el contador
    session.execute("""
        UPDATE id_counter
        SET counter_value = counter_value + 1
        WHERE table_name = 'sample_data'
    """)

    # Recuperar el valor actual del contador
    result = session.execute("""
        SELECT counter_value FROM id_counter WHERE table_name = 'sample_data'
    """)
    next_id = result.one()[0]  # Obtener el valor del contador
    return next_id

# Crear la tabla (si no existe) para los datos
session.execute("""
    CREATE TABLE IF NOT EXISTS sample_data (
        id INT PRIMARY KEY,
        name TEXT,
        value INT
    )
""")

# Insertar 1000 registros
for i in range(1000):
    # Generar un nombre y un valor
    name = f'nombre {i}'
    value = int(i * 0.5)
    id = get_next_id()

    # Insertar los datos en la tabla
    insert_statement = SimpleStatement("""
        INSERT INTO sample_data (id, name, value) 
        VALUES (%s, %s, %s)
    """)
    session.execute(insert_statement, (id, name, value))

print("Se han insertado 1000 datos correctamente.")

# Cerrar la conexión
session.shutdown()
cluster.shutdown()


