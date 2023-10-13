from datetime import datetime
class Transporte:
    def __init__(self, identificador, tipo_vehiculo, fecha_mantenimiento):
        self.identificador = identificador
        self.tipo_vehiculo = tipo_vehiculo
        self.fecha_mantenimiento = fecha_mantenimiento

    def verificar_disponibilidad(self, fecha):
        pass

    def guardar_datos(self):
        return self.identificador+","+self.tipo_vehiculo+","+datetime.strftime(self.fecha_mantenimiento, "%Y/%m/%d")

class TransportePasajeros(Transporte):
    def __init__(self, identificador,tipo_vehiculo, fecha_mantenimiento, numero_pasajeros):
       super().__init__(identificador,tipo_vehiculo,fecha_mantenimiento)
       self.numero_pasajeros =  numero_pasajeros

    def guardar_datos(self):
        return "Pasajeros,"+super().guardar_datos()+","+str(self.numero_pasajeros)+"\n"

class TransporteCarga(Transporte):
    def __init__(self, identificador,tipo_vehiculo, fecha_mantenimiento, capacidad_carga):
       super().__init__(identificador,tipo_vehiculo,fecha_mantenimiento)
       self.capacidad_carga =  capacidad_carga

    def guardar_datos(self):
        return "Carga,"+super().guardar_datos()+","+str(self.capacidad_carga)+"\n"