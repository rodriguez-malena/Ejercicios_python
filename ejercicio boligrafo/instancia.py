from clase_SmartPen import *

smart_pen_1 = Boligrafo("Grueso","Azul")
smart_pen_2 = Boligrafo("Fino","Rojo")
smart_pen_3 = Boligrafo("Grueso","Rosa")
smart_pen_4 = Boligrafo("Fino","Negro")
smart_pen_5 = Boligrafo("Grueso","Blanco")

lista_boligrafos:list["Boligrafo"] = []
lista_boligrafos.append(smart_pen_1)
lista_boligrafos.append(smart_pen_2)
lista_boligrafos.append(smart_pen_3)
lista_boligrafos.append(smart_pen_4)
lista_boligrafos.append(smart_pen_5)

for lapicera in lista_boligrafos:
    print(lapicera.mostrar_boligrafo())
    print("-"*50)
    

texto = "malena"
boligrafos_sin_tinta = []


while  lista_boligrafos:
    for lapicera in lista_boligrafos:
        lapicera.escribir(texto)
        print("-"*50)
    
        if lapicera.cantidad_tinta == 0:
            boligrafos_sin_tinta.append(lapicera)
            lista_boligrafos.remove(lapicera)
    

        
print("--- Boligrafos recargados --- ")
for lapicera in boligrafos_sin_tinta:
    lapicera.recargar(10)
    
    
