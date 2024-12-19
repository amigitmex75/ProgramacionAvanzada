# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# desde el archivo registro.ui quier que importes el componente pagina_registro

from ui_registro import Ui_pagina_registro

from router import RouterManager

from metodos import registrar_usuario

# from router import RouterManager

# comletamos la importacion de mi apartad grafico

class PaginaRegistro(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.router_manager = RouterManager()


        # le indicamos a nuestro codigo de donde obtendra la parte visual
        self.ui = Ui_pagina_registro()

        # le decimos que se inicialice
        self.ui.setupUi(self)

        self.ui.registro.clicked.connect(self.validar_datos)

        self.ui.inicio_sesion.clicked.connect(self.mandar_login)


    # essta funcion se va a encargar de verificar que ningun dato este faltando
    def validar_datos(self):

        # obtenemos toda la informacion que el usuario haya registrado
        nombre = self.ui.texto_nombre.text()
        apellidos = self.ui.texto_apellidos.text()
        telefono = self.ui.telefono.text()
        correo = self.ui.correo.text()
        password_1 = self.ui.password_1.text()
        password_2 = self.ui.password_2.text()


        # 1. aegurarnos que ningun parametros este vacio

        if len(nombre) <= 0 or len(apellidos) <= 0 or len(telefono) <= 0 or len(password_1) <= 0:
            print('Error: Datos faltantes')
            self.ui.error.setText('Error: Datos Faltantes')


        elif '@' not in correo and '.' not in correo:
            print('Error: Correo no valido')
            self.ui.error.setText('Error: Correo no valido')

        elif password_1 != password_2:
            print('Error contraseñas no coinciden')
            self.ui.error.setText('Error: Contraseña no coinciden')

        else:
            print('Todos los datos son correctos :D')
            self.ui.error.setText('')


            resultado = registrar_usuario(nombre, apellidos, telefono, correo, password_1)

            # si se cumple significa que tenemos un usuario previamente registrado
            if 'Error' in resultado:
                self.ui.error.setText('Este usuario ya esta registrado con otra cuenta')

            else:

            self.mandar_login()

            def mandar_login(self):

         #  self.router_manager.acceder_login(self)



# -------------------------------------


if __name__ == "__main__":
    #Primero creamos una aplicacion
    app = QApplication(sys.argv)

    #Creamos la visya de la aplicacion
    widget = PaginaRegistro()

    # Muestra la aplicacion
    widget.show()

    #Salimos de la aplicacion si el usuario cierra la ventana
    sys.exit(app.exec())



