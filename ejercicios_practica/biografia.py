# Información de la biografía
# Pregunte a un usuario su información personal en una sola ronda de preguntas.
# Luego hay que verificar que la información que se ha ingresado sea válida. 
# Finalmente, se imprime un resumen de toda la información que ha sido ingresada.

import re

name = input("Ingrese su nombre: ").capitalize()
while not name.isalpha: 
    print("ERROR. Ingrese un nombre valido. Pruebe denuevo.")
    name.capitalize = input("Ingrese su nombre: ").capitalize()

last_name = input("Ingrese su apellido: ").capitalize()
while not last_name.isalpha():
    print("ERROR. Ingrese un apellido valido. Pruebe denuevo.")
    last_name = input("Ingrese su apellido: ").capitalize()

date_pattern = r"^[a-z]{3} \d{1,2}, \d{4}$"  # Example: "Jan 1, 1954"

date = input("Ingrese su fecha de nacimiento (ejemplo: Jan 1, 1954): ").capitalize()
while not re.match(date_pattern, date, re.I):
    print("ERROR. Ingrese una fecha válida en el formato indicado. Pruebe denuevo.")
    date = input("Ingrese su fecha de nacimiento (ejemplo: Jan 1, 1954): ").capitalize()
    
address = input("Ingrese su domicilio: ").capitalize()
while len(address) < 5: 
    print("ERROR. Ingrese un domicilio válido. Pruebe denuevo.")
    address = input("Ingrese su domicilio: ").capitalize()

while True:
    age = input("Ingrese su edad: ")
    try:
        age = int(age) 
        if age > 0:
            break  
        else:
            print("ERROR. Ingrese una edad mayor a 0. Pruebe denuevo.")
    except ValueError:
        print("ERROR. El dato ingresado no es un número válido. Pruebe denuevo.")

     
     
print(f"Nombre: {name} {last_name}")
print(f"Fecha de nacimiento: {date}")
print(f"Dirección: {address}")
print(f"Edad: {age}")




