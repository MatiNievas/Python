


from random import randint

choice = ["piedra", "papel", "tijera"]
computer = choice[randint(0,2)]
player = input("piedra, papel o tijera: ").lower()
print(f"La computadora eligió: {computer}")

if player == computer:
    print("Empate")
elif player == "piedra" and computer == "papel":
    print("Ganó la computadora")
elif player == "piedra" and computer == "tijera":
    print("Ganó el jugador")
elif player == "papel" and computer == "piedra":
    print("Ganó el jugador")
elif player == "papel" and computer == "tijera":
    print("Ganó la computadora")
elif player == "tijera" and computer == "papel":
    print("Ganó el jugador")
elif player == "tijera" and computer == "piedra":
    print("Ganó la computadora")


