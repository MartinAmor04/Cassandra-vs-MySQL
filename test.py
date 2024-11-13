from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import time

# Parámetros de configuración
host = "127.0.0.1"
port = 9042
keyspace = "test_db"

# Autenticación (si se requiere)
auth_provider = PlainTextAuthProvider(username='cassandra_user', password='cassandra_password')

# Conexión a Cassandra
try:
    cluster = Cluster([host], port=port, auth_provider=auth_provider)
    session = cluster.connect(keyspace)
    print("Conexión exitosa a Cassandra.")
except Exception as e:
    print("Error al conectar a Cassandra:", e)

# Función para calcular la media de la columna 'numero' y contar el número de filas
query = "SELECT numero FROM usuarios"
start_time = time.time()  # Medir el tiempo de inicio

try:
    rows = session.execute(query)
    total = 0
    count = 0
    
    # Contamos las filas y sumamos los valores de 'numero'
    for row in rows:
        total += row.numero
        count += 1
    
    # Calcular la media
    if count > 0:
        avg_value = total / count
    else:
        avg_value = None  # No hay datos
    
    # Medir el tiempo de finalización
    end_time = time.time()
    elapsed_time = end_time - start_time  # Calcular el tiempo de ejecución

    # Mostrar el resultado
    print(f"Número total de filas: {count}")
    
    if avg_value is not None:
        print(f"Resultado de la media: {avg_value}")
    else:
        print("No hay datos para calcular la media.")
    
    print(f"Tiempo de ejecución de la consulta: {elapsed_time:.4f} segundos")

except Exception as e:
    print(f"Error al calcular la media o contar las filas: {e}")

# Cerrar la conexión
cluster.shutdown()
print("Conexión cerrada.")
