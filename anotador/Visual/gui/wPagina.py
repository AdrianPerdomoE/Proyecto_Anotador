from PySide2.QtCore import SIGNAL
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QDialog, QMessageBox, QWidget
from anotador.Mundo.mundo import *
from anotador.Visual.gui.Dialogos import DialogoCrear, DialogoModificar
from anotador.Visual.ui_Ventana_pagina import Ui_WNotas


class WPagina(QWidget):
    def __init__(self,parent,pagina=None):
        QWidget.__init__(self,parent)
        self.ui =Ui_WNotas()
        self.ui.setupUi(self)
        self._configurar()
        self.pagina=pagina

    def _configurar(self):
        self.ui.listViewNotas_2.setModel(QStandardItemModel())
        self.connect(self.ui.pushButtonRegresar_2, SIGNAL("clicked()"), self.cambiar_vetana_anterior)
        self.ui.pushButtonCrear_Nota_2.clicked.connect(self.abrirdialogocrear)
        self.ui.listViewNotas_2.selectionModel().selectionChanged.connect(self.selecionar_nota)
        self.ui.pushButton_Borrar_Nota_2.clicked.connect(self.borrarnota)
        self.ui.pushButton_Modificar_Nota_2.clicked.connect(self.abrir_dialogo_modificar)
        self.ui.pushButton_Archivar_Nota_2.clicked.connect(self.borrarnota)
        self.connect(self.ui.pushButton_Ver_Nota_2, SIGNAL("clicked()"), self.cambiar_ventana)

    def actualizar_listanotas(self):
        self.ui.listViewNotas_2.model().clear()
        notas = self.pagina.notas.values()
        for nota in notas:
            item = QStandardItem(str(nota))
            item.setEditable(False)
            item.nota = nota
            self.ui.listViewNotas_2.model().appendRow(item)

    def abrirdialogocrear(self):
        dialogo = DialogoCrear(self)
        resp = dialogo.exec_()
        if resp == QDialog.Accepted:
            titulo = dialogo.ui.lineEditTitulo.text()
            try:
                self.pagina.agregar_nota(titulo)
                self.ingresar_listanotas(self.pagina.notas[titulo])
                self.parent().parent().actualizar_botones_busquedas(True)
                self.parent().parent().actualizar_nota_actual(self.pagina.notas[titulo])
                self.parent().setCurrentWidget(self.parent().parent().nota_actual_screen)

            except NotaExiste:
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
        self.ui.listViewNotas_2.model().appendRow(item)

    def cambiar_vetana_anterior(self):
        self.parent().setCurrentWidget(
            self.parent().parent().paginas_screen)

    def actualizarSelecion(self):
        indice = self.ui.listViewNotas_2.selectedIndexes()[0]
        nota = self.ui.listViewNotas_2.model().itemFromIndex(indice).nota
        self.parent().parent().actualizar_nota_actual(nota)

    def cambiar_ventana(self):
        self.actualizarSelecion()
        self.parent().setCurrentWidget(self.parent().parent().nota_actual_screen)
    def abrir_dialogo_modificar(self):
        indice = self.ui.listViewNotas_2.selectedIndexes()[0]
        titulo = self.ui.listViewNotas_2.model().itemFromIndex(indice).nota.nombre
        dialog = DialogoModificar(titulo)
        resp = dialog.exec_()
        new = dialog.ui.lineEditTituloNuevo.text()
        if resp == QDialog.Accepted:
            try:
                self.pagina.modificar_nombre_nota(titulo, new)
                self.actualizar_listanotas()
            except NotaExiste:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR EXISTENCIAL")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(f"Error Nota con titulo {new} ya existe")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

    def borrarnota(self):
        indice = self.ui.listViewNotas_2.selectedIndexes()[0]
        titulo = self.ui.listViewNotas_2.model().itemFromIndex(indice).nota.nombre
        self.pagina.borrar_nota(titulo)
        self.actualizar_listanotas()
        if len(self.pagina.notas) == 0:
            self.actualizar_botones_notas(False)
            self.parent().parent().actualizar_botones_busquedas(False)

    def selecionar_nota(self, selected, deselected):
        indices = selected.indexes()
        if len(indices) > 0:
            self.actualizar_botones_notas(True)
        else:
            self.actualizar_botones_notas(False)

    def actualizar_botones_notas(self, boolean: bool):
        self.ui.pushButton_Archivar_Nota_2.setEnabled(boolean)
        self.ui.pushButton_Ver_Nota_2.setEnabled(boolean)
        self.ui.pushButton_Borrar_Nota_2.setEnabled(boolean)
        self.ui.pushButton_Modificar_Nota_2.setEnabled(boolean)
