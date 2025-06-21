# Inventario de Productos

Proyecto en Python para gestionar un sistema de inventario de productos mediante una base de datos SQLite y una interfaz de terminal.

---

## 📋 Descripción

Este proyecto permite:

* Registrar nuevos productos (nombre, descripción, cantidad, precio y categoría).
* Visualizar la lista de productos registrados.
* Actualizar datos de un producto existente.
* Eliminar productos por su ID.
* Buscar productos por ID.
* Generar un reporte de stock bajo (productos con cantidad igual o menor a un límite especificado).

Toda la lógica está modularizada en funciones y se usa SQLite (`inventario.db`) para el almacenamiento persistente.

---

## ⚙️ Requisitos

* Python 3.7 o superior
* Módulos de la librería estándar (`sqlite3`)

*(El uso de `colorama` es opcional; en la versión sin colores no se requiere instalación extra.)*

---

## 🚀 Instalación y uso

1. **Clonar o descargar** el repositorio:

   ```bash
   git clone https://github.com/laulila/inventario-productos.git
   cd inventario-productos
   ```

2. **(Opcional)** Crear y activar un entorno virtual:

   ```bash
   python3 -m venv venv_inventario
   source venv_inventario/bin/activate   # macOS / Linux
   venv_inventario\Scripts\activate      # Windows
   ```

3. **(Opcional)** Instalar `colorama` para la versión con colores:

   ```bash
   pip install colorama
   ```

4. **Ejecutar** el script principal:

   ```bash
   python talento_entregafinal.py
   ```

5. Seguir el menú en pantalla para elegir la operación deseada.

---

## 📑 Menú de opciones

```
--- MENÚ PRINCIPAL ---
1. Registrar nuevo producto
2. Ver productos
3. Actualizar producto
4. Eliminar producto
5. Buscar producto por ID
6. Reporte de productos con bajo stock
7. Salir
```

Cada opción te pedirá la información necesaria (por ejemplo, ID, nuevos datos, o límite de stock para el reporte).

---

## 📝 Estructura del proyecto

```
inventario-productos/
├── talento_entregafinal.py   # Script principal
├── .gitignore               # Archivos ignorados por Git
└── README.md                # Documentación del proyecto
```

---

## 🤝 Contribuciones

Si te gustaría colaborar o sugerir mejoras, por favor abre un *issue* o envía un *pull request*.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
