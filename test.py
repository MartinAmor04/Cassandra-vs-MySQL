from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import time

# Parámetros de configuración
host = "127.0.0.1"
port = 9042
keyspace = "datos"

# Autenticación (si se requiere)
auth_provider = PlainTextAuthProvider(username='cassandra_user', password='cassandra_password')

try:
    # Conexión a la base de datos Cassandra
    cluster = Cluster([host], port=port, auth_provider=auth_provider)
    session = cluster.connect(keyspace)

    # Consulta para obtener todos los valores
    query = "SELECT value FROM sample_data"

    # Medir el tiempo de inicio
    start_time = time.time()

    # Ejecutar la consulta
    rows = session.execute(query)

    # Obtener los valores y calcular la media
    total = 0
    count = 0

    for row in rows:
        total += row.value
        count += 1

    # Calcular la media
    if count > 0:
        avg_value = total / count
    else:
        avg_value = None  # No hay datos

    # Medir el tiempo de finalización
    end_time = time.time()

    # Calcular el tiempo de ejecución
    elapsed_time = end_time - start_time

    # Mostrar el resultado y el tiempo de ejecución
    if avg_value is not None:
        print(f"Resultado de la media: {avg_value}")
    else:
        print("No hay datos para calcular la media.")
    
    print(f"Tiempo de ejecución de la consulta: {elapsed_time:.4f} segundos")

except Exception as e:
    print("Error al conectar a Cassandra:", e)

finally:
    cluster.shutdown()
