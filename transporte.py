class Transporte:
    def __init__(self, identificador: int, tipo:str, fecha_mantenimiento):
        self.identificador = identificador
        self.tipo = tipo
        self.fecha_mantenimiento = fecha_mantenimiento

    def verificar_disponibilidad(self, fecha):
        pass

    def __str__(self):
        pass

    def guardar_datos(self):
        pass

class TransportePasajeros(Transporte):
    def __init__(self, identificador: int, tipo:str, fecha_mantenimiento, numero_pasajeros:int):
       super().__init__(identificador, tipo, fecha_mantenimiento)
       self.numero_pasajeros =  numero_pasajeros
    
    def __str__(self):
        pass

    def guardar_datos(self):
        pass

class TransporteCarga(Transporte):
    def __init__(self, identificador: int, tipo:str, fecha_mantenimiento, capacidad_carga:float):
       super().__init__(identificador, tipo, fecha_mantenimiento)
       self.capacidad_carga =  capacidad_carga
    
    def __str__(self):
        pass

    def guardar_datos(self):
        pass
        


    


    