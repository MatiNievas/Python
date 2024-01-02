# Crea un programa que calcule los puntos de una palabra.
# - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
#   español de 27 letras, la A vale 1 y la Z 27.
# - El programa muestra el valor de los puntos de cada palabra introducida.
# - El programa finaliza si logras introducir una palabra de 100 puntos.
# - Puedes usar la terminal para interactuar con el usuario y solicitarle
#   cada palabra.

def calcular_puntos(palabra):
    puntos = 0
    for letra in palabra.lower():
        
        if 'a' <= letra <= 'z':
            puntos += ord(letra) - ord('a') + 1
        else:
            print("Error: La palabra debe contener solo letras del alfabeto español.")
            return 0
    return puntos

def main():
    while True:
        palabra = input("Introduce una palabra: ")
        puntos = calcular_puntos(palabra)
        
        if puntos == 100:
            print(f"Felicidades, has alcanzado los 100 puntos con la palabra '{palabra}'!")
            break
        else:
            print(f"La palabra '{palabra}' tiene {puntos} puntos.")

if __name__ == "__main__":
    main()
