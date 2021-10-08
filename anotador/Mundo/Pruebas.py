"""
import sys

from PySide2 import QtGui
from PySide2.QtCore import SIGNAL
from PySide2.QtWidgets import QMainWindow, QStackedWidget, QWidget, QHBoxLayout, QPushButton, QApplication, QLabel


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QMainWindow.__init__(self, parent)
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.start_screen = Start(self)
        self.second_screen = Second(self)
        self.central_widget.addWidget(self.start_screen)
        self.central_widget.addWidget(self.second_screen)
        self.central_widget.setCurrentWidget(self.start_screen)

        self.start_screen.clicked.connect(lambda: self.central_widget.setCurrentWidget(self.second_screen))
        self.second_screen.clicked.connect(lambda: self.central_widget.setCurrentWidget(self.start_screen))



class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QMainWindow.__init__(self, parent)
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.start_screen = Start(self)
        self.second_screen = Second(self)
        self.central_widget.addWidget(self.start_screen)
        self.central_widget.addWidget(self.second_screen)
        self.central_widget.setCurrentWidget(self.start_screen)



class Start(QWidget):

    def __init__(self, parent=None):
        super(Start, self).__init__(parent)
        layout = QHBoxLayout()
        button = QPushButton(text=('Push me!'))
        layout.addWidget(button)
        self.setLayout(layout)
        self.connect(button, SIGNAL("clicked()"), self.change_widget)

    def change_widget(self):
        self.parent().setCurrentWidget(
            self.parent().parent().second_screen)


class Second(QWidget):

    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        layout = QHBoxLayout()
        button = QPushButton(text=('Back to Start!'))
        layout.addWidget(button)
        self.setLayout(layout)
        self.connect(button, SIGNAL("clicked()"), self.change_widget)

    def change_widget(self):
        self.parent().setCurrentWidget(
            self.parent().parent().start_screen)

app = QApplication(sys.argv)
myWindow = MainWindow(None)
myWindow.show()
app.exec_()


class Principal(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        login_widget = LoginWidget(self)
        login_widget.button.clicked.connect(self.login)
        self.central_widget.addWidget(login_widget)
    def login(self):
        logged_in_widget = LoggedWidget(self)
        self.central_widget.addWidget(logged_in_widget)
        self.central_widget.setCurrentWidget(logged_in_widget)


class LoginWidget(QWidget):
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)
        layout = QHBoxLayout()
        self.button = QPushButton('Login')
        layout.addWidget(self.button)
        self.setLayout(layout)
        # you might want to do self.button.click.connect(self.parent().login) here


class LoggedWidget(QWidget):
    def __init__(self, parent=None):
        super(LoggedWidget, self).__init__(parent)
        layout = QHBoxLayout()
        self.label = QLabel('logged in!')
        layout.addWidget(self.label)
        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
import sys

from PySide2.QtCore import SIGNAL
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox, QWidget, QStackedWidget
from anotador.Mundo.mundo import *
from anotador.Visual.ui_Dialogo_Crear_Libro import Ui_Dialog_Crear_Libro
from anotador.Visual.ui_Dialogo_Modificar_Libro import Ui_DialogModificarLibro
from anotador.Visual.ui_Ventana_libro import Ui_FormSecciones
from anotador.Visual.ui_Widgetprincipal import Ui_WidgetPrincipal
class Secciones(QWidget):
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
    def actualizar_listasecciones(self):
        self.ui.listViewSecciones.model().clear()
        secciones=self.libro.secciones.values()
        for seccion in secciones:
            item = QStandardItem(str(seccion))
            item.setEditable(False)
            item.seccion = seccion
            self.ui.listViewSecciones.model().appendRow(item)
    def abrirdialogocrear(self):
        dialogo = DialogoCrearLibro(self)
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
        self.connect(self.ui.pushButton_Ver_Libro, SIGNAL("clicked()"), self.change_widget)
        #self.connect(self.ui.listViewLibros, SIGNAL("selectionChanged()"), self.actualizarSelecion)
    def actualizarSelecion(self):
        indice = self.ui.listViewLibros.selectedIndexes()[0]
        libro = self.ui.listViewLibros.model().itemFromIndex(indice).libro
        self.parent().parent().actualizar_segunda_pantalla(libro)
    def change_widget(self):
        self.parent().setCurrentWidget(self.parent().parent().second_screen)
    def abrir_dialogo_modificarlibro(self):
        indice = self.ui.listViewLibros.selectedIndexes()[0]
        titulo= self.ui.listViewLibros.model().itemFromIndex(indice).libro.nombre
        dialog=DialogoModificarLibro(titulo)
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
    def selecionar_libro(self,selected, deselected):
        indices=selected.indexes()
        if len(indices)>0:
            item=self.ui.listViewLibros.model().itemFromIndex(indices[0])
            self.actualizarSelecion()
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
        dialogo =DialogoCrearLibro(self)
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
class DialogoCrearLibro(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui =Ui_Dialog_Crear_Libro()
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
class DialogoModificarLibro(QDialog):
    def __init__(self,titulo, parent=None):
        QDialog.__init__(self, parent)
        self.ui =Ui_DialogModificarLibro()
        self.ui.setupUi(self)
        self.ui.lineEditTituloAntiguo.setText(titulo)
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
class ventana(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.anotador=Anotador()
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.start_screen = principal(self)
        self.central_widget.addWidget(self.start_screen)
        self.second_screen = Secciones(self)
        self.central_widget.addWidget(self.start_screen)
        self.central_widget.addWidget(self.second_screen)
        self.central_widget.setCurrentWidget(self.start_screen)
        self.anotador = Anotador()
        self.show()
    def actualizar_segunda_pantalla(self,libro):
        self.second_screen = Secciones(self,libro)
        self.second_screen.actualizar_listasecciones()
        self.central_widget.addWidget(self.second_screen)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ventana()
    sys.exit(app.exec_())"""