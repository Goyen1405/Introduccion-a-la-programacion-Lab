#Nombre del curso y sección : Introduccion a la programacion lab seccion 17 
#Fecha de creación del programa: 19/09/2023 
#Autor: Alejandro Echegoyen 2459323
#Objetivo: Realizar operaciones aritméticas mediante de valores solicitados al usuario
import math

while True:
    print("Ejercicio 3: Jerarquía de Operaciones")
    print("1. a + b + c")
    print("2. a + (b + c)")
    print("3. a / b * c")
    print("4. Calcular expresión cuadrática")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == '5':
        print("¡Hasta luego!")
        break

    if opcion not in ['1', '2', '3', '4']:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        continue

    a = float(input("Ingrese el valor de 'a': "))
    b = float(input("Ingrese el valor de 'b': "))
    c = float(input("Ingrese el valor de 'c': "))

    if opcion == '1':
        resultado = a + b + c
        operacion = "a + b + c"
    elif opcion == '2':
        resultado = a + (b + c)
        operacion = "a + (b + c)"
    elif opcion == '3':
        if b == 0:
            print("Error: El divisor (b) no puede ser cero.")
            continue
        resultado = a / b * c
        operacion = "a / b * c"
    elif opcion == '4':
        discriminante = b ** 2 - 4 * a * c
        if a == 0 or discriminante < 0:
            print("Error: No se puede calcular la expresión cuadrática con los valores ingresados.")
            continue
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        resultado = f"x1 = {x1}, x2 = {x2}"
        operacion = "Expresión Cuadrática"

    print(f"Resultado de '{operacion}': {resultado}")
