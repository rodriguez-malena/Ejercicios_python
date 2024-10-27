class Boligrafo:
    def __init__(self,grosor_punta,color):
        self.capacidad_tinta_max = 100
        self.grosor = grosor_punta
        self.color_boligrafo = color
        self.cantidad_tinta = 80
        
    def escribir(self,texto):
        if self.grosor == "Grueso":
            tinta_necesaria = len(texto) * 2
        elif self.grosor == "Fino":
            tinta_necesaria = len(texto)
        else:
            print("Grosor inexistente")
            
        if tinta_necesaria <= self.cantidad_tinta:
            self.cantidad_tinta -= tinta_necesaria
            print(f"{self.color_boligrafo}: {texto}")
            print(f"Cantidad de tinta restante: {self.cantidad_tinta}")
        else:
            print(f"{self.color_boligrafo}: No hay tinta suficiente")
            self.cantidad_tinta = 0

    def recargar(self,cantidad:int):
        lapicera_recargada = cantidad + self.cantidad_tinta
        
        if lapicera_recargada <= self.capacidad_tinta_max:
            print(f"Boligrafo {self.color_boligrafo} recargado con {lapicera_recargada}")
        else:
            print(f"Se recargó el  bolígrafo {self.color_boligrafo} y sobró {lapicera_recargada - self.capacidad_tinta_max} cantidad de tinta")
    
    def mostrar_boligrafo(self):
        string_formato = f"Bolígrafo color: {self.color_boligrafo} - Grosor: {self.grosor}. Con una capacidad máxima de tinta de: {self.capacidad_tinta_max} y una cantidad de tinta de: {self.cantidad_tinta}"
        return string_formato
        