# Un polideportivo necesita un sistema que le permita administrar los alquileres de sus diferentes canchas. 
# Cada cancha posee un valor de base por hora, y en algunos casos pueden tener agregados, se detalla a continuación: 

# Canchas de tenis: 
# Valor: $200. 
# Opcional: 1 árbitro, adiciona $100 al valor de la cancha y la ganancia del juez es de $50. 

# Canchas de fútbol 5:  
# Valor: $500 
# No posee adicionales. 

# Canchas de fútbol 7: 
# Valor: $650. 
# Opcional: 1 árbitro, adiciona $100 al valor de la cancha y la ganancia del juez es de $50. 

# Canchas de fútbol 11: 
# Valor: $800. 
# Opcional 1: 1 árbitro, adiciona $100 al valor de la cancha y la ganancia del juez es de $50. 
# Opcional 2: Agregando el “opcional 1” se puede agregar 2 jueces de línea al alquiler, incrementando $90 al costo total, 
# y la recaudación de cada juez de línea es de $35.  

# De cada juez se registra, el nombre, apellido y el legajo. 
 

# Obtener la recaudación total del polideportivo. 
# Obtener la ganancia total del polideportivo (Descontando los gastos de los jueces). 
# Obtener la cancha que más se alquiló. 
# Obtener la cancha que más recaudó. 
# Obtener el juez que más partidos dirigió. 
# Obtener el juez que con mayor recaudación. 
# No permitir que un juez pueda dirigir 2 partidos en simultáneo. 
# No permitir que los alquileres de las canchas se superpongan, administrarlos por horarios


class juez:
    def __init__(self):
        pass

class canchas:
    def __init__(self):
        tipo_cancha = input("Ingrese el tipo de cancha que desee usar\n")
        precio_cancha = self.obtener_precio_cancha(tipo_cancha)
        
    def obtener_precio_cancha(self, tipo_cancha):
        if tipo_cancha == "tenis":
            return 200
        if tipo_cancha == "futbol 5":
            return 500
        if tipo_cancha == "futbol 7":
            return 650
        if tipo_cancha == "futbol 11":
            return 800
        
        

class polideportivo:
    def __init__(self) -> None:
        pass