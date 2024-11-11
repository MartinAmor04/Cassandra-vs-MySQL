from cassandra.cluster import Cluster

# Conectar al clúster de Cassandra
cluster = Cluster(['127.0.0.1'])  # Cambia esto si tu Cassandra está en otro host
session = cluster.connect()

# Seleccionar el keyspace donde vamos a trabajar
session.set_keyspace('datos')  # Cambia 'datos' si tu keyspace tiene otro nombre

# Función para contar las filas de la tabla 'sample_data'
def count_rows():
    # Definir la consulta COUNT
    query = "SELECT COUNT(*) FROM sample_data"
    
    try:
        # Ejecutar la consulta
        result = session.execute(query)
        
        # Obtener el número de filas
        row_count = result.one()[0]
        
        # Imprimir el resultado
        print(f"El número de filas en la tabla 'sample_data' es: {row_count}")
        
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")

# Función para obtener registros de la tabla 'sample_data' (limitados a 10)
def query_sample_data():
    # Definir la consulta SELECT
    query = "SELECT * FROM sample_data LIMIT 10"
    
    try:
        # Ejecutar la consulta
        rows = session.execute(query)

        # Imprimir los resultados
        print("Registros de la tabla 'sample_data' (limitados a 10):")
        for row in rows:
            print(row)

    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")

# Llamar a la función de conteo de filas
count_rows()

# Llamar a la función de consulta para obtener algunos registros
query_sample_data()

# Cerrar la conexión
session.shutdown()
cluster.shutdown()
