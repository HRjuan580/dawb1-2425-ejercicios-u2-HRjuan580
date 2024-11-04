# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
def pedir_numero():
    while True:
        try:
            numero = int(input("Introduce un número entero positivo: "))
            if numero <= 0:
                raise ValueError("El número debe ser mayor que cero.")
            return numero
        except ValueError as e:
            print(f"Error: {e}. Por favor, inténtalo de nuevo.")

def obtener_numeros_impares(numero):
    impares = []
    for i in range(1, numero + 1):
        if i % 2 != 0:  # Verifica si el número es impar
            impares.append(str(i))
    return ', '.join(impares)

def main():
    print("Bienvenido al programa que muestra números impares.")
    numero = pedir_numero()
    numeros_impares = obtener_numeros_impares(numero)
    print(f"Números impares desde 1 hasta {numero}: {numeros_impares}")

if __name__ == "__main__":
    main()
