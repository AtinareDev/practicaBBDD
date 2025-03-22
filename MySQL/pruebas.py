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

cursor.execute("SELECT * FROM usuarios")

# Usando fetchall()
todos_los_resultados = cursor.fetchall()
print("Todos los resultados:", todos_los_resultados)

cursor.execute("SELECT * FROM usuarios where edad > 30")
# Usando fetchall()
# Consumo de los datos de la consulta anterior al asignar a la variable
todos_los_resultados = cursor.fetchall()
print("Todos los resultados de + de 30:", todos_los_resultados)

# Como el cursor al hacer fetchall ha llegado al final de los resultados, 
# no se puede volver a usar fetchall() para obtener los mismos resultados.
# Por lo tanto, se vuelve a ejecutar la consulta para obtener los resultados 
# nuevamente. Es importante recordar que hay que consumir los resultados del cursor
# antes de volver a ejecutar la consulta o dara error Unread result found.
cursor.execute("SELECT * FROM usuarios where edad > 30")

# Usando fetchone() para obtener el primer resultado
primer_resultado = cursor.fetchone()
print("Primer resultado:", primer_resultado)

# Usando fetchmany() para obtener las primeras 2 filas
primeras_dos_filas = cursor.fetchmany(2)
print("Primeras dos filas:", primeras_dos_filas)


