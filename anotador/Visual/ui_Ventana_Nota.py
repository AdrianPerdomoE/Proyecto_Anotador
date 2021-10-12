# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ventana_NotagPntRt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WNota(object):
    def setupUi(self, WNota):
        if not WNota.objectName():
            WNota.setObjectName(u"WNota")
        WNota.resize(827, 558)
        self.verticalLayout = QVBoxLayout(WNota)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(WNota)
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
        self.verticalLayout_18.setContentsMargins(60, 0, 0, 0)

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
        self.labelEtiquetas = QLabel(self.frame_8)
        self.labelEtiquetas.setObjectName(u"labelEtiquetas")
        font = QFont()
        font.setFamily(u"Lucida Handwriting")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelEtiquetas.setFont(font)
        self.labelEtiquetas.setStyleSheet(u"font: 20pt \"Lucida Handwriting\";\n"
"background-color: rgb(254, 255, 237);")
        self.labelEtiquetas.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.labelEtiquetas)


        self.verticalLayout_7.addWidget(self.frame_8)

        self.listViewEtiquetas = QListView(self.frame_6)
        self.listViewEtiquetas.setObjectName(u"listViewEtiquetas")
        self.listViewEtiquetas.setStyleSheet(u"font: 16pt \"Lucida Handwriting\";")
        self.listViewEtiquetas.setFrameShape(QFrame.NoFrame)
        self.listViewEtiquetas.setFlow(QListView.TopToBottom)
        self.listViewEtiquetas.setViewMode(QListView.IconMode)
        self.listViewEtiquetas.setItemAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.listViewEtiquetas)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButtonEliminarEtiqueta = QPushButton(self.frame_5)
        self.pushButtonEliminarEtiqueta.setObjectName(u"pushButtonEliminarEtiqueta")
        self.pushButtonEliminarEtiqueta.setEnabled(False)

        self.gridLayout.addWidget(self.pushButtonEliminarEtiqueta, 0, 2, 1, 1)

        self.pushButtonRegresar = QPushButton(self.frame_5)
        self.pushButtonRegresar.setObjectName(u"pushButtonRegresar")

        self.gridLayout.addWidget(self.pushButtonRegresar, 0, 0, 1, 1)

        self.pushButtonagregarEtiqueta = QPushButton(self.frame_5)
        self.pushButtonagregarEtiqueta.setObjectName(u"pushButtonagregarEtiqueta")
        self.pushButtonagregarEtiqueta.setEnabled(True)

        self.gridLayout.addWidget(self.pushButtonagregarEtiqueta, 0, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_5)


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
        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 40))
        self.frame_13.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_13)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(6, 7, 5, 4)
        self.labelNota = QLabel(self.frame_13)
        self.labelNota.setObjectName(u"labelNota")
        self.labelNota.setFont(font)
        self.labelNota.setStyleSheet(u"font: 20pt \"Lucida Handwriting\";\n"
"background-color: rgb(254, 255, 237);")
        self.labelNota.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.labelNota)


        self.verticalLayout_11.addWidget(self.frame_13)

        self.plainTextEditContenido = QPlainTextEdit(self.frame_9)
        self.plainTextEditContenido.setObjectName(u"plainTextEditContenido")
        self.plainTextEditContenido.setStyleSheet(u"font: 16pt \"Lucida Handwriting\";")
        self.plainTextEditContenido.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_11.addWidget(self.plainTextEditContenido)

        self.frame_7 = QFrame(self.frame_9)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonGuardar = QPushButton(self.frame_7)
        self.pushButtonGuardar.setObjectName(u"pushButtonGuardar")
        self.pushButtonGuardar.setEnabled(False)

        self.horizontalLayout.addWidget(self.pushButtonGuardar)

        self.pushButtonDestacar = QPushButton(self.frame_7)
        self.pushButtonDestacar.setObjectName(u"pushButtonDestacar")

        self.horizontalLayout.addWidget(self.pushButtonDestacar)


        self.verticalLayout_11.addWidget(self.frame_7)

        self.plainTextEditContenido.raise_()
        self.frame_13.raise_()
        self.frame_7.raise_()

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
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)

        self.horizontalLayout_2.addWidget(self.frame_10)


        self.horizontalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frame_16)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(WNota)

        QMetaObject.connectSlotsByName(WNota)
    # setupUi

    def retranslateUi(self, WNota):
        WNota.setWindowTitle(QCoreApplication.translate("WNota", u"Form", None))
        self.labelEtiquetas.setText(QCoreApplication.translate("WNota", u"Etiquetas:", None))
        self.pushButtonEliminarEtiqueta.setText(QCoreApplication.translate("WNota", u"Eliminar Etiqueta", None))
        self.pushButtonRegresar.setText(QCoreApplication.translate("WNota", u"Atras", None))
        self.pushButtonagregarEtiqueta.setText(QCoreApplication.translate("WNota", u"A\u00f1adir Etiqueta", None))
        self.labelNota.setText(QCoreApplication.translate("WNota", u"Nota", None))
        self.plainTextEditContenido.setPlaceholderText(QCoreApplication.translate("WNota", u"Escribe aqui.", None))
        self.pushButtonGuardar.setText(QCoreApplication.translate("WNota", u"Guardar cambios", None))
        self.pushButtonDestacar.setText(QCoreApplication.translate("WNota", u"Destacar", None))
    # retranslateUi

