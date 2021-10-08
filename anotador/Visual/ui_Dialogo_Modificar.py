# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialogo_Modificar_LibrowjHVEt.ui'
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
        DialogModificar.resize(540, 244)
        DialogModificar.setMinimumSize(QSize(540, 243))
        DialogModificar.setModal(True)
        self.verticalLayout = QVBoxLayout(DialogModificar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(DialogModificar)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(520, 200))
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
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEditTituloAntiguo = QLineEdit(self.frame_2)
        self.lineEditTituloAntiguo.setObjectName(u"lineEditTituloAntiguo")
        self.lineEditTituloAntiguo.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditTituloAntiguo, 1, 1, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 12pt \"Lucida Handwriting\";")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.lineEditTituloNuevo = QLineEdit(self.frame_2)
        self.lineEditTituloNuevo.setObjectName(u"lineEditTituloNuevo")

        self.gridLayout.addWidget(self.lineEditTituloNuevo, 2, 1, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 12pt \"Lucida Handwriting\";")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)


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
        self.label.setText(QCoreApplication.translate("DialogModificar", u"Nuevo titulo: ", None))
        self.lineEditTituloNuevo.setInputMask("")
        self.lineEditTituloNuevo.setPlaceholderText(QCoreApplication.translate("DialogModificar", u"Ingrese titulo unico", None))
        self.label_2.setText(QCoreApplication.translate("DialogModificar", u" Titulo Anterior: ", None))
    # retranslateUi

