# este archivo nos ayudara a manejar las rutas


class RouterManager():
    def __init__(self):

        # nos ayudara a determinar desde que ventana venimos
        self.ventana_actual = None


    def acceder_login(self, ventana_anterior=None):
        from pagina_login import LoginWindow

        # creamos un objeto de la ventana nueva que queremos mostrar
        self.ventana_actual = LoginWindow()

        self.ventana_actual.show()

        # cerramos la ventana anterior
        ventana_anterior.close()


    def acceder_registro(self, ventana_anterior=None):
        from pagina_registro import PaginaRegistro

        self.ventana_actual = PaginaRegistro()
        self.ventana_actual.show()
        ventana_anterior.close()

    def acceder_principal(self, ventana_anterior=None):
        from pagina_principal import pagina_principal

        self.ventana_actual = pagina_principal()
        self.ventana_actual.show()
        ventana_anterior.close()





