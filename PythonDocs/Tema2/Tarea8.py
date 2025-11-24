class Persona:
    # A. Constructor con datos opcionales (por defecto cadenas vacías o 0)
    def __init__(self, nombre="", apellidos="", dni="", edad=0):
        # Inicializamos las variables internas
        self._nombre = ""
        self._apellidos = ""
        self._dni = ""
        self._edad = 0
        
        # Llamamos a los setters para validar los datos iniciales
        self.set_nombre(nombre)
        self.set_apellidos(apellidos)
        self.set_dni(dni)
        self.set_edad(edad)

    # B. Setters (Validaciones)
    def set_nombre(self, nombre):
        if len(nombre) > 0:
            self._nombre = nombre.upper() # Guardar en mayúsculas
        else:
            print("El nombre no puede estar vacío.")

    def set_apellidos(self, apellidos):
        if len(apellidos) > 0:
            self._apellidos = apellidos.upper()
        else:
            print("Los apellidos no pueden estar vacíos.")

    def set_dni(self, dni):
        if len(dni) > 0:
            self._dni = dni.upper()
        else:
            print("El DNI no puede estar vacío.")

    def set_edad(self, edad):
        if edad >= 0:
            self._edad = edad
        else:
            print("La edad debe ser un entero positivo.")

    # C. Getters (Para recuperar los valores)
    def get_nombre(self):
        return self._nombre

    def get_apellidos(self):
        return self._apellidos

    def get_dni(self):
        return self._dni

    def get_edad(self):
        return self._edad

    # D. Mostrar datos
    def mostrar(self):
        print(f"PERSONA: {self._nombre} {self._apellidos} | DNI: {self._dni} | Edad: {self._edad}")

    # E. Es mayor de edad
    def mayorDeEdad(self):
        return self._edad >= 18
    

class Cuenta:
    # A. Constructor: Titular obligatorio, cantidad opcional (0.0 por defecto)
    def __init__(self, titular, cantidad=0.0):
        self._titular = titular # Esto será un objeto de la clase Persona
        self._cantidad = cantidad

    # B. Getters y Setters
    def get_titular(self):
        return self._titular

    def set_titular(self, titular):
        self._titular = titular

    def get_cantidad(self):
        return self._cantidad
    
    # No hacemos set_cantidad porque se modifica con ingresar/retirar

    # C. Ingresar dinero
    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad
        else:
            print("La cantidad a ingresar debe ser positiva.")

    # D. Retirar dinero
    def retirar(self, cantidad):
        if cantidad > 0:
            self._cantidad -= cantidad # Puede quedar en negativo (números rojos)
        else:
            print("La cantidad a retirar debe ser positiva.")

    # E. Mostrar datos de la cuenta
    def mostrar(self):
        print("--- DATOS DE LA CUENTA ---")
        print(f"Titular: {self._titular.get_nombre()} {self._titular.get_apellidos()}")
        print(f"Saldo actual: {self._cantidad:.2f}€")


class CuentaJoven(Cuenta):
    # Constructor
    def __init__(self, titular, cantidad=0.0, bonificacion=0):
        # Llamamos al constructor de la clase Padre (Cuenta)
        super().__init__(titular, cantidad)
        # Gestionamos el atributo nuevo
        self._bonificacion = 0
        self.set_bonificacion(bonificacion)

    # A. Setter para bonificación (0-100%)
    def set_bonificacion(self, bonificacion):
        if 0 <= bonificacion <= 100:
            self._bonificacion = bonificacion
        else:
            print("La bonificación debe estar entre 0% y 100%")

    def get_bonificacion(self):
        return self._bonificacion

    # B. Método mostrar adaptado (Polimorfismo)
    def mostrar(self):
        print("--- CUENTA JOVEN ---")
        # Mostramos los datos básicos de la cuenta
        print(f"Titular: {self._titular.get_nombre()} {self._titular.get_apellidos()}")
        print(f"Saldo: {self._cantidad:.2f}€")
        print(f"Bonificación: {self._bonificacion}%")
        # Validación extra de edad para ver si es válida
        if self._titular.get_edad() < 25:
             print("(Cuenta válida: Titular menor de 25 años)")
        else:
             print("(ALERTA: El titular es mayor de 25 años)")


if __name__ == "__main__":
    # --- PRUEBA 1: CUENTA NORMAL ---
    print("\n>>> CREANDO CUENTA NORMAL")
    # 1. Creamos una persona
    persona1 = Persona("Juan", "Perez Garcia", "12345678A", 40)
    
    # 2. Creamos la cuenta asociada a esa persona
    cuenta1 = Cuenta(persona1, 500.0)
    
    # 3. Operaciones
    cuenta1.ingresar(200)   # Saldo 700
    cuenta1.retirar(800)    # Saldo -100 (Números rojos)
    cuenta1.mostrar()

    # --- PRUEBA 2: CUENTA JOVEN ---
    print("\n>>> CREANDO CUENTA JOVEN")
    # 1. Creamos una persona joven
    persona2 = Persona("Ana", "Lopez", "87654321B", 22)
    
    # 2. Creamos la cuenta joven (con 10% de bonificación)
    # Nota: Aunque definimos cantidad 0 por defecto, aquí ponemos 1000
    cuenta_joven = CuentaJoven(persona2, 1000, 10)
    
    # 3. Operaciones
    cuenta_joven.ingresar(50)
    cuenta_joven.mostrar()

    # --- PRUEBA DE VALIDACIONES ---
    print("\n>>> PRUEBA DE VALIDACIONES")
    # Intentar poner nombre vacío
    p3 = Persona("", "Test", "111", 20) 
    
    # Intentar bonificación errónea
    c3 = CuentaJoven(persona2, 0, 150) # Dará error de bonificación
    