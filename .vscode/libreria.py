# Una librería necesita un programa que le permita gestionar sus ventas de sus respectivos productos.
# De cada producto se registran las siguientes características:
# •	Código de Barras
# •	Nombre del producto
# •	Descripción
# •	Precio

# Desarrollar una aplicación Orientada a Objetos utilizando VB.Net o C# que permita:
# 1)	Recuperar bajo demanda la recaudación total de la librería. 
# 2)	Mostrar el subtotal de la venta.
# 3)    Controlar la carga de datos. 

class Producto:
    def __init__(self, codigo_barras, nombre, descripcion, precio, cantidad):
        self.codigo_barras = codigo_barras
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = float(precio)
        self.cantidad = int(cantidad)
       
cant = input("¿Cuantos productos desea ingresar?: ")
while cant.isdigit() != True:
    print("ERROR. El dato ingresado no es un número, o no es un número válido. Pruebe denuevo.")
    cant = input("¿Cuantos productos desea ingresar?: ") 
productos = []

for i in range (int(cant)):     
    print("\nProducto número:", i + 1)
    
    cod = input("\nCódigo de barras del producto: ")
    nom = input("Nombre del producto: ")
    desc = input("Descripcion del producto: ")
    
    pre = input("Precio del producto: ")
    while pre.isdigit() != True:
        print("ERROR. El dato ingresado no es un número, o no es un número válido. Pruebe denuevo.")
        pre = input("Precio del producto: ")
                      
    c = input("Cantidad del producto: ")
    while c.isdigit() != True:
        print("ERROR. El dato ingresado no es un número, o no es un número válido. Pruebe denuevo.")
        c = input("Cantidad del producto: ")
                         
    p = Producto(cod, nom, desc, pre, c)
    productos.append(p)


class Libreria:
    def __init__(self):
        self.productos = []
        self.subtotal = 0
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
        
    def calcular_subtotal(self):    
        for p in self.productos:
            self.subtotal += p.precio * p.cantidad
            
    def calcular_iva(self):
        self.iva = self.subtotal * 0.21
        
    def calcular_recaudacion(self):
        self.recaudacion = self.subtotal + self.iva
        
    # def calcular_total(self):
    #     for p in self.productos:
    #       self.subtotal += p.precio * p.cantidad
    #     self.iva = self.subtotal * 0.21                      
    #     self.recaudacion = self.subtotal + self.iva

libreria = Libreria()

for producto in productos:
    libreria.agregar_producto(producto)

libreria.calcular_subtotal()
libreria.calcular_iva()
libreria.calcular_recaudacion()

recaudacion = libreria.recaudacion
print("\nRecaudacion total de la libreria:", recaudacion)

subtotal = libreria.subtotal
print("Subtotal de la libreria:", subtotal)
