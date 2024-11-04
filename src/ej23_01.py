# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


def pedir_edad():
    while True:
        try:
            edad = int(input("Por favor, introduce tu edad: "))
            if edad < 1:
                raise ValueError("La edad debe ser un número entero positivo.")
            return edad
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")

def mostrar_anos_cumplidos(edad):
    print(f"\nHas cumplido los siguientes años:")
    for año in range(1, edad + 1):
        print(año)

def main():
    print("Bienvenido al programa de edad.")
    edad = pedir_edad()
    mostrar_anos_cumplidos(edad)
    print("¡Gracias por usar el programa!")

if __name__ == "__main__":
    main()


