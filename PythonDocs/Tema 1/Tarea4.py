import math
import random

# --- OPCIÓN a: Mostrar un rombo ---
def mostrar_rombo():
    n = int(input("Introduce un número impar: "))
    while n % 2 == 0:
        n = int(input("Debe ser impar. Introduce otro número: "))
    for i in range(1, n + 1, 2):
        print(("*" * i).center(n))
    for i in range(n - 2, 0, -2):
        print(("*" * i).center(n))

# --- OPCIÓN b: Adivinar un número ---
def adivinar_numero():
    secreto = random.randint(1, 100)
    num = 0
    while num != secreto:
        num = int(input("Adivina el número (1-100): "))
        if num < secreto:
            print("El número es mayor.")
        elif num > secreto:
            print("El número es menor.")
    print("Has acertado!")

# --- OPCIÓN c: Ecuación de segundo grado ---
def resolver_ecuacion():
    a = float(input("Introduce a: "))
    b = float(input("Introduce b: "))
    c = float(input("Introduce c: "))
    if a == 0:
        print("No es una ecuación de segundo grado.")
    else:
        d = b**2 - 4*a*c
        if d < 0:
            print("No tiene solución real.")
        elif d == 0:
            x = -b / (2*a)
            print("Una solución:", x)
        else:
            x1 = (-b + math.sqrt(d)) / (2*a)
            x2 = (-b - math.sqrt(d)) / (2*a)
            print("Soluciones:", x1, "y", x2)

# --- OPCIÓN d: Tabla de números ---
def tabla_numeros():
    filas = int(input("Número de filas: "))
    columnas = int(input("Número de columnas: "))
    for i in range(filas):
        for j in range(columnas):
            print(random.randint(0, 99), end="\t")
        print()

# --- OPCIÓN e: Factorial ---
def calcular_factorial():
    n = int(input("Introduce un número: "))
    f = 1
    for i in range(1, n + 1):
        f *= i
    print("El factorial de", n, "es", f)

# --- OPCIÓN f: Fibonacci ---
def calcular_fibonacci():
    n = int(input("Introduce la posición: "))
    if n <= 2:
        print("El número de Fibonacci es 1")
    else:
        a, b = 1, 1
        for i in range(n - 2):
            a, b = b, a + b
        print("El número de Fibonacci en la posición", n, "es", b)

# --- OPCIÓN g: Tabla de multiplicar ---
def tabla_multiplicar():
    n = int(input("Introduce un número: "))
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

# --- MENÚ PRINCIPAL ---
def menu():
    while True:
        print("\nMENÚ DE OPCIONES")
        print("a) Mostrar un rombo")
        print("b) Adivinar un número")
        print("c) Resolver una ecuación de segundo grado")
        print("d) Tabla de números")
        print("e) Cálculo del número factorial")
        print("f) Cálculo de un número de la sucesión de Fibonacci")
        print("g) Tabla de multiplicar")
        print("h) Salir")

        opcion = input("Elige una opción: ").lower()

        if opcion == "a":
            mostrar_rombo()
        elif opcion == "b":
            adivinar_numero()
        elif opcion == "c":
            resolver_ecuacion()
        elif opcion == "d":
            tabla_numeros()
        elif opcion == "e":
            calcular_factorial()
        elif opcion == "f":
            calcular_fibonacci()
        elif opcion == "g":
            tabla_multiplicar()
        elif opcion == "h":
            print("Fin del programa.")
            break
        else:
            print("Opción incorrecta.")

        input("Pulsa ENTER para continuar...")

# --- PROGRAMA PRINCIPAL ---
menu()
