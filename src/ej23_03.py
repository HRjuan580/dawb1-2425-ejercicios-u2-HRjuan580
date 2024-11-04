#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.

def pedir_numero():
    while True:
        try:
            numero = int(input("Introduce un número entero positivo: "))
            if numero < 1:
                raise ValueError("El número debe ser mayor que cero.")
            return numero
        except ValueError as e:
            print(f"Error: {e}. Por favor, inténtalo de nuevo.")

def cuenta_atras(numero):
    return ', '.join(str(i) for i in range(numero, -1, -1))

def main():
    print("Bienvenido al programa de cuenta atrás.")
    numero = pedir_numero()
    resultado = cuenta_atras(numero)
    print(f"Cuenta atrás desde {numero} hasta 0: {resultado}")

if __name__ == "__main__":
    main()


