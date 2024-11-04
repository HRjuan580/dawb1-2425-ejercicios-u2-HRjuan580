"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****
"""


def pedir_numero():
    while True:
        try:
            numero = int(input("Introduce un número entero positivo para la altura del triángulo: "))
            if numero <= 0:
                raise ValueError("El número debe ser positivo.")
            return numero
        except ValueError as e:
            print(f"Error: {e}. Por favor, inténtalo de nuevo.")

def imprimir_triangulo(altura):
    print("\nTriángulo rectángulo de altura", altura)
    for i in range(1, altura + 1):
        linea = '*' * i
        print(linea)

def main():
    altura = pedir_numero()
    imprimir_triangulo(altura)

if __name__ == "__main__":
    main()
