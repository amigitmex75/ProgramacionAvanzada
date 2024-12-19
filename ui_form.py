# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_pagina_principal(object):
    def setupUi(self, pagina_principal):
        if not pagina_principal.objectName():
            pagina_principal.setObjectName(u"pagina_principal")
        pagina_principal.resize(589, 534)
        self.centralwidget = QWidget(pagina_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 201, 111))
        self.label.setStyleSheet(u"font: 36pt \"Arial\";")
        self.cerrar_sesion = QPushButton(self.centralwidget)
        self.cerrar_sesion.setObjectName(u"cerrar_sesion")
        self.cerrar_sesion.setGeometry(QRect(410, 380, 131, 41))
        self.cerrar_sesion.setStyleSheet(u"font: 13pt \"Academy Engraved LET\";")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 110, 101, 21))
        self.label_2.setStyleSheet(u"font: 18pt \"Arial\";")
        pagina_principal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(pagina_principal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 589, 37))
        pagina_principal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(pagina_principal)
        self.statusbar.setObjectName(u"statusbar")
        pagina_principal.setStatusBar(self.statusbar)

        self.retranslateUi(pagina_principal)

        QMetaObject.connectSlotsByName(pagina_principal)
    # setupUi

    def retranslateUi(self, pagina_principal):
        pagina_principal.setWindowTitle(QCoreApplication.translate("pagina_principal", u"pagina_principal", None))
        self.label.setText(QCoreApplication.translate("pagina_principal", u"PRINCIPAL", None))
        self.cerrar_sesion.setText(QCoreApplication.translate("pagina_principal", u"CERRAR SECION", None))
        self.label_2.setText(QCoreApplication.translate("pagina_principal", u"Bienvenido", None))
    # retranslateUi

