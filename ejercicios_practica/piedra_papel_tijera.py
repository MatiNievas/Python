# "Piedra, Papel o Tijera"

from random import randint

choice = ["piedra", "papel", "tijera", "lagarto", "spock"]
computer = choice[randint(0,2)]
player = input("piedra, papel, tijera, lagarto o spock: ").lower()
print(f"La computadora eligió: {computer}")

if player == computer:
    print("Empate")
elif player == "piedra" and computer == "tijera":
    print("Ganó el jugador")
elif player == "piedra" and computer == "lagarto":
    print("Ganó el jugador")
elif player == "papel" and computer == "piedra":
    print("Ganó el jugador")
elif player == "papel" and computer == "spock":
    print("Ganó el jugador")
elif player == "tijera" and computer == "papel":
    print("Ganó el jugador")
elif player == "tijera" and computer == "lagarto":
    print("Ganó el jugador")
elif player == "lagarto" and computer == "papel":
    print("Ganó el jugador")
elif player == "lagarto" and computer == "spock":
    print("Ganó el jugador")
elif player == "spock" and computer == "piedra":
    print("Ganó el jugador")
elif player == "spock" and computer == "tijera":
    print("Ganó el jugador")
else:
    print("Ganó la computadora")
