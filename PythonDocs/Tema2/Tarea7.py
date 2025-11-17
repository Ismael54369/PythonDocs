class Persona:
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    def get_nombre(self):
        return self.__nombre
    
    def get_direccion(self):
        return self.__direccion
    
    def get_telefono(self):
        return self.__telefono

    def __str__(self):
        return f"Nombre: {self.__nombre.upper()} | Direccion: {self.__direccion} | Telefono: {self.__telefono}"

contactos = {
    "Ana Martínez": Persona("Ana Martínez", "Calle Luna 12", "612345678"),
    "Luis Fernández": Persona("Luis Fernández", "Avenida Sol 34", "678901234"),
    "Carmen Ruíz": Persona("Carmen Ruiz", "Calle Mayor 8", "645789012"),
    "Javier López": Persona("Javier López", "Paseo del Río 22", "699112233"),
    "Sonia Pérez": Persona("Sonia Pérez", "Calle Jardín 5", "634556677"),
    "Miguel Torres": Persona("Miguel Torres", "Camino Verde 19", "622334455"),
    "Elena Gómez": Persona("Elena Gómez", "Plaza del Centro 3", "687998877"),
    "Raúl Hernández": Persona("Raúl Hernández", "Calle Olmo 41", "655443322"),
    "Patricia Morales": Persona("Patricia Morales", "Avenida Mar 10", "693221144"),
    "Diego Navarro": Persona("Diego Navarro", "Calle Norte 77", "690887766")
}

def mostrarListado():
    print("-----------------")

    print("Listado de contactos ordenado:")
    for i in sorted(contactos):
        print(contactos[i])
    
    print("-----------------")

def anadirContacto():
    print("-----------------")

    nombre = input("Introduce el nombre del contacto a añadir o modificar: ")
    direccion = input("Introduce la direccion del contacto a añadir o modificar: ")
    numero = input("Introduce el numero del contacto a añadir o modificar: ")
    
    
    if nombre in contactos:
        confirmacion = input("El contacto ya existe ¿quiere modificarlo?(y/n): ")
        confirmacion.lower
        if confirmacion == "y":
            contactos[nombre] = Persona(nombre, direccion, numero)
            print("Contacto modificado con exito.")
        else:
            print("El contacto no se actualizará.")
    else:
        contactos[nombre] = Persona(nombre, direccion, numero)
        print("Contacto añadido.")
    
    print("-----------------")

def consultarNumero():
    print("-----------------")
    numero = input("Introduce el numero de telefono a consultar: ")
    encontrado = False

    for persona in contactos.values():
        if persona.get_telefono() == numero:
            print(persona)
            encontrado = True

    if not encontrado:
        print("No existe ningun contacto con ese numero")

    print("-----------------")     

def borrarContacto():
    print("-----------------")

    nombre = input("Introduce el nombre del contacto a borrar: ")
    
    if nombre in contactos:
        del contactos[nombre]
        print("Contacto borrado con éxito.")
    else:
        print("El contacto no existe.")

    print("-----------------")

while True:
    opcion = input("MENU DE OPCIONES"
    "\na. Listado de contactos por orden alfabético." 
    "\nb. Añadir un nuevo contacto." 
    "\nc. Modificar un contacto." 
    "\nd. Buscar un número de teléfono."
    "\ne. Eliminar un contacto."
    "\nf. Salir"
    "\n")
    match(opcion.lower()):
        case "a":
            mostrarListado()
        case "b":
            anadirContacto()
        case "c":
            anadirContacto()
        case "d":
            consultarNumero()
        case "e":
            borrarContacto()
        case "f":
            print("Saliendo del programa...")
            exit()
        case _:
            print("Valor desconocido")