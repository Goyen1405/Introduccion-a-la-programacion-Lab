#Nombre del curso y sección : Introduccion a la programacion lab seccion 17 
#Fecha de creación del programa: 12/09/2023 
#Autor: Alejandro Echegoyen 2459323
#Objetivo: Crear un programa en Python que indica el día de la semana correspondiente al número ingresado y maneja errores si el número está fuera del rango permitido
print("Ejercicio 2")

try:
    numero_dia = int(input("Ingrese el número de día: "))

    if numero_dia >= 1 and numero_dia <= 7:
        if numero_dia == 1:
            dia = "Lunes"
        elif numero_dia == 2:
            dia = "Martes"
        elif numero_dia == 3:
            dia = "Miércoles"
        elif numero_dia == 4:
            dia = "Jueves"
        elif numero_dia == 5:
            dia = "Viernes"
        elif numero_dia == 6:
            dia = "Sábado"
        elif numero_dia == 7:
            dia = "Domingo"
        
        print("DIA:", dia)
    else:
        print("Error. El número a ingresar debe estar contenido entre 1 y 7.")

except ValueError:
    print("Error. Debe ingresar un número entero válido.")
