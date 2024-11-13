import mysql.connector
import csv

# Configurar la conexión a MySQL
conn = mysql.connector.connect(
    host='localhost',
    port='3307',
    user='root',
    password='1234',
    database='my_database'
)
cursor = conn.cursor()

# Leer el archivo CSV y realizar inserciones en la base de datos
csv_file = 'dataset.csv'
with open(csv_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute('''
        INSERT INTO dataset (id, nombre, numero)
        VALUES (%s, %s, %s);
        ''', (row['id'], row['nombre'], row['número']))

# Confirmar los cambios y cerrar la conexión
conn.commit()
cursor.close()
conn.close()

print(f"Datos insertados en la base de datos MySQL con éxito.")


