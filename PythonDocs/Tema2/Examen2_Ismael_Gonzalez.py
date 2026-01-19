class Material:
    # Clase base para todos los materiales de la biblioteca.
    # Contiene los atributos comunes que cualquier material debe tener.
    def __init__(self, id_material, titulo, autor, anio_publicacion):
        self.id = id_material
        self.titulo = titulo
        self.autor = autor
        if (anio_publicacion >= 0 and anio_publicacion <= 2025):
            self.anio_publicacion = anio_publicacion
        else: 
            raise ValueError("El año de publicación no puede ser negativo o mayor que el año actual (2025).")

    def mostrar(self):
        # Muestra la información básica del material.
        return f"ID: {self.id} | Título: {self.titulo} | Autor: {self.autor} | Año: {self.anio_publicacion}"

class Libro(Material):
    # Clase para libros, hereda de Material.
    # Añade atributos específicos como género y número de páginas.
    GENEROS_VALIDOS = ["FICCION", "NO FICCION", "TERROR", "CIENCIA"]

    def __init__(self, id_material, titulo, autor, anio_publicacion, genero, num_paginas):
        super().__init__(id_material, titulo, autor, anio_publicacion)
        # Validamos y asignamos el género y el número de páginas
        if genero.upper() in self.GENEROS_VALIDOS:
            self.genero = genero.upper()
        else:
            raise ValueError(f"Género '{genero}' no válido. Opciones: {self.GENEROS_VALIDOS}")

        if num_paginas > 0:
            self.num_paginas = num_paginas
        else:
            raise ValueError("El número de páginas debe ser mayor a 0.")

    def mostrar(self):
        # Polimorfismo: Sobrescribe el método mostrar para añadir detalles del libro.
        return f"LIBRO: {super().mostrar()} | Género: {self.genero} | Páginas: {self.num_paginas}"

class Revista(Material):
    # Clase para revistas, hereda de Material.
    # Añade número de edición y mes de publicación.
    MESES_VALIDOS = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", 
                     "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]

    def __init__(self, id_material, titulo, autor, anio_publicacion, num_edicion, mes_publicacion):
        super().__init__(id_material, titulo, autor, anio_publicacion)
        self.num_edicion = num_edicion
        
        if mes_publicacion.upper() in self.MESES_VALIDOS:
            self.mes_publicacion = mes_publicacion.upper()
        else:
            raise ValueError(f"Mes '{mes_publicacion}' no válido. Opciones: {self.MESES_VALIDOS}")

    def mostrar(self):
        # Polimorfismo: Sobrescribe el método mostrar para añadir detalles de la revista.
        return f"REVISTA: {super().mostrar()} | Edición: {self.num_edicion} | Mes: {self.mes_publicacion}"

materiales = {} # Diccionario para almacenar los materiales por ID
ids_existentes = set() # Usamos un array para almacenar los IDs

def agregar_material():
    # Función para guiar al usuario en la creación de un nuevo libro o revista,
    # validando las entradas y añadiéndolo a la colección.
    print("\n--- Agregar Material ---")
    tipo_material = input("¿Qué desea agregar? (a) Libro / (b) Revista: ").lower()

    while True:
        try:
            id_material = int(input("Introduce el ID del material: "))

            if not id_material:
                id_material = int(input("Introduce el ID del material: "))

            if id_material in ids_existentes:
                print(f"Error: El ID '{id_material}' ya existe. Por favor, introduce uno diferente.")
            else:
                break
        except ValueError:
            print("Error: El ID debe ser un número entero.")
        
    titulo = input("Título: ")
    autor = input("Autor: ")
    
    while True:
        try:
            anio_publicacion = int(input("Año de publicación: "))
            break
        except ValueError:
            print("Error: El año debe ser un número entero.")

    try:
        if tipo_material == 'a':
            print(f"Géneros disponibles: {Libro.GENEROS_VALIDOS}")
            genero = input("Género: ").upper()
            num_paginas = int(input("Número de páginas: "))
            nuevo_material = Libro(id_material, titulo, autor, anio_publicacion, genero, num_paginas)
        
        elif tipo_material == 'b':
            num_edicion = input("Número de edición: ")
            print(f"Meses disponibles: {Revista.MESES_VALIDOS}")
            mes = input("Mes de publicación: ").upper()
            nuevo_material = Revista(id_material, titulo, autor, anio_publicacion, num_edicion, mes)
        
        else:
            print("Opción no válida. No se agregó ningún material.")
            return

        # Si todo fue bien, lo añadimos
        materiales[id_material] = nuevo_material
        ids_existentes.add(id_material)
        print(f"Material '{titulo}' (ID: {id_material}) agregado con éxito.")

    except (ValueError, TypeError) as e:
        # Capturamos errores de validación de las clases (ej. género incorrecto)
        print(f"Error al crear el material: {e}")

