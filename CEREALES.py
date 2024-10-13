from os import system

def crear_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any)->list:
    matrix = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matrix += [fila]
    return matrix
    
def cargar_existencias(matrix:list,minimo_kg:int,maximo_kg:int)-> None:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            while True:
                matrix [i][j] = float(input(f"Ingrese cantidad para el deposito [{i}] y el cereal [{j}]:  "))
            
                if minimo_kg <= matrix[i][j] <= maximo_kg:
                    break
                else:
                    print("Inválido, reingrese")
                    
                    
def cantidad_kilos_por_deposito(matrix:list,valor:any)->list:
    cantidad_deposito = [valor] * len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            cantidad_deposito [i] += matrix[i][j]
    return cantidad_deposito
    
def cereal_menos_kg(matrix:list,nombres_cereales:list)->list:
    menor_cereal_por_depo = [0] * len(matrix)
    for i in range(len(matrix)):
        bandera_cereal = True
        menor_cereal = ""
        menor_cantidad = 0 
        for j in range(len(matrix[i])):
            if matrix[i][j] < menor_cantidad or bandera_cereal:
                menor_cantidad = matrix[i][j]
                menor_cereal = nombres_cereales[j] 
                bandera_cereal = False
            menor_cereal_por_depo [i] = menor_cereal
    return menor_cereal_por_depo

def cereal_maximo_kg(matrix:list,nombre_cereales:list)->list:
    """Función que calcula la máxima cantidad de kilos almacenados de cada cereal.
    DE CADA CEREAL CUAL ALMACENÓ + KILOS 
    LISTA QUE ACUMULE LA SUMA FINAL DE CADA COLUMNA DE CEREALES,LUEGO RECORRO
    LA LISTA COMPARO Y MUESTRO CANTIDAD MAXIMA DE CADA CEREAL"""
    maximo_kg_por_cereal = [0] * len(matrix[0])
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            maximo_kg_por_cereal[j] += matrix[i][j]

    maximo_almacenado = 0
    nombre_cereal_maximo = ""
    maximo =  []
    for j in range(len(maximo_kg_por_cereal)):
        if maximo_kg_por_cereal[j] > maximo_almacenado :
            maximo_almacenado = maximo_kg_por_cereal[j]
            nombre_cereal_maximo = nombre_cereales[j]

    maximo = [nombre_cereal_maximo,maximo_almacenado]
    return maximo

def deposito_mayor_recaudacion(matrix:list,precio_kg:int,nombre_cereal:list)->list:
    """Depósito con mayor recaudación, teniendo en cuenta que disponemos
de un vector con los valores por kilo de cada tipo de cereal."""
    recaudaciones = [0] * len(matrix)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            recaudaciones [i] += matrix[i][j] * precio_kg[j] 
    
    maxima_recaudacion = 0
    bandera_maxima = True
    deposito = 0
    mayor_recaudacion = []
    
    for i in range(len(recaudaciones)):
        if recaudaciones[i] > maxima_recaudacion or bandera_maxima:
            maxima_recaudacion = recaudaciones[i]
            bandera_maxima = False
            deposito = i
        mayor_recaudacion = [deposito,maxima_recaudacion]
    return mayor_recaudacion
        
def depositos_mas_de_50000kg(cantidad_kg_depositos:list)->int:
    """Cantidad de depósitos que hayan almacenado más de 50000 kilos    
    entre los 4 cereales"""
    contador_depositos_mas_50000kg = 0
    for i in range (len(cantidad_kg_depositos)):
        if cantidad_kg_depositos[i] >= 50000:
            contador_depositos_mas_50000kg += 1
    return contador_depositos_mas_50000kg

def cereal_mayor_porcentaje(matrix:list,nombre_cereal:list):
    """Porcentaje de kilos de cada cereal sobre el total de kilos almacenados.
    Además mostrar el nombre del cereal con el máximo porcentaje."""
    cereales_kg = [0] * len(matrix[0])
    acumulador_kg = 0
    porcentaje_maximo = 0
    bandera_porcentaje = True
    cereal_mayor_porcentaje = ""
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            cereales_kg[j] += matrix[i][j]
    
    for x in range(len(cereales_kg)):
        acumulador_kg += cereales_kg[x]
    
    porcentaje_por_cereal = [0] * len(cereales_kg)
    
    for y in range(len(cereales_kg)):
        porcentaje_por_cereal[y] = (cereales_kg[y] * 100) / acumulador_kg
        
    for z in range(len(porcentaje_por_cereal)):
        if porcentaje_por_cereal[z] > porcentaje_maximo or bandera_porcentaje:
            porcentaje_maximo = porcentaje_por_cereal[z]
            cereal_mayor_porcentaje = nombre_cereal[z]
            
    return porcentaje_por_cereal,porcentaje_maximo,cereal_mayor_porcentaje
            
