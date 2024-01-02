# Contador de palabras
# Preguntamos al usuario en que está pensando.
# Cuando se introduce la respuesta, realizará el conteo de palabras en la sentencia e imprimimos en la salida el resultado.

def count_words(sentece):
    words = sentece.split()
    return len(words)

def main():
    ask = input("¿En qué estás pensando?\n")

    numbers_words = count_words(ask)

    print(f"Me has mostrado tu pensamiento en {numbers_words} palabras")

