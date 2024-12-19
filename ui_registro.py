# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_pagina_registro(object):
    def setupUi(self, pagina_registro):
        if not pagina_registro.objectName():
            pagina_registro.setObjectName(u"pagina_registro")
        pagina_registro.resize(800, 600)
        self.centralwidget = QWidget(pagina_registro)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 10, 411, 91))
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"font: 24pt \"Academy Engraved LET\";\n"
"font: 700 13pt \"Arial Narrow\";\n"
"font: 48pt \"Academy Engraved LET\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 90, 58, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 140, 58, 16))
        self.texto_nombre = QLineEdit(self.centralwidget)
        self.texto_nombre.setObjectName(u"texto_nombre")
        self.texto_nombre.setGeometry(QRect(110, 110, 311, 21))
        self.texto_apellidos = QLineEdit(self.centralwidget)
        self.texto_apellidos.setObjectName(u"texto_apellidos")
        self.texto_apellidos.setGeometry(QRect(110, 160, 311, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 190, 58, 16))
        self.telefono = QLineEdit(self.centralwidget)
        self.telefono.setObjectName(u"telefono")
        self.telefono.setGeometry(QRect(110, 210, 311, 21))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 240, 58, 16))
        self.correo = QLineEdit(self.centralwidget)
        self.correo.setObjectName(u"correo")
        self.correo.setGeometry(QRect(110, 260, 311, 21))
        self.password_1 = QLineEdit(self.centralwidget)
        self.password_1.setObjectName(u"password_1")
        self.password_1.setGeometry(QRect(110, 310, 311, 21))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 290, 81, 16))
        self.password_2 = QLineEdit(self.centralwidget)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setGeometry(QRect(110, 360, 311, 21))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(110, 340, 131, 16))
        self.registro = QPushButton(self.centralwidget)
        self.registro.setObjectName(u"registro")
        self.registro.setGeometry(QRect(540, 170, 121, 71))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(460, 260, 141, 16))
        self.inicio_sesion = QPushButton(self.centralwidget)
        self.inicio_sesion.setObjectName(u"inicio_sesion")
        self.inicio_sesion.setGeometry(QRect(610, 250, 131, 41))
        self.error = QLabel(self.centralwidget)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(510, 130, 201, 16))
        self.error.setStyleSheet(u"color: rgb(255, 62, 45)")
        pagina_registro.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(pagina_registro)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 37))
        pagina_registro.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(pagina_registro)
        self.statusbar.setObjectName(u"statusbar")
        pagina_registro.setStatusBar(self.statusbar)

        self.retranslateUi(pagina_registro)

        QMetaObject.connectSlotsByName(pagina_registro)
    # setupUi

    def retranslateUi(self, pagina_registro):
        pagina_registro.setWindowTitle(QCoreApplication.translate("pagina_registro", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("pagina_registro", u"R E G I S T R O", None))
        self.label_2.setText(QCoreApplication.translate("pagina_registro", u"Nombre(s)", None))
        self.label_3.setText(QCoreApplication.translate("pagina_registro", u"Apellidos", None))
        self.label_4.setText(QCoreApplication.translate("pagina_registro", u"Telefono", None))
        self.label_5.setText(QCoreApplication.translate("pagina_registro", u"Correo", None))
        self.password_1.setText("")
        self.label_6.setText(QCoreApplication.translate("pagina_registro", u"Contrase\u00f1a", None))
        self.password_2.setText("")
        self.label_7.setText(QCoreApplication.translate("pagina_registro", u"Verificar contrase\u00f1a", None))
        self.registro.setText(QCoreApplication.translate("pagina_registro", u"Registrarme", None))
        self.label_8.setText(QCoreApplication.translate("pagina_registro", u"\u00bfYa tienes una cuenta?", None))
        self.inicio_sesion.setText(QCoreApplication.translate("pagina_registro", u"Inicia sesion", None))
        self.error.setText("")
    # retranslateUi

