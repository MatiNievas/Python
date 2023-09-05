# Una estación de servicio necesita un programa que le permita administrar sus ventas, 
# para ello cuenta con 3 surtidores, cada surtidor en su interior estará cargado con 1 tipo de nafta.

# Los tipos de naftas junto con sus tarifas por litro son:
# •	Normal: $17.20
# •	Súper: $18.85
# •	Premium: $21.30

# Desarrollar una aplicación Orientada a Objetos utilizando VB.Net o C# que permita:
# 1)	Obtener la recaudación total de la estación de servicio.
# 2)	Obtener la recaudación total de un surtidor.
# 3)	Obtener el surtidor que más recaudó.
# 4)	Obtener el surtidor que menos recaudó.
# 5)	Obtener el surtidor que más clientes tuvo.
# 6)	Calcular el porcentaje de venta de cada tipo de nafta.
# 7)	Calcular el porcentaje de recaudación de cada tipo de nafta.
# 8)	Recargar el surtidor cuando éste haya quedado vacío.
# 9)	Mostrar el surtidor con mayor cantidad recargas.
# 10)	Calcular el promedio de ventas por surtidor.
# 11)	Calcular el promedio de recaudación por surtidor.
   
        
class Surtidor:
    def __init__ (self,tipo_nafta=None, precio_nafta=None):
        self.tipo_nafta = tipo_nafta
        self.precio_nafta = precio_nafta
        self.recargas = 0
        self.clientes = 0
        self.recaudacion = 0
    
        
    def ventas(self, litros):
        venta = self.precio_nafta * litros
        self.recaudacion += venta
        self.clientes += 1
        return venta
    
    def obtener_clientes(self):
        return self.clientes
        
    def obtener_recaudacion(self):
        return self.recaudacion
    
    def recargar(self):
        self.recargas += 1
        
class EstacionDeServicio:
    def __init__ (self):
        self.surtidores = []
        
    def agregar_surtidor(self, surtidor):
        self.surtidores.append(surtidor)
        
    def calcular_recaudacion_total(self):
        recaudacion_total = 0
        for surtidor in self.surtidores:
            recaudacion_total += surtidor.obtener_recaudacion()
        return recaudacion_total
    
    def obtener_recaudacion_surtidor(self, surtidor):
        for s in self.surtidores:
            if s.tipo_nafta == surtidor:
                return s.obtener_recaudacion()
        return 0
            
    def obtener_max_surtidor(self):
        # surtidor_max = False
        # max_recaudacion = 0
        # for surtidor in self.surtidores:
        #     if surtidor.obtener_recaudacion() > max_recaudacion:
        #         max_recaudacion = surtidor.obtener_recaudacion()
        #         surtidor_max = surtidor.tipo_nafta
        # return surtidor_max
        max_surtidor = max(self.surtidores, key= lambda surtidor: surtidor.obtener_recaudacion())
        max_surtidor = max_surtidor.tipo_nafta
        return max_surtidor
    
    def obtener_min_surtidor(self):
        # surtidor_min = Surtidor()
        # min_recaudacion = 0
        # for surtidor in self.surtidores:
        #     if surtidor_min is not None or surtidor.obtener_recaudacion() < min_recaudacion:
        #         surtidor_min = surtidor.obtener_recaudacion()
        #         surtidor_min = surtidor.tipo_nafta
        # return surtidor_min
        min_surtidor = min(self.surtidores, key=lambda surtidor: surtidor.obtener_recaudacion())
        min_surtidor = min_surtidor.tipo_nafta
        return min_surtidor


    
    def obtener_max_clientes(self):
        #  surtidor_max_clientes =  Surtidor()
        #  clientes_max = 0
        #  for surtidor in self.surtidores:
        #      if surtidor_max_clientes is not None or surtidor.obtener_clientes() > clientes_max:
        #          clientes_max = surtidor.obtener_clientes()
        #          surtidor_max_clientes = surtidor.tipo_nafta
        #  return surtidor_max_clientes
        max_clientes = max(self.surtidores, key= lambda surtidor: surtidor.obtener_clientes())
        max_clientes = max_clientes.tipo_nafta
        return max_clientes
        
    
    
    def calcular_porcentaje_venta_nafta(self, tipo_nafta):
        total_litros_vendidos = 0
        for surtidor in self.surtidores:
            if surtidor.tipo_nafta == tipo_nafta:
                total_litros_vendidos += surtidor.obtener_clientes()
        porcentaje = total_litros_vendidos / sum([s.obtener_clientes() for s in self.surtidores])
        porcentaje_venta = porcentaje * 100
        return porcentaje_venta
    
    def calcular_porcentaje_recaudacion_nafta(self, tipo_nafta):
        recaudacion_tipo_nafta = 0
        for surtidor in self.surtidores:
            if surtidor.tipo_nafta == tipo_nafta:
                recaudacion_tipo_nafta += surtidor.obtener_recaudacion()
        porcentaje_recaudacion = (recaudacion_tipo_nafta / self.calcular_recaudacion_total()) * 100
        return porcentaje_recaudacion
    
    def recargar_surtidor(self):
        # surtidor_vacio = False
        # max_recargas = 0
        # for surtidor in self.surtidores:
        #     if surtidor.obtener_clientes() == 0:
        #         if surtidor.recargas > max_recargas:
        #             max_recargas = surtidor.recargas
        #             surtidor_vacio = surtidor.tipo_nafta
        # return surtidor_vacio
        max_recargas = max(self.surtidores, key= lambda surtidor: surtidor.recargas)
        max_recargas = max_recargas.tipo_nafta
        return max_recargas
        
    
    def calcular_promedio_ventas(self):
        total_ventas = sum([s.obtener_clientes() for s in self.surtidores])
        promedio = total_ventas / len(self.surtidores)
        return promedio

    def calcular_promedio_recaudacion(self):
        total_recaudacion = self.calcular_recaudacion_total()
        promedio = total_recaudacion / len(self.surtidores)
        return promedio
                
                
                
