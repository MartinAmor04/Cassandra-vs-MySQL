from cassandra.cluster import Cluster

# Conectar al clúster de Cassandra
cluster = Cluster(['127.0.0.1'])  # Cambia esto si tu Cassandra está en otro host
session = cluster.connect()

# Seleccionar el keyspace donde vamos a trabajar
session.set_keyspace('datos')  # Cambia 'datos' si tu keyspace tiene otro nombre

# Realizar una consulta SELECT para obtener todos los registros de la tabla 'sample_data'
def query_sample_data():
    # Definir la consulta SELECT
    query = "SELECT *  FROM sample_data LIMIT 10"
    
    try:
        # Ejecutar la consulta
        rows = session.execute(query)

        # Imprimir los resultados
        print("Registros de la tabla 'sample_data':")
        for row in rows:
            print(row)

    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")

# Llamar a la función de consulta
query_sample_data()

# Cerrar la conexión
session.shutdown()
cluster.shutdown()
