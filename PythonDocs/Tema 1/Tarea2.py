from datetime import datetime

ejercicio = int(input("Introduzca el numero del ejercicio a resolver: "))

"""1. Escribe un programa que recoja un número e indique si se trata de un número  
par o impar."""
if ejercicio == 1:
    num1 = int(input("Introduce un numero: "))
    if num1 % 2 == 0:
        print("Su numero es par")
    else:
        print("Su numero es impar")

"""2. Escribe un programa que recoja un número por teclado y muestre el día de la  
semana que es (1 = Lunes, 2 = Martes…). En caso de introducir un número  incorrecto, 
mostrará el mensaje “Día de la semana incorrecto”."""
if ejercicio == 2:
    dia = int(input("Introduce un numero del 1 al 7: "))
    match dia:
        case 1:
            print("Lunes")
        case 2: 
            print("Martes")
        case 3:
            print("Miercoles")
        case 4:
            print("Jueves")
        case 5:
            print("Viernes")
        case 6|7:
            print("Fin de semana")
        case _:
            print("Su numero no es correcto")

"""3. Escribe un programa que lea tres números y que muestre los números mayor  y menor."""
if ejercicio == 3:
    num1 = int(input("Introduce un numero: "))
    num2 = int(input("Introduce un numero: "))
    num3 = int(input("Introduce un numero: "))
    menor = num1 if num1 < num2 and num1 < num3 else num2 if num2 < num3 else num3
    mayor = num1 if num1 > num2 and num1 > num3 else num2 if num2 > num3 else num3
    print("El numero mayor es ", mayor)
    print("El numero menor es ", menor)

"""4. Escribe un programa que recoja dividendo y divisor, y realice su división siempre 
que el divisor sea distinto de cero."""
if ejercicio == 4:
    dividendo = float(input("Introduce un dividendo para tu division: "))
    divisor = float(input("Introduce un divisor para tu division: "))
    if divisor == 0:
        print("La operación no se puede realizar, el divisor no puede ser 0")
    else:
        print("El resultado de su division es ", dividendo/divisor)

"""5. Escribe un programa que calcule el precio de entrada a un museo a partir de  la edad 
del visitante, teniendo en cuenta que: 
a. Menores de 5 años entran gratis. 
b. Niños entre 5 años y 18 (sin llegar a los 18) pagan 3€. 
c. Mayores de edad hasta los 65 (sin llegar a los 65) pagan 6€. 
d. Jubilados entran gratis."""
if ejercicio == 5: 
    edad = int(input("Introduzca su edad: "))
    if edad < 5 or edad > 65:
        print("Su entrada es gratuita")
    elif edad >=5 and edad < 18:
        print("Su entrada cuesta 3€")
    else:
        print("Su entrada cuesta 6€")

"""6. Escribe un programa que muestre la nota final de un alumno a partir de su  
calificación numérica (valor decimal), teniendo en cuenta que: 
a. Nota menor de 5 es suspenso. 
b. Nota entre 5 y 6 (sin llegar) es suficiente. 
c. Nota entre 6 y 7 (sin llegar) es bien. 
d. Nota entre 7 y 9 (sin llegar) es notable. 
e. Nota entre 9 y 10 (sin llegar) es sobresaliente. 
f. Nota igual a 10 es matrícula de honor. 
g. Cualquier otro valor numérico fuera de este rango es un error."""
if ejercicio == 6:
    nota = float(input("Introduzca su nota: "))
    if nota >= 0 and nota < 5:
        print("Suspenso")
    elif nota >= 5 and nota < 6:
        print("Suficiente")
    elif nota >= 6 and nota < 7:
        print("Bien")
    elif nota >= 7 and nota < 9:
        print("Notable")
    elif nota >= 9 and nota < 10:
        print("Sobresaliente")
    elif nota == 10:
        print("Matricula de honor")
    else:
        print("Valor numerico invalido")

"""7. Escribe un programa que recoja la hora del día y devuelva un saludo, 
según  las siguientes reglas:"""
if ejercicio == 7:
    hora = int(datetime.now().strftime("%H"))
    if hora >= 7 and hora < 12:
        print("Buenos dias")
    elif hora >= 12 and hora < 20:
        print("Buenas tardes")
    else:
        print("Buenas noches")

"""8. Escribe un programa que recoja un mes del año (en número) y devuelva el  
número de días que tiene el mes. En caso de indicar un mes incorrecto deberá  
mostrar un mensaje de error."""

