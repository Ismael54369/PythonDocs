contactos = {
    "Ana López": "644-238-901",
    "Carlos Méndez": "622-451-879",
    "Lucía Fernández": "655-732-110",
    "Javier Torres": "678-990-542",
    "María Gómez": "611-823-754",
    "Pedro Ruiz": "699-203-478",
    "Sofía Navarro": "621-334-512",
    "Diego Vargas": "688-442-903",
    "Laura Ortega": "670-590-214",
    "David Romero": "633-782-601",
    "Elena Castillo": "647-231-489",
    "Raúl Pérez": "624-850-372",
    "Patricia Morales": "652-415-907",
    "Andrés Gil": "698-124-330",
    "Carmen Díaz": "690-843-556",
    "Rubén Herrera": "654-319-782",
    "Isabel Santos": "661-578-209",
    "Sergio Blanco": "676-442-198",
    "Marta Campos": "609-713-825",
    "Pablo Núñez": "645-298-134"
    }

def mostrarListado():
    print("-----------------")

    print("Listado de contactos:")
    for nombre in contactos:
        print(nombre + ": " + contactos[nombre])
    
    print("-----------------")

def mostrarOrdenado():
    print("-----------------")

    print("Listado de contactos ordenado:")
    for nombre in sorted(contactos):
        print(nombre + ": " + contactos[nombre])
    
    print("-----------------")

def anadirContacto():
    print("-----------------")

    nombre = input("Introduce el nombre del contacto a añadir: ")
    numero = input("Introduce el numero del contacto a añadir: ")
    
    if nombre in contactos:
        confirmacion = input("El contacto ya existe ¿quiere modificarlo?(y/n): ")
        confirmacion.lower
        if confirmacion == "y":
            contactos[nombre] = numero
            print("Contacto modificado con exito.")
        else:
            print("El contacto no se actualizará.")
    else:
        contactos[nombre] = numero
        print("Contacto añadido.")
    
    print("-----------------")

def modificarContacto():
    print("-----------------")

    nombre = input("Introduce el nombre del contacto a cambiar: ")
    

    if nombre in contactos:
        numero = input("Introduce el nuevo numero del contacto: ")
        contactos[nombre] = numero
        print("Contacto modificado.")
    else:
        confirmacion = input("El contacto no existe ¿quiere crearlo?(y/n): ")
        confirmacion.lower
        if confirmacion == "y":
            numero = input("Introduce el nuevo numero del contacto: ")
            contactos[nombre] = numero
        else:
            print("El contacto no se creará.")
    
    print("-----------------") 

def consultarContacto():
    print("-----------------")

    nombre = input("Introduce el nombre del contacto a consultar: ")
    
    if nombre in contactos:
        print(contactos[nombre])
    else:
        print("El contacto no existe.")

    print("-----------------")

def borrarContacto():
    print("-----------------")

    nombre = input("Introduce el nombre del contacto a consultar: ")
    
    if nombre in contactos:
        del contactos[nombre]
        print("Contacto borrado con éxito.")
    else:
        print("El contacto no existe.")

    print("-----------------")

def eliminarContactos():
    print("-----------------")

    confirmacion = input("¿Desea eliminar todos los contactos?(y/n): ")
    confirmacion.lower
    if confirmacion == "y":
        contactos.clear()
        print("Contactos eliminados.")
    else:
        print("No se han eliminado los contactos.")
    
    print("-----------------")

while True:
    opcion = input("MENU DE OPCIONES"
    "\na. Listado de teléfonos, usando orden por defecto" 
    "\nb. Listado de teléfonos, por orden alfabético" 
    "\nc. Añadir un nuevo contacto" 
    "\nd. Modificar el teléfono de un contacto"
    "\ne. Buscar un número de teléfono"
    "\nf. Eliminar un contacto"
    "\ng. Borrar el listado de contactos"
    "\nh. Salir"
    "\n")
    match(opcion.lower()):
        case "a":
            mostrarListado()
        case "b":
            mostrarOrdenado()
        case "c":
            anadirContacto()
        case "d":
            modificarContacto()
        case "e":
            consultarContacto()
        case "f":
            borrarContacto()
        case "g":
            eliminarContactos()
        case "h":
            print("Saliendo del programa...")
            exit()
        case _:
            print("Valor desconocido")