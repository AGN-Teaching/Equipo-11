class Menu:
    def mostrar_menu(self, opciones):
        print('Seleccione una opción:')
        for clave in sorted(opciones):
            print(f' {clave}) {opciones[clave][0]}')


    def leer_opcion(self, opciones):
        while (opcion := input('Opción: ')) not in opciones:
            print('Opción incorrecta, vuelva a intentarlo.')
        return opcion


    def ejecutar_opcion(self, opcion, opciones):
        opciones[opcion][1]()


    def generar_menu(self, opciones, opcion_salida):
        opcion = None
        while opcion != opcion_salida:
            self.mostrar_menu(opciones)
            opcion = self.leer_opcion(opciones)
            self.ejecutar_opcion(opcion, opciones)
            print()