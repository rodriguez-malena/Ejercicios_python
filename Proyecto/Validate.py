
def validar_numero_entero( numero: int, minimo:int, maximo:int) -> bool:
    """
    Valida si el número pedido es mayor es mayor o menor .
    
    Args:
        numero (int): El número a validar.
        minimo (int): Número mínimo requerido.
        maximo (int): Número máximo requerido
        
    Returns:
        bool: True si el número es válido, False en caso contrario.
    """
    return minimo <= numero <= maximo

def validar_numero_flotante(numero:float, minimo:float, maximo:float) -> bool:
    """
    Valida si el número pedido es mayor es mayor o menor .
    
    Args:
        numero (int): El número a validar.
        minimo (int): Número mínimo requerido.
        maximo (int): Número máximo requerido
        
    Returns:
        bool: True si el número es válido, False en caso contrario.
    """
    
    return minimo <= numero <= maximo

def validar_cadena(cadena:str, longitud:int) -> bool:
    """
    Valida si la longitud de la cadena es mayor o igual a la longitud mínima.
    
    Args:
        cadena (str): La cadena a validar.
        longitud (int): Longitud mínima requerida.
        
    Returns:
        bool: True si la cadena es válida, False en caso contrario.
    """
    return len(cadena) > longitud