# Crear surtidores y estación de servicio
surtidor1 = Surtidor("Normal", 17.20)
surtidor2 = Surtidor("Super", 18.85)
surtidor3 = Surtidor("Premium", 21.30)

estacion = EstacionDeServicio()

# Agregar surtidores a la estación de servicio
estacion.agregar_surtidor(surtidor1)
estacion.agregar_surtidor(surtidor2)
estacion.agregar_surtidor(surtidor3)

# Vender nafta en los surtidores
surtidor1.ventas(100)
surtidor2.ventas(300)  
surtidor3.ventas(700)  

# 1) Obtener la recaudacion total de la estacion de servicio
recaudacion_total = estacion.calcular_recaudacion_total()
print("Recaudacion total de la estacion de servicio:", recaudacion_total)

# 2) Obtener la recaudacion total de un surtidor
recaudacion_surtidor = estacion.obtener_recaudacion_surtidor("Normal")
print("Recaudacion del surtidor Normal:", recaudacion_surtidor)

# 3) Obtener el surtidor que más recaudo
surtidor_max_recaudacion = estacion.obtener_max_surtidor()
print("Surtidor que más recaudo:", surtidor_max_recaudacion)

# 4) Obtener el surtidor que menos recaudo
surtidor_min_recaudacion = estacion.obtener_min_surtidor()
print("Surtidor que menos recaudo:", surtidor_min_recaudacion)

# 5) Obtener el surtidor que más clientes tuvo
surtidor_max_clientes = estacion.obtener_max_clientes()
print("Surtidor que mas clientes tuvo:", surtidor_max_clientes)

# 6) Calcular el porcentaje de venta de cada tipo de nafta
porcentaje_venta_normal = estacion.calcular_porcentaje_venta_nafta("Normal")
porcentaje_venta_super = estacion.calcular_porcentaje_venta_nafta("Super")
porcentaje_venta_premium = estacion.calcular_porcentaje_venta_nafta("Premium")
print("Porcentaje de venta de nafta Normal:", porcentaje_venta_normal, "%")
print("Porcentaje de venta de nafta Super:", porcentaje_venta_super, "%")
print("Porcentaje de venta de nafta Premium:", porcentaje_venta_premium, "%")

# 7) Calcular el porcentaje de recaudación de cada tipo de nafta
porcentaje_recaudacion_normal = estacion.calcular_porcentaje_recaudacion_nafta("Normal")
porcentaje_recaudacion_super = estacion.calcular_porcentaje_recaudacion_nafta("Súper")
porcentaje_recaudacion_premium = estacion.calcular_porcentaje_recaudacion_nafta("Premium")
print("Porcentaje de recaudación de nafta Normal:", porcentaje_recaudacion_normal, "%")
print("Porcentaje de recaudación de nafta Súper:", porcentaje_recaudacion_super, "%")
print("Porcentaje de recaudación de nafta Premium:", porcentaje_recaudacion_premium, "%")

# 8) Recargar el surtidor cuando esté vacio
surtidor1.recargar()

# 9) Mostrar el surtidor con mayor cantidad de recargas
surtidor_max_recargas = estacion.recargar_surtidor()
print("Surtidor con mayor cantidad de recargas:", surtidor_max_recargas)

# 10) Calcular el promedio de ventas por surtidor
promedio_ventas = estacion.calcular_promedio_ventas()
print("Promedio de ventas por surtidor:", promedio_ventas)

# 11) Calcular el promedio de recaudacion por surtidor
promedio_recaudacion = estacion.calcular_promedio_recaudacion()
print("Promedio de recaudacion por surtidor:", promedio_recaudacion)