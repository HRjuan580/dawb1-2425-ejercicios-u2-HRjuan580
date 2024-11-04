"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""
def pedir_numero():
    while True: 
        try:
            numero = int(input("Introduce un numero entero positivo: "))
            if numero < 0:
                raise ValueError("El numero debe ser positivo")
            return numero
        except ValueError:
            print(f"*Error* Por favor, intentelo de nuevo.")

def cuenta_atras(numero):
    resultado = []
    for i in range(numero, -1, -1):
        resultado.append(str(i))
    return ",".join(resultado)

def main():
    numero = pedir_numero()
    resultado = cuenta_atras(numero)
    print(f"Cuenta atras: {resultado}")


if __name__ == "__main__":
    main()