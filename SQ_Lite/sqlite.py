import sqlite3

# Crear conexion a la base de datos SQLite
def crear_conexion():
    try:
        conexion = sqlite3.connect(r'SQ_Lite\pruebas.db')
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

# Crear cursor para ejecutar comandos SQL
def crear_cursor(conexion):
    return conexion.cursor() if conexion else None

# Crear tabla de ejemplo
def create_table(cursor, conexion): 
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR NOT NULL CHECK (LENGTH(nombre) <= 50),
                edad INTEGER NOT NULL,
                profesion TEXT NOT NULL,
                dni VARCHAR NOT NULL CHECK (LENGTH(dni) = 9) UNIQUE,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP  
            )
        ''')
        conexion.commit()  # Commit de la conexión
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")


# Insertar datos en la tabla de ejemplo con control de dni
def insertar_una_persona(cursor, conexion, nombre, edad, profesion, dni):
    try:
        cursor.execute('''SELECT COUNT(*) FROM usuarios WHERE dni = ?''', (dni,))
        if cursor.fetchone()[0] > 0:
            print("El DNI ya está registrado. No se puede insertar el dato.")
            return
        
        cursor.execute('''
            INSERT INTO usuarios (nombre, edad, profesion, dni)
            VALUES (?, ?, ?, ?)
        ''', (nombre, edad, profesion, dni))
        conexion.commit()
        print("Dato insertado correctamente.")
    except sqlite3.Error as e:
        print(f"Error al insertar el dato: {e}")

# Insertar varios datos en la tabla de ejemplo
def insertar_varios_datos(cursor, conexion, datos):
    try:
        cursor.executemany('''
            INSERT INTO usuarios (nombre, edad, profesion, dni)
            VALUES (?, ?, ?, ?)
        ''', datos)
        conexion.commit()
        print(f"{len(datos)} datos insertados correctamente.")
    except sqlite3.Error as e:
        print(f"Error al insertar múltiples datos: {e}")

# Obtener todos los datos de la tabla de ejemplo
def obtener_datos(cursor):
    try:
        cursor.execute('SELECT * FROM usuarios')
        productos = cursor.fetchall()
        for producto in productos:
            print(producto)
    except sqlite3.Error as e:
        print(f"Error al obtener los datos: {e}")

# Modificar datos de la tabla de ejemplo
def modificar_datos(cursor, conexion, usuario_id, nombre, edad, profesion, dni):
    try:
        cursor.execute('''
            UPDATE usuarios
            SET nombre = ?, edad = ?, profesion = ?, dni = ?
            WHERE id = ?
        ''', (nombre, edad, profesion, dni, usuario_id))
        conexion.commit()
        print("Datos modificados correctamente.")
    except sqlite3.Error as e:
        print(f"Error al modificar los datos: {e}")

# Borrar tabla de ejemplo
def borrar_tabla(cursor, conexion):
    try:
        cursor.execute('DROP TABLE IF EXISTS usuarios')
        conexion.commit()
        print("Tabla eliminada correctamente.")
    except sqlite3.Error as e:
        print(f"Error al eliminar la tabla: {e}")

# Cerrar la conexion a la base de datos SQLite
def close_connection(conexion):
    if conexion:
        conexion.close()
        print("Conexión cerrada.")

# Función principal para ejecutar el flujo
def main():
    # Crear conexión y cursor
    conexion = crear_conexion()
    cursor = crear_cursor(conexion)

    # Comprobar si la conexión y el cursor son válidos
    if not conexion or not cursor:
        print("No se pudo establecer la conexión a la base de datos.")
        return

    # Crear tabla (pasando tanto el cursor como la conexión)
    create_table(cursor, conexion)

    # Insertar una persona
    insertar_una_persona(cursor, conexion, 'Juan', 30, 'Ingeniero', '12345678A')

    # Modificar datos de la persona
    modificar_datos(cursor, conexion, 1, 'Juan', 31, 'Carnicero', '12345678A')

    # Insertar varios datos
    insertar_varios_datos(cursor, conexion, [
        ('Maria', 25, 'Abogada', '87654321B'),
        ('Pedro', 40, 'Arquitecto', '23456789C'),
        ('Ana', 28, 'Doctora', '34567890D')
    ])

    # Obtener y mostrar los datos
    obtener_datos(cursor)

    # Cerrar conexión
    close_connection(conexion)

# Ejecutar el flujo
if __name__ == "__main__":
    main()