def informe_recaudaciones_odenado(matrix:list,precio_kg:int):
    """Generar un informe con la recaudación de cada depósito, ordenada de
mayor a menor."""
    recaudaciones = [0] * len(matrix)
    indices = [0] * len(matrix)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            recaudaciones [i] += matrix[i][j] * precio_kg[j] 
            indices[i] = i
    
    for y in range(len(recaudaciones)-1):
        for z in range(y+1,len(recaudaciones)):
            if recaudaciones[y] < recaudaciones[z]:
                auxiliar = recaudaciones[y]
                recaudaciones[y] = recaudaciones[z]
                recaudaciones[z] = auxiliar  
                
                auxiliar_indice = indices[y]
                indices[y] = indices[z]
                indices[z] = auxiliar_indice
                
    return recaudaciones,indices


def mostrar_matriz(matrix:list)->None:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()

lista_nombres_cereales = ["maiz","trigo","cebada","centeno"]
valor_kg = [54.8, 23.7,69.4,45.7]

matriz = crear_matriz(3,4,0)



bandera_salida = True
while bandera_salida:
    opcion = int(input("""Menú de opciones:
    1. Cargar existencia.
    2. Calcular por cada depósito la cantidad total de kilos almacenados entre
    todos los cereales.
    3. Nombre del cereal que almacenó menos kilos en cada depósito.
    4. Máxima cantidad de kilos almacenados de cada cereal.
    5. Depósito con mayor recaudación
    6. Cantidad de depósitos que hayan almacenado más de 50000 kilos    
    entre los 4 cereales.
    7. Porcentaje de kilos de cada cereal sobre el total de kilos almacenados.
    Además mostrar el nombre del cereal con el máximo porcentaje.
    8. Generar un informe con la recaudación de cada depósito, ordenada de
    mayor a menor.
    9. Salir
    Elija una opcion: """))
    match opcion:
        case 1:
            print("-"*50)
            cargar_existencias(matriz,5000,20000)
            mostrar_matriz(matriz)
            print("-"*50)

        case 2:
            print("-"*50)
            cantidad_kilos = cantidad_kilos_por_deposito(matriz,0)
            for i in range(len(cantidad_kilos)):
                print(f"Depósito {i} = {cantidad_kilos[i]}kg")
            print("-"*50)

        case 3:
            print("-"*50)
            menor_cereal_deposito = cereal_menos_kg(matriz,lista_nombres_cereales)
            for i in range(len(menor_cereal_deposito)):
                print(f"Menor cereal del depósito {i}: {menor_cereal_deposito[i]}")
            print("-"*50)

        case 4:
            print("-"*50)
            maximo_kilo_cereal = cereal_maximo_kg(matriz,lista_nombres_cereales)
            print(f"Cereal con máxima cantidad: {maximo_kilo_cereal[0]}, Cantidad: {maximo_kilo_cereal[1]} kg")
            print("-"*50)

        case 5:
            print("-"*50)
            deposito_recaudacion = deposito_mayor_recaudacion(matriz,valor_kg,lista_nombres_cereales)
            print(f"Deposito con mayor recaudación: {deposito_recaudacion[0]} - Valor ${deposito_recaudacion[1]} ")
            print("-"*50)
        
        case 6:
            print("-"*50)
            mas_de_50000kg = depositos_mas_de_50000kg(cantidad_kilos)
            print(f"Cantidad de depósitos con más de 50000kg = {mas_de_50000kg}")
            print("-"*50)
        case 7:
            print("-"*50)
            porcentaje_cereales,max_porcentaje, cereal_maximo = cereal_mayor_porcentaje(matriz,lista_nombres_cereales)
            for i in range(len(porcentaje_cereales)):
                print(f"Porcentaje de kilos de {lista_nombres_cereales[i]}: {porcentaje_cereales[i]}")
                
            print(f"El cereal con mayor porcentaje es {cereal_maximo} con {max_porcentaje:.2f}% ")
            print("-"*50)
        case 8:
            print("-"*50)
            recaudacion_orden, indice_orden= informe_recaudaciones_odenado(matriz,valor_kg)
            for i in range(len(recaudacion_orden)):
                print(f"Depósito:{indice_orden[i]} - Recaudación = ${recaudacion_orden[i]} ")
            print("-"*50)
        case 9:
            print("-"*50)
            print("Saliendo, gracias :)")
            bandera_salida = False
            print("-"*50)
        case _:
            print("-"*50)
            print("Opción inválida")
            print("-"*50)

system("pause")
system("cls")