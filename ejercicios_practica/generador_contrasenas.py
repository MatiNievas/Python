# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# Longitud: Entre 8 y 16.
# Con o sin letras mayúsculas.
# Con o sin números.
# Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)


import random

def password_generator(length=8, capital=False, numbers=False, symbols=False): # inicializo el largo en de la contaseña en 8, y el resto en false
    
    characters = list(range(97, 123)) # en el codigo ASCII las minusculas se encuentran en el rango 97 a 122
    
    if capital:
        characters += list(range(65, 91)) # mayusculas codigo ASCII
        
    if numbers:
        characters += list(range(49, 58)) # numeros en el codigo ASCII
        
    if symbols:
        characters += list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) # simbolos en el codigo ASCII
    
    password = ""
    
    final_length = 8 if length < 8 else 16 if length > 16 else length # si el largo de la contraseña es menor a 8, por defecto queda en 8.
                                                                      # Y si es mayor a 16, quedara en 16.
    
    while len(password) < final_length:
        password += chr(random.choice(characters)) # Random.choice(characters) elige caracteres al azar. El chr busca el rango de characters en el codigo ASCII
    
    return password

# casos de prueba

print(password_generator())
print(password_generator(length=16))
print(password_generator(length=1))
print(password_generator(length=22))
print(password_generator(length=12, capital=True))
print(password_generator(length=12, capital=True, numbers=True))
print(password_generator(length=12, capital=True, numbers=True, symbols=True))