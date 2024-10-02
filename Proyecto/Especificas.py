from Package_Input.Input import get_int
numeros = [0] * 10

def pedir_10_numeros():
    """Función para pedir el ingreso de 10 números enteros entre -1000 y 1000."""
    for i in range(10):
        numeros[i] = get_int("Ingrese un número: ","Reingrese el número: ",-1000,1000,3)
        
def mostrar_cantidad_positivos_negativos(lista:list)->int:
    """Función para mostrar la cantidad de numeros positivos y negativos de la lista.

    Args:
        lista (list): Lista de números ingresados por consola.
        
    """    
    contador_positivos = 0
    contador_negativos = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            contador_positivos += 1
        else:
            contador_negativos += 1
    print(f"La cantidad de positivos es {contador_positivos} y la cantidad de negativos {contador_negativos}")
    
def sumar_pares(lista:list)->int:
    """Función para sumar los números pares de la lista.

    Args:
        lista (list): Lista de números ingresados por consola.

    Returns:
        int: Resultado de la suma de los pares.
        
    """    
    suma = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            suma += lista[i]
    return suma

def mostrar_mayor_impar(lista:list)->int:
    """Función para mostrar el impar mayor de la lista.

    Args:
        lista (list): Lista de números ingresados por consola.

    Returns:
        int: El impar mayor de la lista
        
    """    
    bandera_mayor = True
    maximo = 0
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            if lista[i] > maximo or bandera_mayor == True:
                maximo = lista[i]
                bandera_mayor = False
    return maximo

def lista_pares(lista:list)->int:
    """Función para mostrar unicamente números los pares de la lista.

    Args:
        lista (list): Lista de números ingresados por consola.

    """
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            print(lista[i])


def lista_posiciones_impares(lista:list):
    """Función  para mostrar las posiciones de los números impares de la lista.

    Args:
        lista (list): Lista de números ingresados por consola.
        
    """    
    for i in range(len(lista)):
            if lista[i] % 2 != 0:
                print(f"Posición {i+1}: {lista[i]}")