def listar_materiales():
    # Muestra todos los materiales registrados en la biblioteca.
    print("\n--- Listado de Materiales ---")
    if not materiales:
        print("No hay materiales registrados.")
        return
    
    for material in materiales.values():
        print(material.mostrar())
        print("-----------------------------")  # Separador

def buscar_material_por_id():
    # Busca y muestra un material específico a partir de su ID.
    print("\n--- Buscar Material por ID ---")
    try:
        id_buscado = int(input("Introduce el ID del material a buscar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
    
    material = materiales.get(id_buscado)
    if material:
        print(material.mostrar())
    else:
        print(f"No se encontró ningún material con el ID '{id_buscado}'.")

def eliminar_material():
    # Elimina un material de la colección a partir de su ID.
    print("\n--- Eliminar Material ---")
    try:
        id_a_eliminar = int(input("Introduce el ID del material a eliminar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
    
    if id_a_eliminar in materiales:
        titulo_eliminado = materiales[id_a_eliminar].titulo
        del materiales[id_a_eliminar]
        ids_existentes.remove(id_a_eliminar)
        print(f"Material '{titulo_eliminado}' (ID: {id_a_eliminar}) ha sido eliminado.")
    else:
        print(f"No se encontró ningún material con el ID '{id_a_eliminar}'.")

def generar_estadisticas():
    # Calcula y muestra estadísticas sobre la colección: total de materiales,
    # desglose por tipo y promedio de páginas de los libros.
    print("\n--- Estadísticas de la Biblioteca ---")
    
    total_materiales = len(materiales)
    if total_materiales == 0:
        print("No hay materiales para generar estadísticas.")
        return

    num_libros = 0
    num_revistas = 0
    total_paginas_libros = 0

    for material in materiales.values():
        if isinstance(material, Libro):
            num_libros += 1
            total_paginas_libros += material.num_paginas
        elif isinstance(material, Revista):
            num_revistas += 1

    # Calculamos el promedio de páginas solo si hay libros para evitar división por cero
    if num_libros > 0:
        promedio_paginas = total_paginas_libros / num_libros
    else:
        promedio_paginas = 0

    print(f"Total de materiales registrados: {total_materiales}")
    print(f"Número de libros: {num_libros}")
    print(f"Número de revistas: {num_revistas}")
    if num_libros > 0:
        print(f"Promedio de páginas por libro: {promedio_paginas:.2f}")

def mostrar_menu():
    # Imprime el menú de opciones para el usuario.
    print("\n===== MENÚ DE LA BIBLIOTECA =====")
    print("a) Agregar Material.")
    print("b) Listar Materiales.")
    print("c) Buscar Material por ID.")
    print("d) Eliminar Material.")
    print("e) Generar Estadísticas.")
    print("f) Salir.")
    print("=================================")

def main():
    # Función principal que ejecuta el bucle del programa.
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").lower()

        if opcion == 'a':
            agregar_material()
        elif opcion == 'b':
            listar_materiales()
        elif opcion == 'c':
            buscar_material_por_id()
        elif opcion == 'd':
            eliminar_material()
        elif opcion == 'e':
            generar_estadisticas()
        elif opcion == 'f':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una de las opciones del menú.")

if __name__ == "__main__":
    main()