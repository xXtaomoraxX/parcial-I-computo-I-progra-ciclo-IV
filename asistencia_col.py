# Lista para almacenar los estudiantes
# guardara todos los datos de los estudiantes 
estudiantes = []

# Función para agregar estudiantes
# esta funcion permitira añadir uevos estudiantes al sistema del colegio
def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    estudiante = {
        'nombre': nombre,
        'asistencias': []
    }
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} agregado con éxito.")

# Función para registrar asistencia
# esta funcion permite registrar las asistencias, permisos y faltas de los estudiantes,
# incluyendo la razo si la causa aplica justificadamente
def registrar_asistencia():
    nombre = input("Ingrese el nombre del estudiante: ")
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
    estado = input("Ingrese el estado (Asistencia, Permiso, Inasistencia): ")
    razon = ""
    if estado.lower() == "permiso":
        razon = input("Ingrese la razón del permiso: ")
    #usaremos un ciclo for para ejecutar las siguientes acciones en orden 
    for estudiante in estudiantes:
        if estudiante['nombre'] == nombre: #el if determinara que se deba ejecutar
            asistencia = {
                'fecha': fecha,
                'estado': estado,
                'razon': razon
            }
            estudiante['asistencias'].append(asistencia)
            print(f"Asistencia registrada para {nombre}.")
            return
    print("Estudiante no encontrado.")

# Función para mostrar registros de asistencia
# esta opcion mostrara todos los registros de asistencia de los estudiantes
def mostrar_registros():
    # aqui usaremos dos ciclos para ejecutar los siguientes bloques de codigo 
    for estudiante in estudiantes:
        print(f"\nEstudiante: {estudiante['nombre']}")
        for asistencia in estudiante['asistencias']:
            print(f"Fecha: {asistencia['fecha']}, Estado: {asistencia['estado']}, Razón: {asistencia['razon']}")

# Menú principal
# un meenu que muestra todas las opciones dispobibles para la lista de asistencias
def menu():
    while True: #utilizaremos el ciclo while para que el menu se mantenga ejecutado hasta que,
        # el usuario decida cerrar el programa 
        print("\n1. Agregar estudiante")
        print("\n2. Registrar asistencia")
        print("\n3. Mostrar registros de asistencia")
        print("\n4. Salir")
        opcion = input("Seleccione una opción: ")
        # aqui pondremos las condicionantes para que el usuario decida elegir una accion a ejecutar
        if opcion == '1':
            agregar_estudiante()
        elif opcion == '2':
            registrar_asistencia()
        elif opcion == '3':
            mostrar_registros()
        elif opcion == '4': # esta opcion detendra al ejecucion del menu 
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
# inicializamos el menu 
menu()
