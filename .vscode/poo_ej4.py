# Un after office vende diferentes tipos de cerveza tiradas de barril, las mismas se describen a continuación:

# Rubia de origen nacional, cuyo valor por litro es de $50. 
# Negra de origen nacional, cuyo valor por litro es de $58. 
# Rubia de origen extranjero cuyo valor por litro es de $65. 

# Cada barril puede tener un solo tipo de cerveza, y dada las dimensiones del negocio, el sistema debe contemplar el agregado de barriles en función del tiempo. 
# Cada venta se ve afectada por un cálculo de incremento de valor de la cerveza en un 5%, que depende del tipo de vaso donde se sirve: 

# Chopp de 3/4 litros 
#  Vaso de 1/2 litro 
# Jarra de 3 litros 

 
# 1) Calcular la recaudación total del after. 
# 2) Obtener el barril más y menos cerveza sirvió, y mostrar las cantidades. 
# 3) Obtener el barril que más dinero recaudó. 
# 4) Mostrar la cerveza más vendida. 
# 5) Mostrar la cerveza que generó más ganancia. 
# 6) Obtener la cerveza que se vendió mayor cantidad de litros. 
# 7) Obtener la cerveza que se vendió menor cantidad de litros. 
# 8) Obtener el tipo de vaso que más se solicitó. 
# 9) Calcular el porcentaje de venta de cada tipo de cerveza. 
# 10) Calcular el porcentaje de recaudación de cada tipo de cerveza. 
# 11) Calcular el porcentaje de venta de cada barril. 
# 12) Calcular el porcentaje de recaudación de cada barril.

  
class Barril:
    def __init__(self,tipo_cerveza=None, tipo_vaso=None):
        self.tipo_cerveza = tipo_cerveza
        self.tipo_vaso = tipo_vaso
        self.recaudacion = 0
        self.litros = 0
        self.servir = 0
        self.precio = self.obtener_precio(tipo_cerveza, tipo_vaso)
        
    def obtener_precio(self, tipo_cerveza, tipo_vaso):
        if tipo_cerveza == "Rubia Nacional" and tipo_vaso == "Chopp":
            self.servir +=1
            self.litros += 0.75
            return 50 * 0.75
        elif tipo_cerveza == "Rubia Nacional" and tipo_vaso == "Vaso":
            self.servir +=1
            self.litros += 0.5
            return 50 * 0.5
        elif tipo_cerveza == "Rubia Nacional" and tipo_vaso == "Jarra":
            self.servir +=1
            self.litros += 3
            return 50 * 3
        elif tipo_cerveza == "Negra Nacional" and tipo_vaso == "Chopp":
            self.servir +=1
            self.litros += 0.75
            return 58 * 0.75
        elif tipo_cerveza == "Negra Nacional" and tipo_vaso == "Vaso":
            self.servir +=1
            self.litros += 0.5
            return 58 * 0.5
        elif tipo_cerveza == "Negra Nacional" and tipo_vaso == "Jarra":
            self.servir +=1
            self.litros += 3
            return 58 * 3
        if tipo_cerveza == "Rubia Extranjera" and tipo_vaso == "Chopp":
            self.servir +=1
            self.litros += 0.75
            return 65 * 0.75
        if tipo_cerveza == "Rubia Extranjera" and tipo_vaso == "Vaso":
            self.servir +=1
            self.litros += 0.5
            return 65 * 0.5
        if tipo_cerveza == "Rubia Extranjera" and tipo_vaso == "Jarra":
            self.servir +=1
            self.litros += 3
            return 65 * 3
        else:
            raise ValueError("Tipo de cerveza o vaso no válido.")
        
        
    def ventas(self):
        venta = self.precio
        self.recaudacion += venta
        incremento = venta * 5 / 100
        venta += incremento
        return venta

    def obtener_recaudacion(self):
        return self.recaudacion
        
     
