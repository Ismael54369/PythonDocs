"""1. Escriba un programa que recoja un valor por teclado y muestre de qué tipo es."""
valor = input("Introduce un valor: ")
print("El valor introducido es:", valor)
print("El tipo de dato es:", type(valor))

"""2. Escribe un programa que recoja dos números enteros por teclado y muestre
los siguientes resultados: suma, resta, multiplicación, división real, división
entera, resto de la división entera y potencia."""
num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))
suma = num1 + num2
resta = num1 - num2 
multiplicacion = num1 * num2
division_real = num1 / num2
division_entera = num1 // num2
resto = num1 % num2
potencia = num1 ** num2
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División real:", division_real)
print("División entera:", division_entera)
print("Resto de la división entera:", resto)
print("Potencia:", potencia)


"""3. Escribe un programa que pida el nombre del usuario y le responda con un
saludo. En el saludo deberá utilizarse el nombre que introdujo el usuario."""
nombre = input("Introduce tu nombre: ")
print("Hola, " + nombre + "!")

"""4. Escribe un programa que recoja tres números y calcule su media aritmética."""
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))
media = (num1 + num2 + num3) / 3
print("La media aritmética es:", media)

"""5. Escribe un programa que recoja un número y muestre su valor absoluto."""
num = float(input("Introduce un número: "))  
print("El valor absoluto es:", abs(num))

"""6. Escribe un programa que recoja las notas de las tres evaluaciones de un
alumno. A continuación debe calcular y mostrar la nota final, teniendo en
cuenta que la primera evaluación cuenta un 20% de la nota final, la segunda
evaluación un 35% y la tercera evaluación un 45%."""
eval1 = float(input("Introduce la nota de la primera evaluación: "))
eval2 = float(input("Introduce la nota de la segunda evaluación: "))
eval3 = float(input("Introduce la nota de la tercera evaluación: "))
nota_final = (eval1 * 0.20) + (eval2 * 0.35) + (eval3 * 0.45)
print("La nota final es:", nota_final)

"""7. Escribe un programa que recoja un número y muestre su representación en
código binario."""
num = int(input("Introduce un número entero: "))
binario = bin(num)[2:]  # Convertir a binario y eliminar el prefijo '0b'
print("La representación en código binario es:", binario)

"""8. Escribe un programa que recoja un texto y lo muestre cinco veces
consecutivas en la misma línea."""
texto = input("Introduce un texto: ")
print(texto+" " * 5)

"""9. Escribe un programa que recoja un texto y que muestre su longitud."""
texto = input("Introduce un texto: ")
print("La longitud del texto es:", len(texto))

"""""10.Escribe un programa que recoja la edad del usuario y muestre la edad que
tendrá dentro de 5, 10 y 15 años."""
edad = int(input("Introduce tu edad: "))
print("Dentro de 5 años tendrás:", edad + 5)
print("Dentro de 10 años tendrás:", edad + 10)
print("Dentro de 15 años tendrás:", edad + 15)
