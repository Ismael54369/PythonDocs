def ejercicio1():
    frase = str(input("Introduzca una frase: "))
    
    frase.lower()

    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

    fraseSin = ""

    for letra in frase:
        for vocal in vocales:
            if (letra == vocal):
                letra = "*"
        fraseSin += letra

    print(fraseSin)

def ejercicio2():
    numIntroducir = int(input("¿Cuantos numeros vas a introducir?"))

    numeros = []

    for i in range(numIntroducir):
        num = int(input("Introduce un numero: "))

        if (i != 0):
            if (num < numeros[i - 1]):
                print("Tu numero es mas bajo que el anterior")
    
        numeros.append(num)

def ejercicio3():
    frase = input("Introduce una frase para hallar la palabra mas larga: ")

    arrayFrase = frase.split(" ")
    palabraLarga = ""

    for palabra in arrayFrase:
        if (len(palabra) > len(palabraLarga)):
            palabraLarga = palabra

    print("La palabra mas larga es: ", palabraLarga)

def ejercicio4():
    filas = int(input("Número de filas: "))
    columnas = int(input("Número de columnas: "))

    num = 101

    for i in range(filas):
        for j in range(columnas):
            num -= 2
            if (num < 1):
                num = 99
            print((num), end="\t")
        print()  

def ejercicio5():
    print("Este ejercicio no esta hecho, lo siento")


while True:
    opcion = input("Introduce una letra"
    "\na. Ejercicio 1" 
    "\nb. Ejercicio 2" 
    "\nc. Ejercicio 3" 
    "\nd. Ejercicio 4"
    "\ne. Ejercicio 5"
    "\nf. Salir"
    "\n").lower()
    match(opcion):
        case "a":
            ejercicio1()
        case "b":
            ejercicio2()
        case "c":
            ejercicio3()
        case "d":
            ejercicio4()
        case "e":
            ejercicio5()
        case "f":
            print("Saliendo del programa...")
            exit()
        case _:
            print("Valor desconocido")