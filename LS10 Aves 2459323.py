# Curso: Introduccion a la informatica Lab seccion 
# Sección: Seccion 7
# Fecha de creación: 10/10/2023
# Autor: Alejandro Echegoyen 
# Objetivo: Crear un programa que solicite al usuario un valor y ese valor realizar una conversion de cm a metros, kilometros, pulgadas y pies

# Modulo Conversor

def centimetros_a_metros(cms):
    return cms / 100

def centimetros_a_kilometros(cms):
    return cms / 100000

def centimetros_a_pulgadas(cms):
    return cms / 2.54

def centimetros_a_pies(cms):
    return cms / 30.48

# Programa principal

def main():
    

    while True:
        try:
            cantidad = float(input("\nIngrese la cantidad en centímetros: "))
            unidad = input("Seleccione la unidad a la que desea convertir (metros, kilometros, pulgadas, pies): ").lower()

            if unidad == "metros":
                resultado = centimetros_a_metros(cantidad)
                print(f"{cantidad} centímetros son {resultado} metros")
            elif unidad == "kilometros":
                resultado = centimetros_a_kilometros(cantidad)
                print(f"{cantidad} centímetros son {resultado} kilómetros")
            elif unidad == "pulgadas":
                resultado = centimetros_a_pulgadas(cantidad)
                print(f"{cantidad} centímetros son {resultado} pulgadas")
            elif unidad == "pies":
                resultado = centimetros_a_pies(cantidad)
                print(f"{cantidad} centímetros son {resultado} pies")
            else:
                print("Unidad no válida. Intente nuevamente.")

            continuar = input("¿Desea realizar otra conversión? (s/n): ").lower()
            if continuar != 's':
                break

        except ValueError:
            print("Entrada no válida. Ingrese un número válido.")

if __name__ == "__main__":
    main()
