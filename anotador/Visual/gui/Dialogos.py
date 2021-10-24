from PySide2.QtWidgets import QDialog, QMessageBox

from anotador.Visual.ui_Dialogo_Crear import Ui_Dialog_Crear
from anotador.Visual.ui_Dialogo_Crear_nota import Ui_Dialog_Crear_nota
from anotador.Visual.ui_Dialogo_Modificar import Ui_DialogModificar


class DialogoModificar(QDialog):
    def __init__(self,titulo, parent=None):
        QDialog.__init__(self, parent)
        self.ui =Ui_DialogModificar()
        self.ui.setupUi(self)
        self.ui.lineEditTitulo.setText(titulo)
    def accept(self) -> None:
        if self.ui.lineEditTituloNuevo.text() != "":
            super().accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos obligatorios.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
class DialogoCrear(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui =Ui_Dialog_Crear()
        self.ui.setupUi(self)
    def accept(self) -> None:
        if self.ui.lineEditTitulo.text() != "":
            super().accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos obligatorios.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
class DialogoCrear_nota(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui =Ui_Dialog_Crear_nota()
        self.ui.setupUi(self)
    def accept(self) -> None:
        if self.ui.lineEditTitulo.text() != "" and self.ui.lineEditEtiqueta.text()!="":
            super().accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos obligatorios.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
