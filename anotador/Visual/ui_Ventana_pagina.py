# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ventana_paginaXMnahM.ui'
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
        WNotas.resize(857, 701)
        self.verticalLayout = QVBoxLayout(WNotas)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(WNotas)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(32, 42, 84);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 4)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(64, 83, 168);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(9, 1, 9, 9)
        self.frame_16 = QFrame(self.frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"background-color: rgb(102, 101, 86);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 4)
        self.frame_3 = QFrame(self.frame_16)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 252, 212);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setStyleSheet(u"background-color: qlineargradient(spread:repeat,   x1:0.943, y1:1, x2:1, y2:1, stop:0 rgba(255, 252, 212, 255), stop:1 rgba(204, 202, 171, 255));")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_11)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(50, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.frame_11)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(255, 252, 212);")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 40))
        self.frame_8.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(6, 7, 5, 4)
        self.labelNotas_2 = QLabel(self.frame_8)
        self.labelNotas_2.setObjectName(u"labelNotas_2")
        font = QFont()
        font.setFamily(u"Lucida Handwriting")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelNotas_2.setFont(font)
        self.labelNotas_2.setStyleSheet(u"font: 20pt \"Lucida Handwriting\";\n"
"background-color: rgb(254, 255, 237);")
        self.labelNotas_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.labelNotas_2)


        self.verticalLayout_7.addWidget(self.frame_8)

        self.listViewNotas_2 = QListView(self.frame_6)
        self.listViewNotas_2.setObjectName(u"listViewNotas_2")
        self.listViewNotas_2.setStyleSheet(u"font: 16pt \"Lucida Handwriting\";")
        self.listViewNotas_2.setFrameShape(QFrame.NoFrame)
        self.listViewNotas_2.setFlow(QListView.TopToBottom)
        self.listViewNotas_2.setViewMode(QListView.IconMode)
        self.listViewNotas_2.setItemAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.listViewNotas_2)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.frame_15 = QFrame(self.frame_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(30, 0))
        self.frame_15.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 252, 212, 255), stop:1 rgba(204, 202, 171, 255));")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_15)


        self.horizontalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_16)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 252, 212);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_4)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMinimumSize(QSize(30, 0))
        self.frame_12.setMaximumSize(QSize(0, 16777215))
        self.frame_12.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(204, 202, 171, 255), stop:1 rgba(255, 252, 212, 255));")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_12)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setMinimumSize(QSize(189, 0))
        self.frame_9.setStyleSheet(u"background-color: rgb(255, 252, 212);")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.pushButtonCrear_Nota_2 = QPushButton(self.frame_9)
        self.pushButtonCrear_Nota_2.setObjectName(u"pushButtonCrear_Nota_2")

        self.verticalLayout_11.addWidget(self.pushButtonCrear_Nota_2)

        self.pushButton_Ver_Nota_2 = QPushButton(self.frame_9)
        self.pushButton_Ver_Nota_2.setObjectName(u"pushButton_Ver_Nota_2")
        self.pushButton_Ver_Nota_2.setEnabled(False)

        self.verticalLayout_11.addWidget(self.pushButton_Ver_Nota_2)

        self.pushButton_Modificar_Nota_2 = QPushButton(self.frame_9)
        self.pushButton_Modificar_Nota_2.setObjectName(u"pushButton_Modificar_Nota_2")
        self.pushButton_Modificar_Nota_2.setEnabled(False)

        self.verticalLayout_11.addWidget(self.pushButton_Modificar_Nota_2)

        self.pushButton_Archivar_Nota_2 = QPushButton(self.frame_9)
        self.pushButton_Archivar_Nota_2.setObjectName(u"pushButton_Archivar_Nota_2")
        self.pushButton_Archivar_Nota_2.setEnabled(False)

        self.verticalLayout_11.addWidget(self.pushButton_Archivar_Nota_2)

        self.pushButton_Borrar_Nota_2 = QPushButton(self.frame_9)
        self.pushButton_Borrar_Nota_2.setObjectName(u"pushButton_Borrar_Nota_2")
        self.pushButton_Borrar_Nota_2.setEnabled(False)

        self.verticalLayout_11.addWidget(self.pushButton_Borrar_Nota_2)

        self.pushButtonRegresar_2 = QPushButton(self.frame_9)
        self.pushButtonRegresar_2.setObjectName(u"pushButtonRegresar_2")

        self.verticalLayout_11.addWidget(self.pushButtonRegresar_2)


        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.frame_10.setStyleSheet(u"background-color: rgb(255, 252, 212);\n"
"background-color: qlineargradient(spread:repeat,  x1:0.25, y1:0.409, x2:0.624, y2:0.409, stop:0 rgba(204, 202, 171, 255), stop:1 rgba(255, 252, 212, 255));")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, -1, 0, -1)

        self.horizontalLayout_2.addWidget(self.frame_10)


        self.horizontalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frame_16)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(WNotas)

        QMetaObject.connectSlotsByName(WNotas)
    # setupUi

    def retranslateUi(self, WNotas):
        WNotas.setWindowTitle(QCoreApplication.translate("WNotas", u"Form", None))
        self.labelNotas_2.setText(QCoreApplication.translate("WNotas", u"Lista de notas", None))
        self.pushButtonCrear_Nota_2.setText(QCoreApplication.translate("WNotas", u"Crear nueva nota", None))
        self.pushButton_Ver_Nota_2.setText(QCoreApplication.translate("WNotas", u"Ver nota", None))
        self.pushButton_Modificar_Nota_2.setText(QCoreApplication.translate("WNotas", u"Modificar nota", None))
        self.pushButton_Archivar_Nota_2.setText(QCoreApplication.translate("WNotas", u"Archivar nota", None))
        self.pushButton_Borrar_Nota_2.setText(QCoreApplication.translate("WNotas", u"Borrar nota", None))
        self.pushButtonRegresar_2.setText(QCoreApplication.translate("WNotas", u"Atras", None))
    # retranslateUi

