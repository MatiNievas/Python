# Par o impar
# Lo primero que vamos a realizar es dar la bienvenida preguntando un número entre 1 y 1000

# Cuando el usuario proporciona el número, comprobaremos si es par o impar y después imprimimos el mensaje con el resultado.

# Ejemplo:

# Mensaje que se muestra: ¿En qué número estás pensando?
# Entrada: 25
# Salida: ¡Es un número impar! ¿Puedes añadir otro?

number = float(input("¿En qué número estás pensando?\n"))

if number % 2 == 0:
    print("¡Es un número par!")
    
else:
    print("¡Es un número impar!")