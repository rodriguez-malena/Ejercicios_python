
from .Validate import*

def get_int(mensaje:str, mensaje_error: str, minimo: int, maximo: int, reintentos:int) -> int|None:
    """Pedir un número por consola
    Args:
        mensaje(str): mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
        mensaje_error(str): mensaje de error en el caso de que el dato ingresado sea invalido.
        minimo(int): valor minimo admitido.
        maximo(int): valor maximo admitido.
        reintentos(int): cantidad de veces que se pide el dato en caso de error.
        
    Returns:
    int | None: retorna un entero si es válido o None si no se encuentra un número válido."""
    
    for intento in range (reintentos):
        numero = input(mensaje)
        numero = int(numero)
        if validar_numero_entero(numero,minimo,maximo):
            return numero
        else:
            print(mensaje_error)
        print(f"Intento numero: {intento+1}")
    
    print ("se terminaron los intentos :/")
    return None
    

    

def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:int) -> float|None:
    """Pedir un número por consola
    Args:
        mensaje(str): mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
        mensaje_error(str): mensaje de error en el caso de que el dato ingresado sea invalido.
        minimo(float): valor minimo admitido.
        maximo(float): valor maximo admitido.
        reintentos(int): cantidad de veces que se pide el dato en caso de error.
        
    Returns:
    float | None: retorna un entero si es válido o None si no se encuentra un número válido."""
    for intento in range (reintentos):
        numero = input(mensaje)
        numero = float(numero)
        if validar_numero_flotante(numero,minimo,maximo):
            return numero
        else:
            print(mensaje_error)
        print(f"Intento numero: {intento+1}")
    
    print ("se terminaron los intentos :/")
    return None
    
    
def get_string(mensaje:str, mensaje_error:str, longitud:int, reintentos:int) -> str|None:
    
    """Pedir una cadena por consola
    Args:
        mensaje(str): mensaje que se va a imprimir para de pedirle al usuario el dato por consola.
        mensaje_error(str): mensaje de error en el caso de que el dato ingresado sea invalido.
        longitud(int): numero de longitud de la cadena con la que debe cumplir.
        reintentos(int): cantidad de veces que se pide el dato en caso de error.
        
    Returns:
    float | None: retorna un entero si es válido o None si no se encuentra un número válido."""
    
    for intento in range(reintentos):
        cadena = input(mensaje)
        if validar_cadena(cadena,longitud):
            return cadena
        else: 
            print(mensaje_error)
        print(f"Intento numero: {intento+1}")
        
    print("Se terminaron los intentos :/")
    return None