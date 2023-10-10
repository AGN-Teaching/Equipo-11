# tarjeta_credito.py

class TarjetaCredito:
    def _init_(self, numero, vencimiento):
        self.numero = numero
        self.vencimiento = vencimiento

    def mostrar_info(self):
        print(f"Número de Tarjeta: {self.numero}")
        print(f"Fecha de Vencimiento: {self.vencimiento}")