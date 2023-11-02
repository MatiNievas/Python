#Adivina el número oculto
# Debemos de preguntar al usuario un número entre 1 y 50.
# Si añaden un número fuera de ese rango, vamos a indicar con un error que anime a elegir un número dentro del rango adecuado..
# Si no acertamos el número oculto, preguntaremos al usuario si queremos seguir jugando, introduciendo un nuevo número o queremos dejar de jugar.
# Finalmente, cuando el usuario acierta correctamente el número oculto, mostramos un mensaje de enhorabuena y mostramos el número de intentos
# que hemos utilizado para llegar a esta situación.

import random

number = random.randrange(1, 50)
guess = int(input("Adivina el número entre 1 y 50: \n"))
attempts = 0

while guess != number:
    if guess < 1 or guess > 50:
        print("El número que elegiste está fuera de rango. Prueba de nuevo.")
        #attempts += 1        
    elif guess < number:
        print("El número que elegiste es más chico que el que pensé. Prueba de nuevo.")
        #attempts += 1
    else:
        print("El número que elegiste es más grande que el que pensé. Prueba de nuevo.")
        #attempts += 1
    guess = int(input("Adivina el número entre 1 y 50: \n"))
    attempts += 1

print(f"¡Felicidades, adivinaste el número en {attempts} intentos!")
