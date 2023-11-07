# Información del programa
#Curso: Introduccion a la informatica
#Sección: 17
#Fecha de creación: 31/10/2023
#Autor: Alejandro Echegoyen 2459323
#Objetivo: Crear una clase para gestionar información personal con los atributos y métodos especificados.
#Entrada: Nombres, apellidos, apellido de casada, fecha de nacimiento.
#Procesos principales: Insertar nombres, apellidos, apellido de casada, fecha de nacimiento. 
#Obtener nombres, apellidos, fecha de nacimiento, nombre completo, edad.
#Salida: Información personal y edad.


# Definición de la clase
class Persona:
    def __init__(self):
        self.nombres = ""
        self.apellidos = ""
        self.apellido_casada = ""
        self.fecha_nacimiento = ""

    def insertar_nombres(self, nombres):
        self.nombres = nombres

    def insertar_apellidos(self, apellidos):
        self.apellidos = apellidos

    def insertar_apellido_casada(self, apellido_casada):
        self.apellido_casada = apellido_casada

    def insertar_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def obtener_nombres(self):
        return self.nombres

    def obtener_apellidos(self):
        if self.apellido_casada:
            return f"{self.apellidos} de {self.apellido_casada}"
        else:
            return self.apellidos

    def obtener_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def obtener_nombre_completo(self):
        return f"{self.nombres} {self.obtener_apellidos()}"

    def obtener_edad(self):
        # Cálculo de la edad (suponiendo que la fecha de nacimiento esté en el formato YYYY-MM-DD)
        import datetime
        fecha_nacimiento = datetime.datetime.strptime(self.fecha_nacimiento, "%Y-%m-%d").date()
        hoy = datetime.date.today()
        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        return edad

# Ejemplo de uso de la clase
if __name__ == "__main__":
    persona = Persona()
    persona.insertar_nombres("Juan")
    persona.insertar_apellidos("Pérez")
    persona.insertar_apellido_casada("Gómez")
    persona.insertar_fecha_nacimiento("1985-05-15")

    print("Nombre completo:", persona.obtener_nombre_completo())
    print("Fecha de nacimiento:", persona.obtener_fecha_nacimiento())
    print("Edad:", persona.obtener_edad())
