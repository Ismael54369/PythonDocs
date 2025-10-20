def ejercicio1():
    print("EJERCICIO 1")
    print("---------------------")

    num = int(input("Introduzca un numero (0 para salir): "))
    lista = []
    while num != 0 : 
        lista.append(num)
        num = int(input("Introduzca un numero (0 para salir): "))
        
    
    print("Orden de introduccion: ", lista)
    lista.sort()
    print("Ordenado: ", lista)
    lista.reverse()
    print("Invertido: ", lista)
    print("---------------------")

def ejercicio2():
    print("EJERCICIO 2")
    print("---------------------")

    cadena = input("Introduzca una cadena de caracteres ('' o ' ' para salir): ")
    lista = []

    while cadena != "" and cadena != " ":
        lista.append(cadena)
        cadena = input("Introduzca una cadena de caracteres ('' o ' ' para salir): ")

    print("Orden de introduccion: ", lista)
    lista.sort(key=str.lower)
    print("Ordenado: ", lista)
    lista.reverse()
    print("Invertido: ", lista)
    print("---------------------")

def ejercicio3():
    print("EJERCICIO 3")
    print("---------------------")

    def palindromo(str1):
        esPalindromo = False
        invertida = "".join(reversed(str1))
        if (str1.lower() == invertida.lower()):
            esPalindromo = True
        return esPalindromo
    
    cadena = input("Introduzca una cadena de caracteres: ")

    if (palindromo(cadena)):
        print("La cadena ", cadena, " es palindromo")
    else:
        print("La cadena ", cadena, " no es palindromo")
    
    print("---------------------")


def ejercicio4():
    print("EJERCICIO 4")
    print("---------------------")

    def palindromoCase(str1, str2):
        esPalindromo = False
        if (str1.lower() == str2.lower()):
            esPalindromo = True
        return esPalindromo
    
    def palindromo(str1, str2):
        esPalindromo = False
        if (str1 == str2):
            esPalindromo = True
        return esPalindromo
    
    cadena1 = input("Introduzca la primera cadena: ")
    cadena2 = input("Introduzca la segunda cadena: ")
    opcion = input("¿Quiere tener en cuenta mayuscula/minuscula (y/n): ")
    opcion.lower
    
    match(opcion):
        case "n":
            if (palindromoCase(cadena1, cadena2)):
                print("La cadena 1, ", cadena1, ", y la cadena 2, ", cadena2, " son palindromos")
            else:
                print("La cadena 1, ", cadena1, ", y la cadena 2, ", cadena2, " no son palindromos")

        case "y":
            if (palindromo(cadena1, cadena2)):
                print("La cadena 1, ", cadena1, ", y la cadena 2, ", cadena2, " son palindromos")
            else:
                print("La cadena 1, ", cadena1, ", y la cadena 2, ", cadena2, " no son palindromos")
        case _:
            print("ERROR: DEBE INTRODUCIR Y/N")
    
    print("---------------------")

while True:
    opcion = input("Introduce una letra"
    "\na. Ejercicio 1" 
    "\nb. Ejercicio 2" 
    "\nc. Ejercicio 3" 
    "\nd. Ejercicio 4"
    "\ne. Salir"
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
            print("Saliendo del programa...")
            exit()
        case _:
            print("Valor desconocido")
