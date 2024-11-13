from cassandra.cluster import Cluster

# Configura la conexión al clúster de Cassandra
cluster = Cluster(['127.0.0.1'])  # Cambia esto si tu Cassandra está en otro host
session = cluster.connect()

# Crear un Keyspace (si no existe)
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS datos WITH REPLICATION = {
        'class': 'SimpleStrategy',
        'replication_factor': 1
    }
""")

# Usar el Keyspace recién creado
session.set_keyspace('datos')

# Crear una tabla (si no existe)
session.execute("""
    CREATE TABLE IF NOT EXISTS sample_data (
        id int PRIMARY KEY,
        name text,
        value int
    )
""")

print("Keyspace y tabla creados con éxito.")