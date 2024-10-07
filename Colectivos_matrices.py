"""1. Cargar planilla.
El chofer se debe identificar (el legajo debe existir dentro de una matriz de legajos). 
Si el chofer existe cargará la recaudación del viaje indicando línea y coche
(no necesariamente un chofer está asignado a una única línea y coche), estos datos deben estar validados. 
Un chofer puede cargar más de una recaudación por día (para distintas líneas y distintos coches).
Cada coche de cada línea puede tener varias recaudaciones diarias.

2. Mostrar la recaudación de cada coche y línea (mostrar la matriz).
3. Calcular y mostrar recaudación por línea.
4. Calcular y mostrar recaudación por coche.
5. Calcular y mostrar la recaudación total.
6. Salir.
"""
from os import system
import random

def crear_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any)->list:
    """Función para crear una matriz con un tamaño específico y un valor inicial.

    Args:
        cantidad_filas (int): Número de fila que tendrá la matriz (cantidad de líneas de colectivo).
        cantidad_columnas (int): Número de columnas que tendrá la matriz (cantidad de coches).
        valor_inicial (any): Valor con el que se inicializará la matriz.

    Returns:
        list: La matriz creada con los valores dados.
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz:list)->None:
    """Función para mostrar la matriz

    Args:
        matriz (list): Matriz creada.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j],end=" ")
        print()

def crear_lista(limite:int,valor:any)->list:
    """Función para crear una lista.

    Args:
        limite (int): Indica la longitud que tendrá la lista.
        valor (any): Valor inicial para completar la lista

    Returns:
        list: Lista creada con valores aleatorios.
    """
    lista_legajos = [valor] * limite
    for i in range(len(lista_legajos)):
        lista_legajos [i] = random.randint(1000,5000)
    return lista_legajos


def cargar_planilla(lista_matriz: list, legajos_choferes:list)->None:
    """Función para cargar una recaudación a partir de la validación del legajo, número de línea y coche.

    Args:
        lista_matriz (list): Matriz creada, donde se guardarán las recaudaciones
        legajos_choferes (list): Lista con los legajos de los choferes.
    """
    while True:
        num_legajo = int(input("Ingrese número de legajo: "))
        legajo_existe = False
        for i in range(len(legajos_choferes)):
            if num_legajo == legajos_choferes[i]:
                legajo_existe = True
                
        if legajo_existe:
            break
        else:
            print("Este legajo no existe, reingrese")
            
    while True:    
        num_linea = int(input("Ingrese el número de línea: "))
        if 0 <= num_linea < len(lista_matriz):
            break
        else:
            print("No valido")
    
    while True:
        num_coche = int(input("Ingresa número de coche: "))
        if 0 <= num_coche < len(lista_matriz[0]):
            break    
        else: 
            print("no valido")
            
    while True:
        recaudacion = float((input("Ingrese monto de la recaudación: $")))
        if recaudacion >= 0:
            break
        else:
            print("Monto inválido")
        
    lista_matriz[num_linea][num_coche] += recaudacion
    

def mostrar_recaudacion_linea(lista_matriz:list)->None:
    """Función para mostrar recaudación total por línea.

    Args:
        lista_matriz (list): Matriz con las recaudaciones.
    """
    for i in range(len(lista_matriz)):
        recaudación_por_linea = 0
        for j in range(len(lista_matriz[i])):
            recaudación_por_linea += lista_matriz [i][j]
    
        print(f"Linea {i}: ${recaudación_por_linea:.2f}")
            
def mostrar_recaudacion_coche(lista_matriz:list)->None:
    """Función para mostrar recaudación total por coche.

    Args:
        lista_matriz (list): Matriz con las recaudaciones.
    """
    for j in range(len(lista_matriz[0])):
        recaudacion_por_coche = 0
        for i in range(len(lista_matriz)):
            recaudacion_por_coche += lista_matriz [i][j]
        
        print(f"Coche {j}: ${recaudacion_por_coche:.2f}")
    
def mostrar_recaudacion_total(lista_matriz:list)->int:
    """Función para mostrar la recaudación total de toda la matriz.

    Args:
        lista_matriz (list): Matriz con las recaudaciones.

    Returns:
        int: _description_
    """
    recaudacion_total = 0
    for i in range(len(lista_matriz)):
        for j in range(len(lista_matriz[i])):
            recaudacion_total += lista_matriz [i][j]
    return recaudacion_total

matriz = crear_matriz(3,5,0)
legajos = crear_lista(15,0)
print (legajos)
bandera = True

while bandera: 
    opcion = input("""1. Cargar planilla.
2. Mostrar la recaudación de cada coche y línea.
3. Mostrar recaudación por línea.
4. Mostrar recaudación por coche.
5. Mostrar la recaudación total.
6. Salir.\nElija una opción: """)
    match opcion:
        case "1":
            print("-"*20)
            cargar_planilla(matriz,legajos)
            print("-"*20)
        case "2":
            print("-"*20)
            mostrar_matriz(matriz)
            print("-"*20)
        case "3":
            print("-"*20)
            mostrar_recaudacion_linea(matriz)
            print("-"*20)
        case "4":
            print("-"*20)
            mostrar_recaudacion_coche(matriz)
            print("-"*20)
        case "5":
            print("-"*20)
            recaudacion = mostrar_recaudacion_total(matriz)
            print(f"Recaudacion total: {recaudacion}")
            print("-"*20)
        case "6":
            print("-"*20)
            print("Saliendo del menu...")
            bandera = False
        case _:
            print("Opción no válida")

system("pause")
system("cls")