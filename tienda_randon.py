# Lista para almacenar los productos
# guardara todos los datos de los estudiantes 
productos = []

# Función para agregar productos
# la funcion agregar productos permite permite añadir nuevos productos al inventario
# con su nombre, cantidad y precio sugerido

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")#el imput recibira el nombre, cantidad y precio sugerido
    cantidad = int(input("Ingrese la cantidad del producto: ")) #int por que la cantidad es un valor de 
    #caracter entero
    precio_sugerido = float(input("Ingrese el precio sugerido del producto: "))# float por que el precio es un
    # valor que puede ser casi siempre de tipo decimal
    producto = {
        'nombre': nombre,
        'cantidad': cantidad,
        'precio_sugerido': precio_sugerido
    }
    productos.append(producto)
    print(f"Producto {nombre} agregado con éxito.")

# Función para registrar una venta
# esta funcion permite registrar una venta, calcular el total y el vuelto, y actualizar
# la cantidad de productos en el inventario
def registrar_venta():
    nombre = input("Ingrese el nombre del producto vendido: ")#este imput registrara los detalles de las ventas
    cantidad_vendida = int(input("Ingrese la cantidad vendida: "))# la cantidad sera de tipo entero
    pago = float(input("Ingrese el pago recibido: ")) #el pago sera un valor decimal muchas veces
    #usarems un ciclo for para ejecutar estos bloques de codigo
    for producto in productos:
        if producto['nombre'] == nombre:# los if iran determinando que se ejecuten 
            if producto['cantidad'] >= cantidad_vendida:
                total = cantidad_vendida * producto['precio_sugerido']
                vuelto = pago - total
                producto['cantidad'] -= cantidad_vendida
                print(f"Venta registrada. Total: ${total:.2f}, Vuelto: ${vuelto:.2f}")
                return #devolvera los valores en caso que se cumplan los requerimientos de la venta
            else:
                print("Cantidad insuficiente en inventario.")# devolvera esto en caso de que no sea suficiente 
                # la cantidad vendida
                return
    print("Producto no encontrado.")
    #este print imprimira los detalles en caso de que se cumpla esta condicio

# Función para mostrar el inventario
# esta funcion muestra todos los productos disponibles en la tienda con sus detalles 
def mostrar_inventario():
    print("Inventario de productos:")
    for producto in productos:# un for para ejecutar los bloques de codigo que mostraran los detalles del registro
        #del producto 
        print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio sugerido: ${producto['precio_sugerido']:.2f}")

# Menú principal
# este menu se encarga de ayudar al usuario a seleccionar si agregar un nuevo producto, registrar ventas
# mostrar el inventario o sair del programa 
def menu():
    while True:# el while mantendra en ejecucion el menu hasta que el usuario decida finalizar la ejecucion 
        print("\n1. Agregar producto")
        print("\n2. Registrar venta")
        print("\n3. Mostrar inventario")
        print("\n4. Salir")#detendra la ejecucion del programa 
        opcion = input("Seleccione una opción: ")
        #usaremos estas condiciones para declarar la accion a iniciar para e usuario 
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            registrar_venta()
        elif opcion == '3':
            mostrar_inventario()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
# ejecutara el menu al inicializar el programa 
menu()
