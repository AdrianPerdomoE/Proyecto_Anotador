# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ventana_SeccionCykFHN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WidgetPaginas(object):
    def setupUi(self, WidgetPaginas):
        if not WidgetPaginas.objectName():
            WidgetPaginas.setObjectName(u"WidgetPaginas")
        WidgetPaginas.resize(818, 698)
        self.verticalLayout = QVBoxLayout(WidgetPaginas)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(WidgetPaginas)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(800, 680))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 252, 212);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 40))
        self.frame_5.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 7, 5, 4)
        self.labelpaginas = QLabel(self.frame_5)
        self.labelpaginas.setObjectName(u"labelpaginas")
        font = QFont()
        font.setFamily(u"Lucida Handwriting")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelpaginas.setFont(font)
        self.labelpaginas.setStyleSheet(u"font: 20pt \"Lucida Handwriting\";\n"
"background-color: rgb(254, 255, 237);")
        self.labelpaginas.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.labelpaginas)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.listViewPaginas = QListView(self.frame_2)
        self.listViewPaginas.setObjectName(u"listViewPaginas")
        self.listViewPaginas.setStyleSheet(u"font: 16pt \"Lucida Handwriting\";")
        self.listViewPaginas.setViewMode(QListView.IconMode)
        self.listViewPaginas.setItemAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.listViewPaginas)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(341, 0))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 252, 212);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(189, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButtonCrear_Pagina = QPushButton(self.frame_4)
        self.pushButtonCrear_Pagina.setObjectName(u"pushButtonCrear_Pagina")

        self.verticalLayout_4.addWidget(self.pushButtonCrear_Pagina)

        self.pushButton_Ver_Pagina = QPushButton(self.frame_4)
        self.pushButton_Ver_Pagina.setObjectName(u"pushButton_Ver_Pagina")
        self.pushButton_Ver_Pagina.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_Ver_Pagina)

        self.pushButton_Modificar_Pagina = QPushButton(self.frame_4)
        self.pushButton_Modificar_Pagina.setObjectName(u"pushButton_Modificar_Pagina")
        self.pushButton_Modificar_Pagina.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_Modificar_Pagina)

        self.pushButton_Archivar_Pagina = QPushButton(self.frame_4)
        self.pushButton_Archivar_Pagina.setObjectName(u"pushButton_Archivar_Pagina")
        self.pushButton_Archivar_Pagina.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_Archivar_Pagina)

        self.pushButton_Borrar_Pagina = QPushButton(self.frame_4)
        self.pushButton_Borrar_Pagina.setObjectName(u"pushButton_Borrar_Pagina")
        self.pushButton_Borrar_Pagina.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_Borrar_Pagina)

        self.pushButtonRegresar = QPushButton(self.frame_4)
        self.pushButtonRegresar.setObjectName(u"pushButtonRegresar")

        self.verticalLayout_4.addWidget(self.pushButtonRegresar)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(WidgetPaginas)

        QMetaObject.connectSlotsByName(WidgetPaginas)
    # setupUi

    def retranslateUi(self, WidgetPaginas):
        WidgetPaginas.setWindowTitle(QCoreApplication.translate("WidgetPaginas", u"Form", None))
        self.labelpaginas.setText(QCoreApplication.translate("WidgetPaginas", u"Lista de paginas", None))
        self.pushButtonCrear_Pagina.setText(QCoreApplication.translate("WidgetPaginas", u"Crear nueva pagina", None))
        self.pushButton_Ver_Pagina.setText(QCoreApplication.translate("WidgetPaginas", u"Ver pagina", None))
        self.pushButton_Modificar_Pagina.setText(QCoreApplication.translate("WidgetPaginas", u"Modificar pagina", None))
        self.pushButton_Archivar_Pagina.setText(QCoreApplication.translate("WidgetPaginas", u"Archivar pagina", None))
        self.pushButton_Borrar_Pagina.setText(QCoreApplication.translate("WidgetPaginas", u"Borrar pagina", None))
        self.pushButtonRegresar.setText(QCoreApplication.translate("WidgetPaginas", u"Atras", None))
    # retranslateUi

