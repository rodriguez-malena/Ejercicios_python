tema = " Karina | J mena | Angela - SinVerguenza "
vistas = "45.8 millones"
duracion = "228"
link = "https://www.youtube.com/watch?v=AhZvCgk1Ay4"
fecha_lanzamiento = "2023-12-05"

from datetime import datetime

def obtener_colaboradores(titulo: str) -> list:
    particion = titulo.split("-")
    if len(particion) > 1:
        #print(particion)
        colaboradores = particion[0] #colaboradores guarda los elementos 0 de la lista que se generó haciendo particion
        #print(colaboradores)
        cantantes = colaboradores.split("|")
        return cantantes
    else:
        return []
    
def obtener_nombre_tema(titulo:str) -> str:
    if "-" in titulo:
        cancion = titulo.split("-")[1]
        nombre_tema = cancion.strip()
        return nombre_tema
    else:
        return titulo
        
    
def convertir_vistas_numerico(visualizaciones: str)->int:
    """convertirá la cantidad de vistas a un número entero expresado en millones."""
    numero = visualizaciones.replace("millones","")
    numero.strip()
    vistas_en_entero = int(float(numero) * 1000000)
    return vistas_en_entero 

def convertir_duracion_numerico(segundos: str)->int:
    segundos_entero = int(segundos)
    duracion_en_entero = round(segundos_entero / 60)
    return duracion_en_entero

def obtener_codigo(url:str)->str:
    """"retorna el código de la url recibida como parámetro."""
    _,codigo = url.split("=",1)
    return codigo

def formatear_fecha(fecha: str): 
    """retorna la fecha recibida por parámetro como un objeto de tipo fecha """
    date_time_str = fecha
    date_time_object = datetime.strptime(date_time_str, "%Y-%m-%d").date()
    return date_time_object
