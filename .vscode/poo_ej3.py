# Una cafetería cuenta con varias de máquinas de preparar café. 

# Cada máquina puede hacer 1 solo tipo de café. Los tipos de café con sus precios por litro son: 
# Arábigo $50.
# Robusto: $58. 

# El café se puede servir en diferentes vasos: 
# Vaso Chico: 50 cm3 = 0,05 litros
# Vaso Mediano: 100 cm3  = 0,1 litros
# Vaso Grande ¼ litro. = 0,25 litros


# Desarrollar una aplicación orientada a objetos utilizando VB.Net o C# que permita: 
# 1) Obtener la recaudación total del negocio.
# 2) Obtener la recaudación por máquina de café.
# 3) Mostrar la máquina que más café sirvió. 
# 4) Mostrar la máquina que menos café sirvió. 
# 5) Mostrar la máquina que más dinero recaudó. 
# 6) Mostrar la máquina que menos dinero recaudó. 
# 7) Mostrar el café que más veces se sirvió 
# 8) Mostrar el café que menos veces se sirvió. 
# 9) Mostrar el café que dejó mayor recaudación.
# 10) Mostrar el café que menos recaudación dejó. 
# 11) Mostrar el porcentaje de venta y recaudación de cada café. 
# 12) Mostrar el porcentaje de venta y recaudación de cada máquina. 
# 13) Informar y recargar cada vez que una máquina se encuentre vacía. 
# 14) Mostrar la máquina que mayor cantidad de veces se recargó.


class MaquinaCafe:
    def __init__(self, tipo_cafe=None, tamano_vaso=None):
        self.tipo_cafe = tipo_cafe
        self.tamano_vaso = tamano_vaso
        self.servir = 0
        self.precio = self.obtener_precio(tipo_cafe, tamano_vaso)
        self.recargas = 0
        self.recaudacion = 0
        
    def obtener_precio(self, tipo_cafe, tamano_vaso):
        if tipo_cafe == "Robusto" and tamano_vaso == "Chico":
            self.servir += 1
            return 58 * 0.05
        elif tipo_cafe == "Robusto" and tamano_vaso == "Mediano":
            self.servir += 1
            return 58 * 0.1
        elif tipo_cafe == "Robusto" and tamano_vaso == "Grande":
            self.servir += 1
            return 58 * 0.25
        elif tipo_cafe == "Arabigo" and tamano_vaso == "Chico":
            self.servir += 1
            return 50 * 0.05
        elif tipo_cafe == "Arabigo" and tamano_vaso == "Mediano":
            self.servir += 1
            return 50 * 0.1
        elif tipo_cafe == "Arabigo" and tamano_vaso == "Grande":
            self.servir += 1
            return 50 * 0.25
        else:
            raise ValueError("Tipo de café o tamaño de vaso no válido.")

    def ventas(self, cantidad_litros):
        venta = self.precio * cantidad_litros
        self.recaudacion += venta
        return venta

    def obtener_recaudacion(self):
        return self.recaudacion

    def recargar(self):
        self.recargas += 1


class Cafeteria:
    def __init__(self):
        self.maquinas = []

    def agregar_maquina(self, maquina_cafe):
        self.maquinas.append(maquina_cafe)

    def calcular_recaudacion_total(self):
        recaudacion_total = 0
        for maquina_cafe in self.maquinas:
            recaudacion_total += maquina_cafe.obtener_recaudacion()
        return recaudacion_total

    def obtener_recaudacion_maquina(self, maquina):
        for m in self.maquinas:
            if m.tipo_cafe == maquina:
                return m.obtener_recaudacion()
        return 0

    def obtener_max_servir_maquina(self):
        max_servir_maquina = max(self.maquinas, key=lambda maquina_cafe: maquina_cafe.servir)
        return max_servir_maquina.tipo_cafe

    def obtener_min_servir_maquina(self):
        min_servir_maquina = min(self.maquinas, key=lambda maquina_cafe: maquina_cafe.servir)
        return min_servir_maquina.tipo_cafe

    def obtener_max_recaudar_maquina(self):
        max_recaudar_maquina = max(self.maquinas, key=lambda maquina_cafe: maquina_cafe.obtener_recaudacion())
        return max_recaudar_maquina.tipo_cafe

    def obtener_min_recaudar_maquina(self):
        min_recaudar_maquina = min(self.maquinas, key=lambda maquina_cafe: maquina_cafe.obtener_recaudacion())
        return min_recaudar_maquina.tipo_cafe

    def obtener_max_cafe_servir(self):
        max_servir_cafe = max(self.maquinas, key=lambda maquina_cafe: maquina_cafe.servir)
        return max_servir_cafe.tipo_cafe

    def obtener_min_cafe_servir(self):
        min_servir_cafe = min(self.maquinas, key=lambda maquina_cafe: maquina_cafe.servir)
        return min_servir_cafe.tipo_cafe

    def obtener_max_cafe_recaudar(self):
        max_cafe_recaudar = max(self.maquinas, key=lambda maquina_cafe: maquina_cafe.obtener_recaudacion())
        return max_cafe_recaudar.tipo_cafe

    def obtener_min_cafe_recaudar(self):
        min_cafe_recaudar = min(self.maquinas, key=lambda maquina_cafe: maquina_cafe.obtener_recaudacion())
        return min_cafe_recaudar.tipo_cafe

    def mostrar_porcentaje_venta_recaudacion_cafe(self):
        total_cafes = sum(maquina.servir for maquina in self.maquinas)
        for maquina in self.maquinas:
            porcentaje_venta = round((maquina.servir / total_cafes) * 100, 2)
            porcentaje_recaudacion = round((maquina.obtener_recaudacion() / self.calcular_recaudacion_total()) * 100, 2)
            print(f"\n Máquina: {maquina.tipo_cafe}")
            print(f"Porcentaje de venta: {porcentaje_venta}%")
            print(f"Porcentaje de recaudación: {porcentaje_recaudacion}%")

    def mostrar_porcentaje_venta_recaudacion_maquina(self):
        recaudacion_total = self.calcular_recaudacion_total()
        for maquina in self.maquinas:
            porcentaje_venta = round((maquina.servir / sum(m.servir for m in self.maquinas)) * 100, 2)
            porcentaje_recaudacion = round((maquina.obtener_recaudacion() / recaudacion_total) * 100, 2)
            print(f"\n Máquina: {maquina.tipo_cafe}")
            print(f"Porcentaje de venta: {porcentaje_venta}%")
            print(f"Porcentaje de recaudación: {porcentaje_recaudacion}%")


    def informar_recargar_maquinas_vacias(self):
        for maquina in self.maquinas:
            if maquina.servir == 0:
                print(f"La máquina de café {maquina.tipo_cafe} se encuentra vacía. Se procederá a recargarla.")
                maquina.recargar()

    def obtener_maquina_mas_recargada(self):
        max_recargas = max(maquina.recargas for maquina in self.maquinas)
        maquina_mas_recargada = next((maquina.tipo_cafe for maquina in self.maquinas if maquina.recargas == max_recargas), None)
        return maquina_mas_recargada


