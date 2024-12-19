# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_login import Ui_LoginWindow

from router import RouterManager

from metodos import login_usuario

class LoginWindow(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)

        # inicializar un par de atributos

        # contendra la ui de nuestra ventana

        self.ui = Ui_LoginWindow()

        # configurar la ventana que vamos a mostrar
        self.ui.setupUi(self)

        self.router_manager = RouterManager()

        # cuando el boton registro sea presionado ejecutamos mandar a registro
        self.ui.registro.clicked.connect(self.mandar_a_registro)

        # iniciamos sesion con el usuario
        self.ui.inicio_sesion.clicked.connect(self.iniciar_sesion)

        # ese metodo redirige al usuario a la ventana de registro
    def mandar_a_registro(self):
        self.router_manager.acceder_registro(ventana_anterior=self)

        # inicia sesion y manda al usuario a la pagina principal
    def iniciar_sesion(self):


        correo = self.ui.correo.text()
        password = self.ui.password.text()

        login_usuario(correo, password)



        #else:
        #    self.ui.error.setText('El correo o la contraseña no coinciden :(')





# nos ayuda a depurar
if __name__ == "__main__":
    #crear una variable que conenga nuestra aplicacion
    app = QApplication(sys.argv)

    # la variable que va a contener nuestra ventana

    widget = LoginWindow()

    widget.show()

    # regitramos si el usuaro quiere salir de la app

    sys.exit(app.exec())





