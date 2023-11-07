# Información del programa
#Curso: Introduccion a la informatica
#Sección: 17
#Fecha de creación: 07/11/2023
#Autor: Alejandro Echegoyen 2459323

class Automovil:
    def __init__(self):
        self.modelo = 0
        self.precio = 0.0
        self.marca = ""
        self.disponible = False
        self.tipoCambioDolar = 0.0
        self.descuentoAplicado = 0.0

    def DefinirModelo(self, unModelo):
        self.modelo = unModelo

    def DefinirPrecio(self, unPrecio):
        self.precio = unPrecio

    def DefinirMarca(self, unaMarca):
        self.marca = unaMarca

    def DefinirTipoCambio(self, unTipoCambio):
        self.tipoCambioDolar = unTipoCambio

    def CambiarDisponibilidad(self):
        self.disponible = not self.disponible

    def MostrarDisponibilidad(self):
        if self.disponible:
            return "Disponible"
        else:
            return "No se encuentra disponible actualmente"

    def MostrarInformacion(self):
        precio_dolares = self.precio / self.tipoCambioDolar
        return f"Marca: {self.marca}. Modelo: {self.modelo}. Precio de venta: Q{self.precio}. Precio en dólares: ${precio_dolares}. {self.MostrarDisponibilidad()}"

    def AplicarDescuento(self, miDescuento):
        self.descuentoAplicado = miDescuento
        precio_con_descuento = self.precio - self.descuentoAplicado
        self.DefinirPrecio(precio_con_descuento)


# Interacción con el usuario para ingresar datos
automovil = Automovil()
automovil.DefinirMarca(input("Ingrese la marca del automóvil: "))
automovil.DefinirModelo(input("Ingrese el modelo del automóvil: "))
automovil.DefinirPrecio(float(input("Ingrese el precio del automóvil en quetzales: ")))
automovil.DefinirTipoCambio(float(input("Ingrese el tipo de cambio actual: ")))

# Aplicar descuento
descuento = float(input("Ingrese el descuento a aplicar en quetzales: "))
automovil.AplicarDescuento(descuento)

# Cambiar disponibilidad
automovil.CambiarDisponibilidad()

# Mostrar información del automóvil
print(automovil.MostrarInformacion())
