def ejercicio1():
    print("EJERCICIO 1")
    print("---------------------")

    #Declaro el diccionario personas para utilizarlo mas tarde
    personas = {}

    while True: 
        nombre = input("Introduce el nombre (o salir para terminar): ")
        if nombre.lower() == 'salir':
            break

        edad = int(input("Introduce la edad: "))
        direccion = str(input("Introduce la dirección: "))
        telefono = str(input("Introduce el telefono: "))

        #Aqui guardaré la información en el diccionario persona, previamente declarado
        personas[nombre] = {
            "edad": edad,
            "direccion": direccion,
            "telefono": telefono
        }

    print("\nLista de personas registradas")
    for nombre, datos in personas.items():
        print(f"{nombre} tiene {datos['edad']} años, vive en {datos['direccion']} y su número de teléfono es {datos['telefono']}")

    print("---------------------")

def ejercicio2():
    ventas = {
        "A": {1: 5, 2: 3, 3: 6, 4: 8, 5: 1},
        "B": {1: 3, 2: 7, 3: 2, 4: 0, 5: 4},
        "C": {1: 6, 2: 4, 3: 3, 4: 5, 5: 2},
        "D": {1: 0, 2: 2, 3: 1, 4: 3, 5: 0}
    }

    print("Total de ventas mensuales por producto")
    total_mensual = {}

    for producto in ventas:
        total = 0
        for dia in ventas[producto]:
            total += ventas[producto][dia]
        total_mensual[producto] = total
        print(f"{producto}: {total} unidades")

    producto_mas = None
    producto_menos = None
    mayor_venta = -1
    menor_venta = 99999

    for producto in total_mensual:
        if total_mensual[producto] > mayor_venta:
            mayor_venta = total_mensual[producto]
            producto_mas = producto
        if total_mensual[producto] < menor_venta:
            menor_venta = total_mensual[producto]
            producto_menos = producto
    
    print("---------------------")

    print(f"Producto más vendido {producto_mas} con {mayor_venta}")
    print(f"Producto menos vendido {producto_menos} con {menor_venta}")

    print("---------------------")

    print(f"Ventas diarias del producto más vendido ({producto_mas}):")
    for dia in ventas[producto_mas]:
        print(f"Dia {dia}: {ventas[producto_mas][dia]} unidades")

    print("---------------------")

    print(f"Dia con mayor venta para cada producto:")
    for producto in ventas:
        dia_mayor = 0
        mayor = -1
        for dia in ventas[producto]:
            if ventas[producto][dia] > mayor:
                mayor = ventas[producto][dia]
                dia_mayor = dia
        print(f"{producto}: Día {dia_mayor} con {mayor} unidades")

    print("---------------------")


while True:
    opcion = input("MENU DE OPCIONES"
    "\na. Ejercicio 1" 
    "\nb. Ejercicio 2"
    "\nc. Salir"
    "\n")
    match(opcion.lower()):
        case "a":
            ejercicio1()
        case "b":
            ejercicio2()
        case "c":
            print("Saliendo del programa...")
            exit()
        case _:
            print("Valor desconocido")