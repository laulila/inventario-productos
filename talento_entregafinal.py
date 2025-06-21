import sqlite3
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

def conectar_db():
    return sqlite3.connect("inventario.db")

def crear_tabla():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    ''')
    conexion.commit()
    conexion.close()

def registrar_producto():
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    categoria = input("Categoría: ")

    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",
                   (nombre, descripcion, cantidad, precio, categoria))
    conexion.commit()
    conexion.close()
    print(Fore.GREEN + "Producto registrado correctamente.")

def ver_productos():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()

    for prod in productos:
        print(Fore.CYAN + f"ID: {prod[0]}, Nombre: {prod[1]}, Cantidad: {prod[3]}, Precio: ${prod[4]:.2f}, Categoría: {prod[5]}")

def actualizar_producto():
    id = input("Ingrese el ID del producto a actualizar: ")
    nombre = input("Nuevo nombre: ")
    descripcion = input("Nueva descripción: ")
    cantidad = int(input("Nueva cantidad: "))
    precio = float(input("Nuevo precio: "))
    categoria = input("Nueva categoría: ")

    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("UPDATE productos SET nombre=?, descripcion=?, cantidad=?, precio=?, categoria=? WHERE id=?",
                   (nombre, descripcion, cantidad, precio, categoria, id))
    conexion.commit()
    conexion.close()
    print(Fore.YELLOW + "Producto actualizado.")

def eliminar_producto():
    id = input("Ingrese el ID del producto a eliminar: ")
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id=?", (id,))
    conexion.commit()
    conexion.close()
    print(Fore.RED + "Producto eliminado.")

def buscar_producto():
    id = input("Ingrese el ID del producto a buscar: ")
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id=?", (id,))
    prod = cursor.fetchone()
    conexion.close()

    if prod:
        print(Fore.CYAN + f"ID: {prod[0]}, Nombre: {prod[1]}, Descripción: {prod[2]}, Cantidad: {prod[3]}, Precio: ${prod[4]:.2f}, Categoría: {prod[5]}")
    else:
        print(Fore.RED + "Producto no encontrado.")

def reporte_stock_bajo():
    limite = int(input("Mostrar productos con cantidad igual o menor a: "))
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()
    conexion.close()

    print(Fore.MAGENTA + "Productos con bajo stock:")
    for prod in productos:
        print(Fore.MAGENTA + f"ID: {prod[0]}, Nombre: {prod[1]}, Cantidad: {prod[3]}")

def menu():
    crear_tabla()
    while True:
        print(Style.BRIGHT + Fore.BLUE + "\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar nuevo producto")
        print("2. Ver productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto por ID")
        print("6. Reporte de productos con bajo stock")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            ver_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            reporte_stock_bajo()
        elif opcion == "7":
            print(Fore.GREEN + "Saliendo del programa...")
            break
        else:
            print(Fore.RED + "Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
