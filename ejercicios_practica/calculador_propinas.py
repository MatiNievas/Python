# Calculador de propinas

bill = float(input("Por favor ingrese el total de la factura: "))
people = int(input("¿Cuantas personas van a pagar la factura?: ")) 
tip = round(bill * 0.10, 2)
total = round(bill + tip, 2)

if people > 1:
    division = float(round(total / people, 2))
    print(f"La propina aplicando el 10% es de {tip}, que da un total de {total}, cada uno debe pagar {division}.")
else:
    print(f"La propina aplicando el 10% es de {tip}, que da un total de {total}.")