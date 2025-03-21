import BD_MySql

# Conectar a la base de datos MySQL
conexion = BD_MySql.conectar_mysql(
    host='localhost',
    user='root',
    password="",
    database='prueba'
)
# Crear cursor para ejecutar consultas
cursor = BD_MySql.crear_cursor(conexion)

# Crear la base de datos
BD_MySql.crear_base_datos(cursor, 'prueba')

# Crear la tabla de ejemplo
BD_MySql.crear_tabla(cursor)

# Insertar datos en la tabla
BD_MySql.insertar_datos(cursor, 'Juan', 30, 'Ingeniero', '12345678A')

BD_MySql.insertar_varios_datos(cursor, [
    ('Pedro', 25, 'Médico', '87654321B'),
    ('Ana', 28, 'Abogada', '23456789C'),
    ('Luis', 35, 'Arquitecto', '34567890D')
])

# Confirmar los cambios en la base de datos
conexion.commit()

# Consultar los datos de un usuario
cursor.execute("SELECT * FROM usuarios WHERE nombre = 'Pedro'")

# Obtener todos los resultados
ana = cursor.fetchall()

# Imprimir los resultados
print(ana)


