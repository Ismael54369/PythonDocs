entrada_usuario = "veinte"

try:
    numero = int(entrada_usuario)
    print(f"El número es {numero}")
except ValueError:
    # Este bloque solo se ejecuta si falla la conversión de tipo
    print(f"❌ Error: '{entrada_usuario}' no es un número válido.")
except Exception as e:
    # Captura cualquier otro error imprevisto
    print(f"Ocurrió un error desconocido: {e}")