def ejercicio1():
    texto = input("Introduce un texto: ")

    for letra in texto:
        print(letra)

def ejercicio2():
    numero = int(input("Introduce un número: "))
    factorial = 1

    for i in range(1, numero + 1):
        factorial *= i

    print(f"El factorial de {numero} es {factorial}")

def ejercicio3():
    numeros = []

    while True:
        n = float(input("Introduce un número (0 para terminar): "))
        if n == 0:
            break
        numeros.append(n)

    if numeros:
        print(f"Números introducidos: {len(numeros)}")
        print(f"Mínimo: {min(numeros)}")
        print(f"Máximo: {max(numeros)}")
        print(f"Suma: {sum(numeros)}")
        print(f"Media: {sum(numeros) / len(numeros)}")
    else:
        print("No se introdujeron números.")

def ejercicio4():
    n = int(input("Introduce un número: "))

    for i in range(1, n + 1):
        print("*" * i)

def ejercicio5():
    n = int(input("Introduce un número: "))

    for i in range(1, n + 1):
        print(i ** 2, end=" ")
    print()

def ejercicio6():
    filas = int(input("Introduce el número de filas: "))
    columnas = int(input("Introduce el número de columnas: "))

    contador = 1
    for i in range(filas):
        for j in range(columnas):
            print(contador, end=" ")
            contador += 1
        print()

def ejercicio7():
    texto = input("Introduce una cadena de texto: ")
    letra = input("Introduce una letra a buscar: ")

    contador = 0

    for caracter in texto:
        if caracter == letra:
            contador += 1

    print(f"La letra '{letra}' aparece {contador} veces en el texto.")

def ejercicio8():
    numero = int(input("Introduce un número: "))

    if numero <= 1:
        print("No es primo.")
    else:
        es_primo = True
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break

        if es_primo:
            print("Es primo.")
        else:
            print("No es primo.")

def ejercicio9():
    while True:
        numero = int(input("Introduce un número impar: "))
        if numero % 2 != 0:
            break
        print("El número no es impar. Intenta de nuevo.")

    for i in range(1, numero + 1, 2):
        print("*" * i)

def ejercicio10():
    n = int(input("Introduce un número: "))

    for i in range(n):
        for j in range(i + 1):
            print(2 * (i - j) + 1, end=" ")
        print()

while True:
    opcion = input("Introduce una letra"
    "\na. Ejercicio 1" 
    "\nb. Ejercicio 2" 
    "\nc. Ejercicio 3" 
    "\nd. Ejercicio 4"
    "\ne. Ejercicio 5"
    "\nf. Ejercicio 6"
    "\ng. Ejercicio 7"
    "\nh. Ejercicio 8"
    "\ni. Ejercicio 9"
    "\nj. Ejercicio 10"
    "\nk. Salir"
    "\n")
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
            ejercicio6()
        case "g":
            ejercicio7()
        case "h":
            ejercicio8()
        case "i":
            ejercicio9()
        case "j":
            ejercicio10()
        case "k":
            print("Saliendo del programa...")
            exit()
        case _:
            print("Valor desconocido")