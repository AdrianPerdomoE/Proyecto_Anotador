# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Libro_layoutFkPeVv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_libro_layout(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(725, 546)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
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
        self.verticalLayout_2.setContentsMargins(-1, 1, -1, -1)
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
        self.frame_11.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:0.373051, y1:0.409, x2:0.624, y2:0.409, stop:0 rgba(255, 252, 212, 255), stop:1 rgba(204, 202, 171, 255));")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_11)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")

        self.horizontalLayout_3.addWidget(self.frame_11)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 252, 212);\n"
"")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 40))
        self.frame_7.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(6, 7, 5, 4)
        self.labelLibros_2 = QLabel(self.frame_7)
        self.labelLibros_2.setObjectName(u"labelLibros_2")
        font = QFont()
        font.setFamily(u"Lucida Handwriting")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelLibros_2.setFont(font)
        self.labelLibros_2.setStyleSheet(u"font: 20pt \"Lucida Handwriting\";\n"
"background-color: rgb(254, 255, 237);")
        self.labelLibros_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.labelLibros_2)


        self.verticalLayout_9.addWidget(self.frame_7)

        self.listViewLibros_2 = QListView(self.frame_5)
        self.listViewLibros_2.setObjectName(u"listViewLibros_2")
        self.listViewLibros_2.setStyleSheet(u"font: 16pt \"Lucida Handwriting\";")
        self.listViewLibros_2.setFrameShape(QFrame.NoFrame)
        self.listViewLibros_2.setFrameShadow(QFrame.Sunken)
        self.listViewLibros_2.setLineWidth(1)
        self.listViewLibros_2.setViewMode(QListView.IconMode)
        self.listViewLibros_2.setItemAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.listViewLibros_2)


        self.horizontalLayout_3.addWidget(self.frame_5)

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
        self.pushButtonCrear_Libro_2 = QPushButton(self.frame_9)
        self.pushButtonCrear_Libro_2.setObjectName(u"pushButtonCrear_Libro_2")

        self.verticalLayout_11.addWidget(self.pushButtonCrear_Libro_2)

        self.pushButton_Ver_Libro_2 = QPushButton(self.frame_9)
        self.pushButton_Ver_Libro_2.setObjectName(u"pushButton_Ver_Libro_2")
        self.pushButton_Ver_Libro_2.setEnabled(False)

        self.verticalLayout_11.addWidget(self.pushButton_Ver_Libro_2)

        self.pushButton_Modificar_Libro_2 = QPushButton(self.frame_9)
        self.pushButton_Modificar_Libro_2.setObjectName(u"pushButton_Modificar_Libro_2")
        self.pushButton_Modificar_Libro_2.setEnabled(False)

        self.verticalLayout_11.addWidget(self.pushButton_Modificar_Libro_2)

        self.pushButton_Archivar_Libro_2 = QPushButton(self.frame_9)
        self.pushButton_Archivar_Libro_2.setObjectName(u"pushButton_Archivar_Libro_2")
        self.pushButton_Archivar_Libro_2.setEnabled(False)

        self.verticalLayout_11.addWidget(self.pushButton_Archivar_Libro_2)

        self.pushButton_Borrar_Libro_2 = QPushButton(self.frame_9)
        self.pushButton_Borrar_Libro_2.setObjectName(u"pushButton_Borrar_Libro_2")
        self.pushButton_Borrar_Libro_2.setEnabled(False)

        self.verticalLayout_11.addWidget(self.pushButton_Borrar_Libro_2)

        self.pushButton_Informe_Etiqueta_2 = QPushButton(self.frame_9)
        self.pushButton_Informe_Etiqueta_2.setObjectName(u"pushButton_Informe_Etiqueta_2")
        self.pushButton_Informe_Etiqueta_2.setEnabled(False)

        self.verticalLayout_11.addWidget(self.pushButton_Informe_Etiqueta_2)

        self.pushButton_Buscar_Nota_2 = QPushButton(self.frame_9)
        self.pushButton_Buscar_Nota_2.setObjectName(u"pushButton_Buscar_Nota_2")
        self.pushButton_Buscar_Nota_2.setEnabled(False)

        self.verticalLayout_11.addWidget(self.pushButton_Buscar_Nota_2)

        self.pushButton_Notas_Destacadas_2 = QPushButton(self.frame_9)
        self.pushButton_Notas_Destacadas_2.setObjectName(u"pushButton_Notas_Destacadas_2")
        self.pushButton_Notas_Destacadas_2.setEnabled(False)

        self.verticalLayout_11.addWidget(self.pushButton_Notas_Destacadas_2)


        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.frame_10.setStyleSheet(u"background-color: rgb(255, 252, 212);\n"
"background-color: qlineargradient(spread:repeat, x1:0.373051, y1:0.409, x2:0.624, y2:0.409, stop:0 rgba(204, 202, 171, 255), stop:1 rgba(255, 252, 212, 255));")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.horizontalLayout_2.addWidget(self.frame_10)


        self.horizontalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frame_16)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelLibros_2.setText(QCoreApplication.translate("Form", u"Lista de Libros", None))
        self.pushButtonCrear_Libro_2.setText(QCoreApplication.translate("Form", u"Crear nuevo libro", None))
        self.pushButton_Ver_Libro_2.setText(QCoreApplication.translate("Form", u"Ver libro", None))
        self.pushButton_Modificar_Libro_2.setText(QCoreApplication.translate("Form", u"Modificar libro", None))
        self.pushButton_Archivar_Libro_2.setText(QCoreApplication.translate("Form", u"Archivar libro", None))
        self.pushButton_Borrar_Libro_2.setText(QCoreApplication.translate("Form", u"Borrar libro", None))
        self.pushButton_Informe_Etiqueta_2.setText(QCoreApplication.translate("Form", u"Informe etiqueta", None))
        self.pushButton_Buscar_Nota_2.setText(QCoreApplication.translate("Form", u"Buscar nota", None))
        self.pushButton_Notas_Destacadas_2.setText(QCoreApplication.translate("Form", u"Notas destacadas", None))
    # retranslateUi

