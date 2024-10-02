from os import system

from Package_Arrays.Especificas import *
from Package_Arrays.Generales_array import *

bandera = True
bandera_numeros_ingresados = False

while bandera:
    opcion = input("""Bienvenido al Menú!!!
a. Pedir el ingreso de 10 números enteros entre -1000 y 1000.
b. Mostrar la cantidad de números positivos y negativos.
c. Mostrar la sumatoria de los números pares.
d. Informar el mayor de los números impares.
e. Listar todos los números ingresados.
f. Listar todos los números pares.
g. Listar los números de las posiciones impares.
h. Salir.
Elija una opcion:  """)
    match opcion:
        case "a":
            print("-"*50)
            pedir_10_numeros()
            bandera_numeros_ingresados = True
            print("-"*50)
        case "b":
            print("-"*50)
            if bandera_numeros_ingresados:     
                mostrar_cantidad_positivos_negativos(numeros)
            else:
                print("Debe ingresar los numeros (opcion 'a')")
            print("-"*50)
        case "c":
            print("-"*50)
            if bandera_numeros_ingresados:
                sumatoria_pares = sumar_pares(numeros)
                print(f"La suma de los pares es {sumatoria_pares}")
            else: 
                print("Debe ingresar los numeros (opcion 'a')")
            print("-"*50)
        case "d":
            print("-"*50)
            if bandera_numeros_ingresados:
                mayor_impar = mostrar_mayor_impar(numeros)
                print(f"El mayor de los impares es {mayor_impar}")
            else:
                print("Debe ingresar los numeros (opcion 'a')")
            print("-"*50)
        case "e":
            print("-"*50)
            if bandera_numeros_ingresados:
                mostrar_lista(numeros)
            else:
                print("Debe ingresar los numeros (opcion 'a')")
            print("-"*50)
        case "f":
            print("-"*50)
            if bandera_numeros_ingresados:
                lista_pares(numeros)
            else:
                print("Debe ingresar los numeros (opcion 'a')")
            print("-"*50)
        case "g":
            print("-"*50)
            if bandera_numeros_ingresados:
                lista_posiciones_impares(numeros)
            else:
                print("Debe ingresar los numeros (opcion 'a')")
            print("-"*50)
        case "h":
            print("-"*50)
            print("Saliendoo")
            bandera = False
        case _:
            print("Invalido, no está en el menú")
    
            
system("pause")
system("cls")




