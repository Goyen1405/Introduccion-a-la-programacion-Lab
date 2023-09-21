#Nombre del curso y sección : Introduccion a la programacion lab seccion 17 
#Fecha de creación del programa: 19/09/2023 
#Autor: Alejandro Echegoyen 2459323
#Objetivo: Crear programa que mediante la seleccion de un numero entre 1 y 10 me pueda dar las tablas de multiplicacion 
# Imprime mi nombre completo
print("Mi nombre completo es Alejandro Vladimir Echegoyen Sequeira")

# Ciclo principal
while True:
    # Solicitar al usuario que ingrese un número en el rango de 1 a 10
    numero = int(input("Por favor, ingrese un número entre 1 y 10: "))
    
    # Verificar si el número está en el rango correcto
    if numero < 1 or numero > 10:
        print("El número ingresado no está en el rango correcto.")
    else:
        # Utilizar un ciclo for para mostrar la tabla de multiplicar
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} X {i} = {resultado}")
        
        # Preguntar al usuario si desea generar la tabla de otro número
        respuesta = input("¿Desea generar la tabla de otro número? (SALIR para salir): ")
        if respuesta.upper() == "SALIR":
            break
