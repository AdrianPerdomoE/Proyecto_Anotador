from PySide2.QtCore import SIGNAL
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QDialog, QMessageBox, QWidget
from anotador.Mundo.mundo import *
from anotador.Visual.gui.wprincipal import DialogoModificar, DialogoCrear
from anotador.Visual.ui_Ventana_libro import Ui_FormSecciones

class WSeccion(QWidget):
    def __init__(self,parent,libro=None):
        QWidget.__init__(self,parent)
        self.ui=Ui_FormSecciones()
        self.ui.setupUi(self)
        self._configurar()
        self.libro=libro
    def _configurar(self):
        self.ui.listViewSecciones.setModel(QStandardItemModel())
        self.connect(self.ui.pushButtonRegresar, SIGNAL("clicked()"), self.change_widget)
        self.ui.pushButtonCrear_Seccion.clicked.connect(self.abrirdialogocrear)
        self.ui.listViewSecciones.selectionModel().selectionChanged.connect(self.selecionar_seccion)
        self.ui.pushButton_Borrar_seccion.clicked.connect(self.borrarseccion)
        self.ui.pushButton_Modificar_seccion.clicked.connect(self.abrir_dialogo_modificar)
        self.ui.pushButton_Archivar_seccion.clicked.connect(self.borrarseccion)
        self.connect(self.ui.pushButton_Ver_seccion, SIGNAL("clicked()"), self.change_stage)
    def actualizar_listasecciones(self):
        self.ui.listViewSecciones.model().clear()
        secciones=self.libro.secciones.values()
        for seccion in secciones:
            item = QStandardItem(str(seccion))
            item.setEditable(False)
            item.seccion = seccion
            self.ui.listViewSecciones.model().appendRow(item)
    def abrirdialogocrear(self):
        dialogo = DialogoCrear(self)
        resp = dialogo.exec_()
        if resp == QDialog.Accepted:
            titulo = dialogo.ui.lineEditTitulo.text()
            try:
                self.libro.agregar_seccion(titulo)
                self.ingresar_listasecciones(self.libro.secciones[titulo])
            except SeccionExiste:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR EXISTENCIAL")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(f"Error Seccion con titulo {titulo} ya existe")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
    def ingresar_listasecciones(self, seccion):
        item = QStandardItem(str(seccion))
        item.setEditable(False)
        item.seccion=seccion
        self.ui.listViewSecciones.model().appendRow(item)
    def change_widget(self):
        self.parent().setCurrentWidget(
            self.parent().parent().start_screen)
    def actualizarSelecion(self):
        indice = self.ui.listViewSecciones.selectedIndexes()[0]
        seccion = self.ui.listViewSecciones.model().itemFromIndex(indice).seccion
        self.parent().parent().actualizar_paginas_pantalla(seccion)
    def change_stage(self):
        self.parent().setCurrentWidget(self.parent().parent().paginas_screen)
    def abrir_dialogo_modificar(self):
        indice = self.ui.listViewSecciones.selectedIndexes()[0]
        titulo= self.ui.listViewSecciones.model().itemFromIndex(indice).seccion.nombre
        dialog=DialogoModificar(titulo)
        resp=dialog.exec_()
        new=dialog.ui.lineEditTituloNuevo.text()
        if resp==QDialog.Accepted:
            try:
                self.libro.modificar_seccion(titulo,new)
                self.actualizar_listasecciones()
            except SeccionExiste:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR EXISTENCIAL")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(f"Error seccion con titulo {new} ya existe")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
    def borrarseccion(self):
        indice=self.ui.listViewSecciones.selectedIndexes()[0]
        titulo=self.ui.listViewSecciones.model().itemFromIndex(indice).seccion.nombre
        self.libro.borrar_seccion(titulo)
        self.actualizar_listasecciones()
        if len(self.libro.secciones)==0:
            self.actualizar_botones_secciones(False)
    def selecionar_seccion(self,selected, deselected):
        indices=selected.indexes()
        if len(indices)>0:
            self.actualizarSelecion()
            self.actualizar_botones_secciones(True)
        else:
            self.actualizar_botones_secciones(False)

    def actualizar_botones_secciones(self, boolean:bool):
        self.ui.pushButton_Archivar_seccion.setEnabled(boolean)
        self.ui.pushButton_Ver_seccion.setEnabled(boolean)
        self.ui.pushButton_Borrar_seccion.setEnabled(boolean)
        self.ui.pushButton_Modificar_seccion.setEnabled(boolean)
