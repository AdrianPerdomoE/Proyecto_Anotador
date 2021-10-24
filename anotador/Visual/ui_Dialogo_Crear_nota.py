# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialogo_Crear_notawQxsab.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_Crear_nota(object):
    def setupUi(self, Dialog_Crear):
        if not Dialog_Crear.objectName():
            Dialog_Crear.setObjectName(u"Dialog_Crear")
        Dialog_Crear.resize(540, 243)
        self.verticalLayout = QVBoxLayout(Dialog_Crear)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog_Crear)
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
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_16)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 252, 212);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(255, 252, 212);")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 12pt \"Lucida Handwriting\";")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEditTitulo = QLineEdit(self.frame_6)
        self.lineEditTitulo.setObjectName(u"lineEditTitulo")

        self.gridLayout.addWidget(self.lineEditTitulo, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 12pt \"Lucida Handwriting\";")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEditEtiqueta = QLineEdit(self.frame_6)
        self.lineEditEtiqueta.setObjectName(u"lineEditEtiqueta")

        self.gridLayout.addWidget(self.lineEditEtiqueta, 1, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_6)


        self.horizontalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame_16)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(Dialog_Crear)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStyleSheet(u"")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog_Crear)
        self.buttonBox.accepted.connect(Dialog_Crear.accept)
        self.buttonBox.rejected.connect(Dialog_Crear.reject)

        QMetaObject.connectSlotsByName(Dialog_Crear)
    # setupUi

    def retranslateUi(self, Dialog_Crear):
        Dialog_Crear.setWindowTitle(QCoreApplication.translate("Dialog_Crear", u"A\u00f1adir ", None))
        self.label.setText(QCoreApplication.translate("Dialog_Crear", u"Titulo: ", None))
        self.lineEditTitulo.setInputMask("")
        self.lineEditTitulo.setPlaceholderText(QCoreApplication.translate("Dialog_Crear", u"Ingrese titulo unico*", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_Crear", u"Etiqueta:", None))
        self.lineEditEtiqueta.setInputMask("")
        self.lineEditEtiqueta.setPlaceholderText(QCoreApplication.translate("Dialog_Crear", u"Ingrese etiqueta *", None))
    # retranslateUi

