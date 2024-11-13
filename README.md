# Comparación de Rendemento entre MySQL e Cassandra

Este proxecto ten como obxectivo comparar o rendemento de diferentes operacións de agregación (como a media) sobre datos almacenados en dous tipos de bases de datos: **MySQL** (relacional) e **Cassandra** (noSQL). A través deste exercicio, mediremos o tempo de execución das consultas para poder comparar os resultados e xustificalos teóricamente.

## Contido do Proxecto

- **Dataset Aleatorio**: Crearemos un conxunto de datos con valores aleatorios que se cargarán en ambas as bases de datos.
- **Bases de Datos**: Utilizaremos **MySQL** como base de datos relacional e **Cassandra** como base de datos noSQL.
- **Docker**: Usaremos Docker para levantar os servidores das bases de datos.

## Pasos do Proxecto

### 1. Levantar os Servidores de Bases de Datos con Docker
Usamos Docker para levantar instancias de MySQL e Cassandra. Isto permite executar ambas as bases de datos de maneira rápida e sen ter que instalalas manualmente no sistema operativo.

```bash
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=root -p 3307:3306 -d mysql:latest
```
```bash
docker run --name cassandra-container -d -p 9042:9042 cassandra:latest
```
#### Docker compose
Ademáis, creamos un arquivos de configuración de docker para poder levantar os contedores de maneira máis sinxela.

### 2. Creación de scripts (.py & .sql)
Crearemos os scripts necesarios para a creación da base de datos e a tabla, inserción de datos e a conexión ao contedor.
#### Environments
Utilizaremos environments coas súas librerías e versión propias polo que tamén crearemos un arquivo .yml onde estarán todo-los parámetros de ese environment.

### 3. Consultas a base de datos
Finalmente, faremos as consultas as dúas bases de datos SQL e Cassandra e mediremos o rendemento de cada unha.
