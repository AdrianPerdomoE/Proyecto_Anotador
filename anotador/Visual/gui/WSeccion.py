from PySide2.QtCore import SIGNAL
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QDialog, QMessageBox, QWidget

from anotador.Mundo.mundo import *
from anotador.Visual.gui.Dialogos import DialogoCrear, DialogoModificar
from anotador.Visual.ui_Ventana_Seccion import Ui_WidgetPaginas


class WSeccion(QWidget):
    def __init__(self,parent,seccion=None):
        QWidget.__init__(self,parent)
        self.ui =Ui_WidgetPaginas()
        self.ui.setupUi(self)
        self._configurar()
        self.seccion =seccion

    def _configurar(self):
        self.ui.listViewPaginas.setModel(QStandardItemModel())
        self.connect(self.ui.pushButtonRegresar, SIGNAL("clicked()"), self.cambiar_ventana_anterior)
        self.ui.pushButtonCrear_Pagina.clicked.connect(self.abrirdialogocrear)
        self.ui.listViewPaginas.selectionModel().selectionChanged.connect(self.selecionar_pagina)
        self.ui.pushButton_Borrar_Pagina.clicked.connect(self.borrarpagina)
        self.ui.pushButton_Modificar_Pagina.clicked.connect(self.abrir_dialogo_modificar)
        self.ui.pushButton_Archivar_Pagina.clicked.connect(self.borrarpagina)
        self.connect(self.ui.pushButton_Ver_Pagina, SIGNAL("clicked()"), self.cambiar_ventana)

    def actualizar_listapaginas(self):
        self.ui.listViewPaginas.model().clear()
        paginas = self.seccion.paginas.values()
        for pagina in paginas:
            item = QStandardItem(str(pagina))
            item.setEditable(False)
            item.pagina = pagina
            self.ui.listViewPaginas.model().appendRow(item)

    def abrirdialogocrear(self):
        dialogo = DialogoCrear(self)
        resp = dialogo.exec_()
        if resp == QDialog.Accepted:
            titulo = dialogo.ui.lineEditTitulo.text()
            try:
                self.seccion.agregar_pagina(titulo)
                self.ingresar_listapaginas(self.seccion.paginas[titulo])
            except PaginaExiste:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR EXISTENCIAL")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(f"Error pagina con titulo {titulo} ya existe")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

    def ingresar_listapaginas(self, pagina):
        item = QStandardItem(str(pagina))
        item.setEditable(False)
        item.pagina =pagina
        self.ui.listViewPaginas.model().appendRow(item)

    def cambiar_ventana_anterior(self):
        self.parent().setCurrentWidget(
            self.parent().parent().secciones_screen)

    def actualizarSelecion(self):
        indice = self.ui.listViewPaginas.selectedIndexes()[0]
        pagina = self.ui.listViewPaginas.model().itemFromIndex(indice).pagina
        self.parent().parent().actualizar_notas_pantalla(pagina)

    def cambiar_ventana(self):
        self.actualizarSelecion()
        self.parent().setCurrentWidget(self.parent().parent().notas_screen)

    def abrir_dialogo_modificar(self):
        indice = self.ui.listViewPaginas.selectedIndexes()[0]
        titulo = self.ui.listViewPaginas.model().itemFromIndex(indice).pagina.nombre
        dialog = DialogoModificar(titulo)
        resp = dialog.exec_()
        new = dialog.ui.lineEditTituloNuevo.text()
        if resp == QDialog.Accepted:
            try:
                self.seccion.modificar_pagina(titulo, new)
                self.actualizar_listapaginas()
            except PaginaExiste:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR EXISTENCIAL")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(f"Error pagina con titulo {new} ya existe")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

    def borrarpagina(self):
        indice = self.ui.listViewPaginas.selectedIndexes()[0]
        titulo = self.ui.listViewPaginas.model().itemFromIndex(indice).pagina.nombre
        self.seccion.borrar_pagina(titulo)
        self.actualizar_listapaginas()
        if len(self.seccion.paginas) == 0:
            self.actualizar_botones_paginas(False)
            self.parent().parent().actualizar_botones_busquedas(False)

    def selecionar_pagina(self, selected, deselected):
        indices = selected.indexes()
        if len(indices) > 0:
            self.actualizar_botones_paginas(True)
        else:
            self.actualizar_botones_paginas(False)

    def actualizar_botones_paginas(self, boolean: bool):
        self.ui.pushButton_Archivar_Pagina.setEnabled(boolean)
        self.ui.pushButton_Ver_Pagina.setEnabled(boolean)
        self.ui.pushButton_Borrar_Pagina.setEnabled(boolean)
        self.ui.pushButton_Modificar_Pagina.setEnabled(boolean)
