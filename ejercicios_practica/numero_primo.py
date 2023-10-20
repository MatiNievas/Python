# Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.


def is_prime():
    
    for number in range(1, 101): 
        is_divisible = False

        for i in range(2, number):
            if number % i == 0:
                is_divisible = True
                break
                
        if not is_divisible:
            print(number)

is_prime()


 