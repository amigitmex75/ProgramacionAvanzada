# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_pagina_principal

from router import RouterManager

class pagina_principal(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


        self.ui = Ui_pagina_principal()

        # de ese apartado grafico lo inicializamos
        self.ui.setupUi(self)

        # creamos un objeto de tipo router manager
        self.router_manager = RouterManager()

        self.ui.cerrar_sesion.clicked.connect(self.cerrar_sesion)

    def cerrar_sesion(self):

        #esta linea de codigo nos ayuda a enviar al usuario al login
        self.router_manager.acceder_login(ventana_anterior=self)


# Determina si el usuario esta ejecutando este archivo
if __name__ == "__main__":

    #Primero creamos una aplicacion
    app = QApplication(sys.argv)

    #Creamos la visya de la aplicacion
    widget = pagina_principal()

    # Muestra la aplicacion
    widget.show()

    #Salimos de la aplicacion si el usuario cierra la ventana
    sys.exit(app.exec())
