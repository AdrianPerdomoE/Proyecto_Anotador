# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ventana_libroZzxuyn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FormSecciones(object):
    def setupUi(self, FormSecciones):
        if not FormSecciones.objectName():
            FormSecciones.setObjectName(u"FormSecciones")
        FormSecciones.resize(819, 698)
        self.verticalLayout = QVBoxLayout(FormSecciones)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(FormSecciones)
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
        self.labelLibros = QLabel(self.frame_5)
        self.labelLibros.setObjectName(u"labelLibros")
        font = QFont()
        font.setFamily(u"Lucida Handwriting")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelLibros.setFont(font)
        self.labelLibros.setStyleSheet(u"font: 20pt \"Lucida Handwriting\";\n"
"background-color: rgb(254, 255, 237);")
        self.labelLibros.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.labelLibros)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.listViewSecciones = QListView(self.frame_2)
        self.listViewSecciones.setObjectName(u"listViewSecciones")
        self.listViewSecciones.setStyleSheet(u"font: 16pt \"Lucida Handwriting\";")
        self.listViewSecciones.setViewMode(QListView.IconMode)
        self.listViewSecciones.setItemAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.listViewSecciones)


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
        self.pushButtonCrear_Seccion = QPushButton(self.frame_4)
        self.pushButtonCrear_Seccion.setObjectName(u"pushButtonCrear_Seccion")

        self.verticalLayout_4.addWidget(self.pushButtonCrear_Seccion)

        self.pushButton_Ver_seccion = QPushButton(self.frame_4)
        self.pushButton_Ver_seccion.setObjectName(u"pushButton_Ver_seccion")
        self.pushButton_Ver_seccion.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_Ver_seccion)

        self.pushButton_Modificar_seccion = QPushButton(self.frame_4)
        self.pushButton_Modificar_seccion.setObjectName(u"pushButton_Modificar_seccion")
        self.pushButton_Modificar_seccion.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_Modificar_seccion)

        self.pushButton_Archivar_seccion = QPushButton(self.frame_4)
        self.pushButton_Archivar_seccion.setObjectName(u"pushButton_Archivar_seccion")
        self.pushButton_Archivar_seccion.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_Archivar_seccion)

        self.pushButton_Borrar_seccion = QPushButton(self.frame_4)
        self.pushButton_Borrar_seccion.setObjectName(u"pushButton_Borrar_seccion")
        self.pushButton_Borrar_seccion.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_Borrar_seccion)

        self.pushButtonRegresar = QPushButton(self.frame_4)
        self.pushButtonRegresar.setObjectName(u"pushButtonRegresar")

        self.verticalLayout_4.addWidget(self.pushButtonRegresar)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(FormSecciones)

        QMetaObject.connectSlotsByName(FormSecciones)
    # setupUi

    def retranslateUi(self, FormSecciones):
        FormSecciones.setWindowTitle(QCoreApplication.translate("FormSecciones", u"Form", None))
        self.labelLibros.setText(QCoreApplication.translate("FormSecciones", u"Lista de secciones", None))
        self.pushButtonCrear_Seccion.setText(QCoreApplication.translate("FormSecciones", u"Crear nueva seccion", None))
        self.pushButton_Ver_seccion.setText(QCoreApplication.translate("FormSecciones", u"Ver seccion", None))
        self.pushButton_Modificar_seccion.setText(QCoreApplication.translate("FormSecciones", u"Modificar seccion", None))
        self.pushButton_Archivar_seccion.setText(QCoreApplication.translate("FormSecciones", u"Archivar seccion", None))
        self.pushButton_Borrar_seccion.setText(QCoreApplication.translate("FormSecciones", u"Borrar seccion", None))
        self.pushButtonRegresar.setText(QCoreApplication.translate("FormSecciones", u"Home", None))
    # retranslateUi

