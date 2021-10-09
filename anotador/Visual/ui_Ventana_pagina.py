# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ventana_paginavSsBEV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WNotas(object):
    def setupUi(self, WNotas):
        if not WNotas.objectName():
            WNotas.setObjectName(u"WNotas")
        WNotas.resize(818, 698)
        self.verticalLayout = QVBoxLayout(WNotas)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(WNotas)
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
        self.labelNotas = QLabel(self.frame_5)
        self.labelNotas.setObjectName(u"labelNotas")
        font = QFont()
        font.setFamily(u"Lucida Handwriting")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelNotas.setFont(font)
        self.labelNotas.setStyleSheet(u"font: 20pt \"Lucida Handwriting\";\n"
"background-color: rgb(254, 255, 237);")
        self.labelNotas.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.labelNotas)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.listViewNotas = QListView(self.frame_2)
        self.listViewNotas.setObjectName(u"listViewNotas")
        self.listViewNotas.setStyleSheet(u"font: 16pt \"Lucida Handwriting\";")
        self.listViewNotas.setViewMode(QListView.IconMode)
        self.listViewNotas.setItemAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.listViewNotas)


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
        self.pushButtonCrear_Nota = QPushButton(self.frame_4)
        self.pushButtonCrear_Nota.setObjectName(u"pushButtonCrear_Nota")

        self.verticalLayout_4.addWidget(self.pushButtonCrear_Nota)

        self.pushButton_Ver_Nota = QPushButton(self.frame_4)
        self.pushButton_Ver_Nota.setObjectName(u"pushButton_Ver_Nota")
        self.pushButton_Ver_Nota.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_Ver_Nota)

        self.pushButton_Modificar_Nota = QPushButton(self.frame_4)
        self.pushButton_Modificar_Nota.setObjectName(u"pushButton_Modificar_Nota")
        self.pushButton_Modificar_Nota.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_Modificar_Nota)

        self.pushButton_Archivar_Nota = QPushButton(self.frame_4)
        self.pushButton_Archivar_Nota.setObjectName(u"pushButton_Archivar_Nota")
        self.pushButton_Archivar_Nota.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_Archivar_Nota)

        self.pushButton_Borrar_Nota = QPushButton(self.frame_4)
        self.pushButton_Borrar_Nota.setObjectName(u"pushButton_Borrar_Nota")
        self.pushButton_Borrar_Nota.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_Borrar_Nota)

        self.pushButtonRegresar = QPushButton(self.frame_4)
        self.pushButtonRegresar.setObjectName(u"pushButtonRegresar")

        self.verticalLayout_4.addWidget(self.pushButtonRegresar)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(WNotas)

        QMetaObject.connectSlotsByName(WNotas)
    # setupUi

    def retranslateUi(self, WNotas):
        WNotas.setWindowTitle(QCoreApplication.translate("WNotas", u"Form", None))
        self.labelNotas.setText(QCoreApplication.translate("WNotas", u"Lista de notas", None))
        self.pushButtonCrear_Nota.setText(QCoreApplication.translate("WNotas", u"Crear nueva nota", None))
        self.pushButton_Ver_Nota.setText(QCoreApplication.translate("WNotas", u"Ver nota", None))
        self.pushButton_Modificar_Nota.setText(QCoreApplication.translate("WNotas", u"Modificar nota", None))
        self.pushButton_Archivar_Nota.setText(QCoreApplication.translate("WNotas", u"Archivar nota", None))
        self.pushButton_Borrar_Nota.setText(QCoreApplication.translate("WNotas", u"Borrar nota", None))
        self.pushButtonRegresar.setText(QCoreApplication.translate("WNotas", u"Atras", None))
    # retranslateUi

