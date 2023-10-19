#Nombre del curso y sección : Introduccion a la programacion lab seccion 17 Trabajo supervisado
#Fecha de creación del programa: 19/10/2023 
#Autor: Alejandro Echegoyen 2459323
# Solicitar una palabra al usuario y mostrar las primeras 3 letras
palabra = input("Ingrese una palabra: ")
primeras_tres_letras = palabra[:3]
print("Las primeras tres letras son:", primeras_tres_letras)

# Almacenar las primeras tres letras en una nueva variable y mostrarla
nueva_subcadena = primeras_tres_letras
print("La nueva subcadena formada por las primeras tres letras es:", nueva_subcadena)

# Solicitar un nuevo texto al usuario y reemplazar las vocales "O" por "X"
nuevo_texto = input("Ingrese un nuevo texto: ")
texto_modificado = ""

for letra in nuevo_texto:
    if letra.lower() == "o":
        texto_modificado += "X"
    else:
        texto_modificado += letra

# Mostrar el nuevo texto formado
print("El nuevo texto con las vocales 'O' reemplazadas por 'X' es:")
print(texto_modificado)

