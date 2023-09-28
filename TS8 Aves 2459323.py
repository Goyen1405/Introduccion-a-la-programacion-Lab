#Nombre del curso y sección : Introduccion a la programacion lab seccion 17 Trabajo supervisado
#Fecha de creación del programa: 29/09/2023 
#Autor: Alejandro Echegoyen 2459323
#Objetivo: Realizar diferentes ejercicios con for y con while 
#Utilizando FOR para mostrar la secuencia de números de 1 a 25:
for i in range(1, 26):
    print(i, end=", ")
#Utilizando WHILE para mostrar la secuencia de números de 1 a 25:
num = 1
while num <= 25:
    print(num, end=", ")
    num += 1
#Utilizando FOR para mostrar la secuencia de números de 5 a 50 con incrementos de 5:
for i in range(5, 51, 5):
    print(i, end=", ")
#Utilizando WHILE para mostrar la secuencia de números de 5 a 50 con incrementos de 5:
num = 5
while num <= 50:
    print(num, end=", ")
    num += 5
#Utilizando FOR para mostrar la secuencia de números de 20 a 0 con decrementos de 2:
for i in range(20, -1, -2):
    print(i, end=", ")
#Utilizando WHILE para mostrar la secuencia de números de 20 a 0 con decrementos de 2:
num = 20
while num >= 0:
    print(num, end=", ")
    num -= 2
