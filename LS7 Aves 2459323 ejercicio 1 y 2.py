#Nombre del curso y sección : Introduccion a la programacion lab seccion 17 
#Fecha de creación del programa: 19/09/2023 
#Autor: Alejandro Echegoyen 2459323
#Objetivo: Realizar operaciones aritméticas mediante de valores solicitados al usuario
while True:
    print("Ejercicio 1: Operaciones Aritméticas")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo")
    print("6. Exponenciación")
    print("7. Cociente")
    print("8. Salir")

    opcion = input("Seleccione una opción (1-8): ")

    if opcion == '8':
        print("¡Hasta luego!")
        break

    if opcion not in ['1', '2', '3', '4', '5', '6', '7']:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        continue

    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        resultado = numero1 + numero2
        operacion = "suma"
    elif opcion == '2':
        resultado = numero1 - numero2
        operacion = "resta"
    elif opcion == '3':
        resultado = numero1 * numero2
        operacion = "multiplicación"
    elif opcion == '4':
        if numero2 == 0:
            print("Error: No se puede dividir por cero.")
            continue
        resultado = numero1 / numero2
        operacion = "división"
    elif opcion == '5':
        resultado = numero1 % numero2
        operacion = "módulo"
    elif opcion == '6':
        resultado = numero1 ** numero2
        operacion = "exponenciación"
    elif opcion == '7':
        if numero2 == 0:
            print("Error: No se puede calcular el cociente con divisor cero.")
            continue
        resultado = numero1 // numero2
        operacion = "cociente"

    print(f"{numero1} {operacion} {numero2} = {resultado}")