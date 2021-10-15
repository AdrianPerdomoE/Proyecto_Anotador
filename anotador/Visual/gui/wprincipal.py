from PySide2.QtCore import SIGNAL
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QDialog, QMessageBox, QWidget
from anotador.Mundo.mundo import *
from anotador.Visual.gui.Dialogos import DialogoCrear, DialogoModificar
from anotador.Visual.ui_Widgetprincipal import Ui_WidgetPrincipal


class principal(QWidget):
    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.ui =Ui_WidgetPrincipal()
        self.ui.setupUi(self)
        self._configurar()
        self.anotador=parent.anotador
    def _configurar(self):
        self.ui.pushButtonCrear_Libro.clicked.connect(self.abrir_dialogo_crearlibro)
        self.ui.listViewLibros.setModel(QStandardItemModel())
        self.ui.listViewLibros.selectionModel().selectionChanged.connect(self.selecionar_libro)
        self.ui.pushButton_Borrar_Libro.clicked.connect(self.borrarlibro)
        self.ui.pushButton_Modificar_Libro.clicked.connect(self.abrir_dialogo_modificarlibro)
        self.ui.pushButton_Archivar_Libro.clicked.connect(self.borrarlibro)
        self.connect(self.ui.pushButton_Ver_Libro, SIGNAL("clicked()"), self.cambiar_Ventana)
        self.connect(self.ui.pushButton_Buscar_Nota,SIGNAL("clicked()"),self.buscar)
    def buscar(self):
        self.parent().setCurrentWidget(self.parent().parent().buscador_screen)
        self.parent().parent().buscador_screen.ui.listViewNotas.model().clear()
        self.parent().parent().buscador_screen.ui.lineEditEtiqueta.setText("")
    def actualizarSelecion(self):
        indice = self.ui.listViewLibros.selectedIndexes()[0]
        libro = self.ui.listViewLibros.model().itemFromIndex(indice).libro
        self.parent().parent().actualizar_secciones_pantalla(libro)
    def cambiar_Ventana(self):
        self.actualizarSelecion()
        self.parent().setCurrentWidget(self.parent().parent().secciones_screen)
    def abrir_dialogo_modificarlibro(self):
        indice = self.ui.listViewLibros.selectedIndexes()[0]
        titulo= self.ui.listViewLibros.model().itemFromIndex(indice).libro.nombre
        dialog=DialogoModificar(titulo)
        resp=dialog.exec_()
        new=dialog.ui.lineEditTituloNuevo.text()
        if resp==QDialog.Accepted:
            try:
                self.anotador.modificar_libro(titulo,new)
                self.actualizar_listalibros()
            except LibroExiste:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR EXISTENCIAL")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(f"Error Libro con titulo {new} ya existe")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

    def borrarlibro(self):
        indice=self.ui.listViewLibros.selectedIndexes()[0]
        titulo=self.ui.listViewLibros.model().itemFromIndex(indice).libro.nombre
        self.anotador.borrar_libro(titulo)
        self.actualizar_listalibros()
        if len(self.anotador.libros)==0:
            self.actualizar_botones_libro(False)
            self.parent().parent().actualizar_botones_busquedas(False)
    def selecionar_libro(self,selected, deselected):
        indices=selected.indexes()
        if len(indices)>0:
            self.actualizar_botones_libro(True)
        else:
            self.actualizar_botones_libro(False)

    def actualizar_botones_libro(self, boolean:bool):
        self.ui.pushButton_Archivar_Libro.setEnabled(boolean)
        self.ui.pushButton_Ver_Libro.setEnabled(boolean)
        self.ui.pushButton_Borrar_Libro.setEnabled(boolean)
        self.ui.pushButton_Modificar_Libro.setEnabled(boolean)
    def actualizar_listalibros(self):
        self.ui.listViewLibros.model().clear()
        libros=self.anotador.libros.values()
        for libro in libros:
            item = QStandardItem(str(libro))
            item.setEditable(False)
            item.libro = libro
            self.ui.listViewLibros.model().appendRow(item)
    def ingresar_listalibros(self, libro):
        item = QStandardItem(str(libro))
        item.setEditable(False)
        item.libro=libro
        self.ui.listViewLibros.model().appendRow(item)

    def abrir_dialogo_crearlibro(self):
        dialogo =DialogoCrear(self)
        resp = dialogo.exec_()
        if resp==QDialog.Accepted:
            titulo=dialogo.ui.lineEditTitulo.text()
            try:
                self.anotador.agregar_libro(titulo)
                self.ingresar_listalibros(self.anotador.libros[titulo])
            except LibroExiste:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR EXISTENCIAL")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(f"Error Libro con titulo {titulo} ya existe")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()