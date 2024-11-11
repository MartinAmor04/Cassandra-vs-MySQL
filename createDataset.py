import csv
import random
import faker

# Inicializar la biblioteca Faker para generar datos ficticios
fake = faker.Faker()

# Definir el número de filas a generar
num_filas = 1000000

# Definir los campos del CSV
fieldnames = ['id', 'nombre', 'número']

# Crear el archivo CSV
csv_file = 'dataset.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Escribir la cabecera
    writer.writeheader()
    
    # Generar y escribir cada fila de datos
    for i in range(1, num_filas + 1):
        row = {
            'id': i,
            'nombre': fake.name(),
            'número': random.randint(0, 1000)
        }
        writer.writerow(row)

print(f"Archivo CSV '{csv_file}' creado con éxito con {num_filas} filas.")
