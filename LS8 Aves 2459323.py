# Curso: Introduccion a la informatica Lab seccion 
# Sección: Seccion 7
# Fecha de creación: 26/09/2023
# Autor: Alejandro Echegoyen 
# Objetivo: Este programa muestra un menú de opciones al usuario para calcular el factorial o la secuencia de Fibonacci de un número ingresado.

# Función para calcular el factorial de un número
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

# Función para generar la secuencia de Fibonacci
def fibonacci(numero):
    if numero <= 0:
        return []
    elif numero == 1:
        return [0]
    elif numero == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < numero:
            next_num = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_num)
        return fib_sequence

# Bucle principal
while True:
    # Mostrar el menú
    print("Menu:")
    print("1. Factorial")
    print("2. Secuencia de Fibonacci")
    print("3. Salir")

    # Solicitar al usuario que ingrese una opción
    opcion = input("Ingrese el número de opción que desea ejecutar: ")

    # Verificar la opción ingresada
    if opcion == "1":
        # Calcular el factorial
        numero = int(input("Ingrese un número para calcular su factorial: "))
        resultado = factorial(numero)
        print(f"{numero}! = {resultado}")
    elif opcion == "2":
        # Generar la secuencia de Fibonacci
        numero = int(input("Ingrese un número para generar la secuencia de Fibonacci: "))
        fib_sequence = fibonacci(numero)
        print(", ".join(map(str, fib_sequence)), f"Fibonacci({numero})")
    elif opcion == "3":
        # Salir del programa
        print("¡Hasta luego!")
        break
    else:
        # Opción inválida
        print("Opción inválida. Por favor, ingrese una opción válida.")

# Fin del programa
