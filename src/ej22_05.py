"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# Formula para calcular El capital tras un año.
amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 
"""

def pedir_datos():
    while True:
        try: 
            cantidad = float(input("Introduce la cantidad a invertir: "))
            interes = float(input("Introduce el interes anual (en %): "))
            anios = int(input("Introduce el numero de años: "))
            if cantidad < 0 or interes < 0 or anios < 0:
                raise ValueError
            return cantidad, interes, anios
        except ValueError:
            print(f"*Error* Por favor, intentalo de nuevo.")


def calcular_capital(cantidad, interes, anios):
    capital_anual = []
    for anios in range(1, anios + 1):
        cantidad *= 1 + interes / 100
        capital_anual.append((anios, round(cantidad, 2)))

def mostrar_resultados(capital_anual):
    print("\nCapital obtenido cada año:")
    for anios, capital in capital_anual:
        print(f"Año {anios}: {capital}")

def main():
    cantidad, interes, años = pedir_datos()
    capital_anual = calcular_capital(cantidad, interes, anios)
    mostrar_resultados(capital_anual)

if __name__ == "__main__":
    main()