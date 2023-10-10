# cliente.py

from persona import Persona
from transporte import Transporte

class Cliente(Persona):
    def _init_(self, nombre, identificacion, tarjeta_credito):
        super()._init_(nombre, identificacion)
        self.tarjeta_credito = tarjeta_credito
        self.registro_renta = None

    def rentar_transporte(self, transporte):
        self.registro_renta = transporte

    def mostrar_info(self):
        super().mostrar_info()
        self.tarjeta_credito.mostrar_info()
        if self.registro_renta:
            print("Registro de Renta:")
            self.registro_renta.mostrar_info()