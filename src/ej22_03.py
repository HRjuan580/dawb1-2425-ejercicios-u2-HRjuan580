"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""



def pedir_entero():
    while True:
        try: 
            numero = int(input("Introduce un número entero positivo: "))
            if numero <= 0:
                print("El numero introducido debe ser positivo. Intentalo de nuevo.")
                continue
            return numero
        except ValueError:
            print("Entrada no valida. Por favor, introduce un numero entero.")


def generar_impares(numero):
    impares = []
    for i in range(1, numero + 1, 2):
        impares.append(str(i))
    return impares


def imprimir_impares(numero, impares):
    print("Numeros impares desde 1 hasta  {}: { }".format(numero, ",".join(impares)))

def main():
    numero = pedir_entero()
    impares = generar_impares(numero)
    imprimir_impares(numero, impares)


if __name__ == "__main__":
    main()
    