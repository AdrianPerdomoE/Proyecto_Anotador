# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialogo_ModificarqYyEPK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogModificar(object):
    def setupUi(self, DialogModificar):
        if not DialogModificar.objectName():
            DialogModificar.setObjectName(u"DialogModificar")
        DialogModificar.resize(540, 264)
        DialogModificar.setMinimumSize(QSize(540, 243))
        DialogModificar.setModal(True)
        self.verticalLayout = QVBoxLayout(DialogModificar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(DialogModificar)
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
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 12pt \"Lucida Handwriting\";")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEditTitulo = QLineEdit(self.frame_6)
        self.lineEditTitulo.setObjectName(u"lineEditTitulo")
        self.lineEditTitulo.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditTitulo, 2, 1, 1, 1)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 12pt \"Lucida Handwriting\";")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.lineEditTituloNuevo = QLineEdit(self.frame_6)
        self.lineEditTituloNuevo.setObjectName(u"lineEditTituloNuevo")

        self.gridLayout.addWidget(self.lineEditTituloNuevo, 3, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_6)


        self.horizontalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame_16)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(DialogModificar)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setAutoFillBackground(True)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogModificar)
        self.buttonBox.accepted.connect(DialogModificar.accept)
        self.buttonBox.rejected.connect(DialogModificar.reject)

        QMetaObject.connectSlotsByName(DialogModificar)
    # setupUi

    def retranslateUi(self, DialogModificar):
        DialogModificar.setWindowTitle(QCoreApplication.translate("DialogModificar", u"Modificar ", None))
        self.label_2.setText(QCoreApplication.translate("DialogModificar", u" Titulo Anterior: ", None))
        self.lineEditTitulo.setInputMask("")
        self.lineEditTitulo.setPlaceholderText(QCoreApplication.translate("DialogModificar", u"Ingrese titulo unico", None))
        self.label_3.setText(QCoreApplication.translate("DialogModificar", u"Nuevo titulo: ", None))
        self.lineEditTituloNuevo.setInputMask("")
        self.lineEditTituloNuevo.setPlaceholderText(QCoreApplication.translate("DialogModificar", u"Ingrese titulo unico", None))
    # retranslateUi

