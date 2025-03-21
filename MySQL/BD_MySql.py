import mysql.connector

# Conexion a la base de datos MySQL sin especificar base de datos
def conectar_mysql(host, user, password,database):
    try:
        conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Conexión a MySQL exitosa.")
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None
    
# Crear cursor para ejecutar consultas
def crear_cursor(conexion):
    try:
        cursor = conexion.cursor()
        print("Cursor creado.")
        return cursor
    except mysql.connector.Error as e:
        print(f"Error al crear el cursor: {e}")
        return None

# Crear base de datos
def crear_base_datos(cursor, nombre_bd):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nombre_bd}")
        print(f"Base de datos '{nombre_bd}' creada")
    except mysql.connector.Error as e:
        print(f"Error al crear la base de datos: {e}")


# Crear tabla de ejemplo
def crear_tabla(cursor):
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                edad INT NOT NULL,
                profesion TEXT NOT NULL,
                dni VARCHAR(9) NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP  
            )
        ''')
        print("Tabla creada o ya existe.")
    except mysql.connector.Error as e:
        print(f"Error al crear la tabla: {e}")

# Insertar datos en la tabla
def insertar_datos(cursor, nombre, edad, profesion, dni):
    try:
        cursor.execute('''
            INSERT INTO usuarios (nombre, edad, profesion, dni)
            VALUES (%s, %s, %s, %s)
        ''', (nombre, edad, profesion, dni))
        print("Datos insertados.")
    except mysql.connector.Error as e:
        print(f"Error al insertar datos: {e}")

# Insertar varios datos en la tabla
def insertar_varios_datos(cursor, datos):
    try:
        cursor.executemany('''
            INSERT INTO usuarios (nombre, edad, profesion, dni)
            VALUES (%s, %s, %s, %s)
        ''', datos)
        print("Varios datos insertados.")
    except mysql.connector.Error as e:
        print(f"Error al insertar varios datos: {e}")