cafeteria = Cafeteria()

maquina1 = MaquinaCafe("Robusto", "Chico")
maquina2 = MaquinaCafe("Arabigo", "Grande")
maquina3 = MaquinaCafe("Robusto", "Mediano")

cafeteria.agregar_maquina(maquina1)
cafeteria.agregar_maquina(maquina2)
cafeteria.agregar_maquina(maquina3)


maquina1.ventas(2)
maquina2.ventas(3)
maquina3.ventas(1)

recaudacion_total = cafeteria.calcular_recaudacion_total()
recaudacion_maquina1 = cafeteria.obtener_recaudacion_maquina("Robusto")
max_servir_maquina = cafeteria.obtener_max_servir_maquina()
min_servir_maquina = cafeteria.obtener_min_servir_maquina()
max_recaudar_maquina = cafeteria.obtener_max_recaudar_maquina()
min_recaudar_maquina = cafeteria.obtener_min_recaudar_maquina()
max_cafe_servir = cafeteria.obtener_max_cafe_servir()
min_cafe_servir = cafeteria.obtener_min_cafe_servir()
max_cafe_recaudar = cafeteria.obtener_max_cafe_recaudar()
min_cafe_recaudar = cafeteria.obtener_min_cafe_recaudar()
maquinas_mas_recargadas = cafeteria.obtener_maquina_mas_recargada()

# Imprimir las Respuestas

# 1) Obtener la recaudación total del negocio.
print("Recaudación total: $", recaudacion_total)
# 2) Obtener la recaudación por máquina de café.
print("Recaudación máquina 1 (Robusto): $", recaudacion_maquina1)
# 3) Mostrar la máquina que más café sirvió.
print("Máquina con mayor cantidad de cafés servidos:", max_servir_maquina)
# 4) Mostrar la máquina que menos café sirvió. 
print("Máquina con menor cantidad de cafés servidos:", min_servir_maquina)
# 5) Mostrar la máquina que más dinero recaudó. 
print("Máquina con mayor recaudación:", max_recaudar_maquina)
# 6) Mostrar la máquina que menos dinero recaudó. 
print("Máquina con menor recaudación:", min_recaudar_maquina)
# 7) Mostrar el café que más veces se sirvió 
print("Café más servido:", max_cafe_servir)
# 8) Mostrar el café que menos veces se sirvió. 
print("Café menos servido:", min_cafe_servir)
# 9) Mostrar el café que dejó mayor recaudación.
print("Café con mayor recaudación:", max_cafe_recaudar)
# 10) Mostrar el café que menos recaudación dejó. 
print("Café con menor recaudación:", min_cafe_recaudar)
# 11) Mostrar el porcentaje de venta y recaudación de cada café.
cafeteria.mostrar_porcentaje_venta_recaudacion_cafe()
# 12) Mostrar el porcentaje de venta y recaudación de cada máquina. 
cafeteria.mostrar_porcentaje_venta_recaudacion_maquina()
# 13) Informar y recargar cada vez que una máquina se encuentre vacía. 
cafeteria.informar_recargar_maquinas_vacias()
# 14) Mostrar la máquina que mayor cantidad de veces se recargó.
print("Máquina(s) con mayor cantidad de recargas:", maquinas_mas_recargadas)










