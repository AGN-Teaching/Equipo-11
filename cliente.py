class Cliente:
    def __init__(self,  nombre:str, identificacion:str, tarjeta_credito:str):
        self.nombre = nombre
        self.identificacion = identificacion
        self.tarjeta_credito = tarjeta_credito
        #self.fecha_caducidad =fecha_caducidad
        #self.cvv = cvv
        
    def __str__(self):
        pass

    def guardar_datos(self):
        pass