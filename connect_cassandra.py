from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra import OperationTimedOut

# Configura la dirección del clúster de Cassandra
cluster = Cluster(['127.0.0.1'])  # Asegúrate de que Cassandra esté corriendo en este host

# Intenta conectarte al clúster
try:
    session = cluster.connect()
    print("Conexión exitosa a Cassandra")

    # Realiza una consulta simple para verificar la conexión
    session.set_keyspace('system')  # 'system' es un keyspace predeterminado en Cassandra
    result = session.execute('SELECT release_version FROM system.local')  # Consulta para obtener la versión del clúster

    # Imprime los resultados
    for row in result:
        print(f"Cassandra version: {row.release_version}")

except OperationTimedOut:
    print("Error: No se pudo conectar a Cassandra. El tiempo de conexión ha expirado.")
except Exception as e:
    print(f"Error al conectar a Cassandra: {e}")
finally:
    # Cierra la sesión y el cluster si está conectado
    if 'session' in locals():
        session.shutdown()
    cluster.shutdown()
