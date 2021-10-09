from PySide2.QtCore import SIGNAL
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QDialog, QMessageBox, QWidget
from anotador.Mundo.mundo import *
from anotador.Visual.gui.Dialogos import DialogoCrear, DialogoModificar
from anotador.Visual.ui_Ventana_pagina import Ui_WNotas


class WNota(QWidget):
    def __init__(self,parent,pagina=None):
        QWidget.__init__(self,parent)
        self.ui =Ui_WNotas()
        self.ui.setupUi(self)
        self._configurar()
        self.pagina =pagina

    def _configurar(self):
        self.ui.listViewNotas.setModel(QStandardItemModel())
        self.connect(self.ui.pushButtonRegresar, SIGNAL("clicked()"), self.change_widget)
        self.ui.pushButtonCrear_Nota.clicked.connect(self.abrirdialogocrear)
        self.ui.listViewNotas.selectionModel().selectionChanged.connect(self.selecionar_nota)
        self.ui.pushButton_Borrar_Nota.clicked.connect(self.borrarnota)
        self.ui.pushButton_Modificar_Nota.clicked.connect(self.abrir_dialogo_modificar)
        self.ui.pushButton_Archivar_Nota.clicked.connect(self.borrarnota)
        #self.connect(self.ui.pushButton_Ver_Nota, SIGNAL("clicked()"), self.change_stage)

    def actualizar_listanotas(self):
        self.ui.listViewNotas.model().clear()
        notas = self.pagina.notas.values()#Buscar error
        for nota in notas:
            item = QStandardItem(str(nota))
            item.setEditable(False)
            item.nota = nota
            self.ui.listViewNotas.model().appendRow(item)

    def abrirdialogocrear(self):
        dialogo = DialogoCrear(self)
        resp = dialogo.exec_()
        if resp == QDialog.Accepted:
            titulo = dialogo.ui.lineEditTitulo.text()
            try:
                self.pagina.agregar_nota(titulo)
                self.ingresar_listanotas(self.pagina.notas[titulo])
            except PaginaExiste:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR EXISTENCIAL")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(f"Error nota con titulo {titulo} ya existe")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

    def ingresar_listanotas(self, nota):
        item = QStandardItem(str(nota))
        item.setEditable(False)
        item.nota =nota
        self.ui.listViewNotas.model().appendRow(item)

    def change_widget(self):
        self.parent().setCurrentWidget(
            self.parent().parent().paginas_screen)

    def actualizarSelecion(self):
        indice = self.ui.listViewNotas.selectedIndexes()[0]
        nota = self.ui.listViewNotas.model().itemFromIndex(indice).nota
        self.parent().parent().actualizar_notas_pantalla(nota)

   #def change_stage(self):
    #    self.parent().setCurrentWidget(self.parent().parent().nota_screen)
    def abrir_dialogo_modificar(self):
        indice = self.ui.listViewNotas.selectedIndexes()[0]
        titulo = self.ui.listViewNotas.model().itemFromIndex(indice).nota.nombre
        dialog = DialogoModificar(titulo)
        resp = dialog.exec_()
        new = dialog.ui.lineEditTituloNuevo.text()
        if resp == QDialog.Accepted:
            try:
                self.seccion.modificar_pagina(titulo, new)
                self.actualizar_listanotas()
            except NotaExiste:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR EXISTENCIAL")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(f"Error Nota con titulo {new} ya existe")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

    def borrarnota(self):
        indice = self.ui.listViewNotas.selectedIndexes()[0]
        titulo = self.ui.listViewNotas.model().itemFromIndex(indice).pagina.nombre
        self.seccion.borrar_pagina(titulo)
        self.actualizar_listanotas()
        if len(self.pagina.notas) == 0:
            self.actualizar_botones_notas(False)

    def selecionar_nota(self, selected, deselected):
        indices = selected.indexes()
        if len(indices) > 0:
            self.actualizarSelecion()
            self.actualizar_botones_notas(True)
        else:
            self.actualizar_botones_notas(False)

    def actualizar_botones_notas(self, boolean: bool):
        self.ui.pushButton_Archivar_Nota.setEnabled(boolean)
        self.ui.pushButton_Ver_Nota.setEnabled(boolean)
        self.ui.pushButton_Borrar_Nota.setEnabled(boolean)
        self.ui.pushButton_Modificar_Nota.setEnabled(boolean)