class After:
    def __init__(self):
        self.barriles = []
        
    def agregar_barril(self, barril_cerveza):
        self.barriles.append(barril_cerveza)
        
    def calcular_recaudacion_total(self):
        recaudacion_total = 0
        for barril_cerveza in self.barriles:
            recaudacion_total += barril_cerveza.obtener_recaudacion()
        return recaudacion_total
    
    def obtener_max_servir_barril(self):
        max_servir_barril = max(self.barriles, key=lambda barril_cerveza: barril_cerveza.servir)
        return max_servir_barril

    def obtener_min_servir_barril(self):
        min_servir_barril = min(self.barriles, key=lambda barril_cerveza: barril_cerveza.servir)
        return min_servir_barril
    
    def obtener_max_recaudar_barril(self):
        max_recaudar_barril = max(self.barriles, key=lambda barril_cerveza: barril_cerveza.obtener_recaudacion())
        return max_recaudar_barril.tipo_cerveza
    
    def obtener_max_cerveza_vendida(self):
        max_vender_cerveza = max(self.barriles, key=lambda barril_cerveza: barril_cerveza.servir)
        return max_vender_cerveza.tipo_cerveza
    
    def obtener_max_cerveza_ganancia(self):
        max_cerveza_ganancia = max(self.barriles, key=lambda barril_cerveza: barril_cerveza.obtener_recaudacion())
        return max_cerveza_ganancia.tipo_cerveza
    
    def obtener_max_litros_cerveza_vendida(self):
        max_litros_cerveza = max(self.barriles, key=lambda barril_cerveza: barril_cerveza.litros)
        return max_litros_cerveza.tipo_cerveza
    
    def obtener_min_litros_cerveza_vendida(self):
        min_litros_cerveza = min(self.barriles, key=lambda barril_cerveza: barril_cerveza.litros)
        return min_litros_cerveza.tipo_cerveza
    
    def obtener_max_vaso_solicitado(self):
        max_vaso_solicitado = max(self.barriles, key=lambda barril_cerveza: barril_cerveza.servir)
        return max_vaso_solicitado.tipo_vaso
    
    def calcular_porcentaje_venta_cerveza(self):
        total_cervezas = sum(barril.servir for barril in self.barriles)
        
        for barril in self.barriles:
            porcentaje_venta = round((barril.servir / total_cervezas) * 100, 2)
            
            print(f"\n Cerveza: {barril.tipo_cerveza}")
            print(f"Porcentaje de venta: {porcentaje_venta}%")
    
    def calcular_porcentaje_recaudacion_cerveza(self):
        recaudacion_tipo_cerveza = 0
        for barril in self.barriles:
            recaudacion_tipo_cerveza += barril.servir
            porcentaje_recaudacion_cerveza =  round((recaudacion_tipo_cerveza / sum(b.servir for b in self.barriles)) * 100, 2)
            
            print(f"\nCerveza: {barril.tipo_cerveza}")
            print(f"Porcentaje de recaudación: {porcentaje_recaudacion_cerveza}%")

            
    def calcular_porcentaje_venta_barril(self):
        for barril in self.barriles:
            porcentaje_venta_barril = round((barril.servir / sum(b.servir for b in self.barriles)) * 100, 2)
            
            print(f"\nBarril: {barril.tipo_cerveza}")
            print(f"Porcentaje de venta: {porcentaje_venta_barril}%")
            
        
    def calcular_porcentaje_recaudacion_barril(self):
         recaudacion_total = self.calcular_recaudacion_total()
         for barril in self.barriles:
            porcentaje_recaudacion_barril = round((barril.obtener_recaudacion() / recaudacion_total) * 100, 2)
            
            print(f"\nBarril: {barril.tipo_cerveza}")
            print(f"Porcentaje de recaudación: {porcentaje_recaudacion_barril}%")
         
         
after = After()

barril1 = Barril("Rubia Nacional", "Vaso")
barril2 = Barril("Negra Nacional", "Chopp")
barril3 = Barril("Rubia Extranjera", "Jarra")

after.agregar_barril(barril1)
after.agregar_barril(barril2)
after.agregar_barril(barril3)

barril1.ventas()
barril2.ventas()
barril3.ventas()

recaudacion_total = after.calcular_recaudacion_total()
barril_max_recaudacion = after.obtener_max_recaudar_barril()
cerveza_mas_vendida = after.obtener_max_cerveza_vendida()
cerveza_mas_ganancia = after.obtener_max_cerveza_ganancia()
cerveza_mas_litros = after.obtener_max_litros_cerveza_vendida()
cerveza_menos_litros = after.obtener_min_litros_cerveza_vendida()
vaso_mas_solicitado = after.obtener_max_vaso_solicitado()
min_servir_barril = after.obtener_min_servir_barril()
max_servir_barril = after.obtener_max_servir_barril()


# 1) Calcular la recaudación total del after.
print("Recaudación total: $", recaudacion_total)

# 2_a) Obtener el barril que más cerveza sirvió, y mostrar las cantidades.
print("\nBarril que más cerveza sirvió:")
print(f"Barril: {max_servir_barril.tipo_cerveza}")
print(f"Cantidad de veces que se sirvió: {max_servir_barril.servir}")

# 2_b) Obtener el barril que menos cerveza sirvió, y mostrar las cantidades. 
print("\nBarril que menos cerveza sirvió:")
print(f"Barril: {min_servir_barril.tipo_cerveza}")
print(f"Cantidad de veces que se sirvió: {min_servir_barril.servir}")

# 3) Obtener el barril que más dinero recaudó. 
print("El barril que mas dinero recaudó: ", barril_max_recaudacion)

# 4) Mostrar la cerveza más vendida. 
print("La cerveza mas vendida: ", cerveza_mas_vendida)

# 5) Mostrar la cerveza que generó más ganancia. 
print("La cerveza que mas ganacia generó: ", cerveza_mas_ganancia)

# 6) Obtener la cerveza que se vendió mayor cantidad de litros. 
print("La cerveza que se vendió mayor cantidad de litros: ", cerveza_mas_litros)

# 7) Obtener la cerveza que se vendió menor cantidad de litros. 
print("La cerveza que se vendió menor cantidad de litros: ", cerveza_menos_litros)

# 8) Obtener el tipo de vaso que más se solicitó. 
print("El vaso que más se solicitó: ", vaso_mas_solicitado)
 

