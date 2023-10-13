from datetime import datetime
class RegistroRenta:
    def __init__(self, fecha_inicio,fecha_fin,nombre_cliente:str,licencia_manejo:int, vehiculos):
        self.vehiculos = vehiculos
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.nombre_cliente = nombre_cliente
        self.licencia_manejo =licencia_manejo

    def guardar_datos(self):
        return datetime.strftime(self.fecha_inicio, "%Y/%m/%d")+","+datetime.strftime(self.fecha_fin, "%Y/%m/%d")+","+self.nombre_cliente+","+self.licencia_manejo+","+"&".join(self.vehiculos)+"\n"