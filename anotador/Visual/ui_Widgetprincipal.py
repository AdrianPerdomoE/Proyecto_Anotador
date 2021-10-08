# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WidgetprincipalnNEoOv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WidgetPrincipal(object):
    def setupUi(self, WidgetPrincipal):
        if not WidgetPrincipal.objectName():
            WidgetPrincipal.setObjectName(u"WidgetPrincipal")
        WidgetPrincipal.resize(642, 304)
        self.verticalLayout = QVBoxLayout(WidgetPrincipal)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(WidgetPrincipal)
        self.frame.setObjectName(u"frame")
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

        self.listViewLibros = QListView(self.frame_2)
        self.listViewLibros.setObjectName(u"listViewLibros")
        self.listViewLibros.setStyleSheet(u"font: 16pt \"Lucida Handwriting\";")
        self.listViewLibros.setViewMode(QListView.IconMode)
        self.listViewLibros.setItemAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.listViewLibros)


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
        self.pushButtonCrear_Libro = QPushButton(self.frame_4)
        self.pushButtonCrear_Libro.setObjectName(u"pushButtonCrear_Libro")

        self.verticalLayout_4.addWidget(self.pushButtonCrear_Libro)

        self.pushButton_Ver_Libro = QPushButton(self.frame_4)
        self.pushButton_Ver_Libro.setObjectName(u"pushButton_Ver_Libro")
        self.pushButton_Ver_Libro.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_Ver_Libro)

        self.pushButton_Modificar_Libro = QPushButton(self.frame_4)
        self.pushButton_Modificar_Libro.setObjectName(u"pushButton_Modificar_Libro")
        self.pushButton_Modificar_Libro.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_Modificar_Libro)

        self.pushButton_Archivar_Libro = QPushButton(self.frame_4)
        self.pushButton_Archivar_Libro.setObjectName(u"pushButton_Archivar_Libro")
        self.pushButton_Archivar_Libro.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_Archivar_Libro)

        self.pushButton_Borrar_Libro = QPushButton(self.frame_4)
        self.pushButton_Borrar_Libro.setObjectName(u"pushButton_Borrar_Libro")
        self.pushButton_Borrar_Libro.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_Borrar_Libro)

        self.pushButton_Informe_Etiqueta = QPushButton(self.frame_4)
        self.pushButton_Informe_Etiqueta.setObjectName(u"pushButton_Informe_Etiqueta")
        self.pushButton_Informe_Etiqueta.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_Informe_Etiqueta)

        self.pushButton_Buscar_Nota = QPushButton(self.frame_4)
        self.pushButton_Buscar_Nota.setObjectName(u"pushButton_Buscar_Nota")
        self.pushButton_Buscar_Nota.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_Buscar_Nota)

        self.pushButton_Notas_Destacadas = QPushButton(self.frame_4)
        self.pushButton_Notas_Destacadas.setObjectName(u"pushButton_Notas_Destacadas")
        self.pushButton_Notas_Destacadas.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_Notas_Destacadas)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(WidgetPrincipal)

        QMetaObject.connectSlotsByName(WidgetPrincipal)
    # setupUi

    def retranslateUi(self, WidgetPrincipal):
        WidgetPrincipal.setWindowTitle(QCoreApplication.translate("WidgetPrincipal", u"Form", None))
        self.labelLibros.setText(QCoreApplication.translate("WidgetPrincipal", u"Lista de Libros", None))
        self.pushButtonCrear_Libro.setText(QCoreApplication.translate("WidgetPrincipal", u"Crear nuevo libro", None))
        self.pushButton_Ver_Libro.setText(QCoreApplication.translate("WidgetPrincipal", u"Ver libro", None))
        self.pushButton_Modificar_Libro.setText(QCoreApplication.translate("WidgetPrincipal", u"Modificar libro", None))
        self.pushButton_Archivar_Libro.setText(QCoreApplication.translate("WidgetPrincipal", u"Archivar libro", None))
        self.pushButton_Borrar_Libro.setText(QCoreApplication.translate("WidgetPrincipal", u"Borrar libro", None))
        self.pushButton_Informe_Etiqueta.setText(QCoreApplication.translate("WidgetPrincipal", u"Informe etiqueta", None))
        self.pushButton_Buscar_Nota.setText(QCoreApplication.translate("WidgetPrincipal", u"Buscar nota", None))
        self.pushButton_Notas_Destacadas.setText(QCoreApplication.translate("WidgetPrincipal", u"Notas destacadas", None))
    # retranslateUi

