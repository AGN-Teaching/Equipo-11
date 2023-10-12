class RegistroRenta:
    def __init__(self, fecha_inicio,fecha_fin,nombre_cliente:str,licencia_manejo:int, vehiculos):
        self.vehiculos = vehiculos
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.nombre_cliente = nombre_cliente
        self.licencia_manejo =licencia_manejo

    def __str__(self):
        pass

    def guardar_datos(self):
        pass