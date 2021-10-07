# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialogo_Crear_LibroqxCfDZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_Crear_Libro(object):
    def setupUi(self, Dialog_Crear_Libro):
        if not Dialog_Crear_Libro.objectName():
            Dialog_Crear_Libro.setObjectName(u"Dialog_Crear_Libro")
        Dialog_Crear_Libro.resize(540, 243)
        self.verticalLayout = QVBoxLayout(Dialog_Crear_Libro)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog_Crear_Libro)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(520, 200))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 252, 212);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 12pt \"Lucida Handwriting\";")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEditTitulo = QLineEdit(self.frame_2)
        self.lineEditTitulo.setObjectName(u"lineEditTitulo")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditTitulo)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(Dialog_Crear_Libro)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStyleSheet(u"")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog_Crear_Libro)
        self.buttonBox.accepted.connect(Dialog_Crear_Libro.accept)
        self.buttonBox.rejected.connect(Dialog_Crear_Libro.reject)

        QMetaObject.connectSlotsByName(Dialog_Crear_Libro)
    # setupUi

    def retranslateUi(self, Dialog_Crear_Libro):
        Dialog_Crear_Libro.setWindowTitle(QCoreApplication.translate("Dialog_Crear_Libro", u"A\u00f1adir Libro", None))
        self.label.setText(QCoreApplication.translate("Dialog_Crear_Libro", u"Titulo: ", None))
        self.lineEditTitulo.setInputMask("")
        self.lineEditTitulo.setPlaceholderText(QCoreApplication.translate("Dialog_Crear_Libro", u"Ingrese titulo unico", None))
    # retranslateUi

