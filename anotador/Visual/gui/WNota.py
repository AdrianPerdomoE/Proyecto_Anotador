from PySide2.QtCore import SIGNAL
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QWidget, QDialog, QMessageBox

from anotador.Mundo.Errores import NotaExiste
from anotador.Visual.gui.Dialogos import DialogoCrear
from anotador.Visual.ui_Ventana_Nota import Ui_WNota


class WNota(QWidget):
    def __init__(self,parent,nota=None):
        QWidget.__init__(self,parent)
        self.ui = Ui_WNota()
        self.ui.setupUi(self)
        self._configurar()
        self.nota = nota

    def _configurar(self):
        self.ui.listViewEtiquetas.setModel(QStandardItemModel())
        self.connect(self.ui.pushButtonRegresar, SIGNAL("clicked()"), self.cambiar_ventana_anterior)
        self.ui.pushButtonagregarEtiqueta.clicked.connect(self.abrirdialogocrear)
        self.ui.listViewEtiquetas.selectionModel().selectionChanged.connect(self.selecionar_etiqueta)
        self.ui.pushButtonEliminarEtiqueta.clicked.connect(self.borraretiqueta)
        self.ui.pushButtonGuardar.clicked.connect(self.guardar)
        self.ui.pushButtonDestacar.clicked.connect(self.destacado)
        self.ui.plainTextEditContenido.textChanged.connect(self.habilitar_guardado)
    def habilitar_guardado(self):
        self.ui.pushButtonGuardar.setEnabled(True)
    def destacado(self):
        if self.ui.pushButtonDestacar.text()== "Destacar":
            self.ui.pushButtonDestacar.setText("Desmarcar")
            self.nota.destacar_nota(True)
        else:
            self.ui.pushButtonDestacar.setText("Destacar")
            self.nota.destacar_nota(False)
        self.parent().parent().notas_screen.actualizar_listanotas()
    def guardar(self):
        texto=self.ui.plainTextEditContenido.toPlainText()
        self.nota.contenido=texto
        self.ui.pushButtonGuardar.setEnabled(False)
    def actualizar_listaetiquetas(self):
        self.ui.listViewEtiquetas.model().clear()
        etiquetas = self.nota.etiquetas
        for etiqueta in etiquetas:
            item = QStandardItem(str(etiqueta))
            item.setEditable(False)
            item.etiqueta = etiqueta
            self.ui.listViewEtiquetas.model().appendRow(item)

    def abrirdialogocrear(self):
        dialogo = DialogoCrear(self)
        resp = dialogo.exec_()
        if resp == QDialog.Accepted:
            nombre = dialogo.ui.lineEditTitulo.text()
            try:
                self.nota.agregar_etiqueta(nombre)
                self.ingresar_listaetiquetas(nombre)
            except NotaExiste:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR EXISTENCIAL")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(f"Error Etiqueta con titulo {nombre} ya existe")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

    def ingresar_listaetiquetas(self, etiqueta):
        item = QStandardItem(str(etiqueta))
        item.setEditable(False)
        item.etiqueta = etiqueta
        self.ui.listViewEtiquetas.model().appendRow(item)

    def cambiar_ventana_anterior(self):
        self.parent().setCurrentWidget(
            self.parent().parent().notas_screen)
    def borraretiqueta(self):
        indice = self.ui.listViewEtiquetas.selectedIndexes()[0]
        nombre = self.ui.listViewEtiquetas.model().itemFromIndex(indice).etiqueta
        self.nota.eliminiar_etiqueta(nombre)
        self.actualizar_listaetiquetas()
        if len(self.nota.etiquetas) == 0:
            self.actualizar_boton_etiqueta(False)

    def selecionar_etiqueta(self, selected, deselected):
        indices = selected.indexes()
        if len(indices) > 0:
            self.actualizar_boton_etiqueta(True)
        else:
            self.actualizar_boton_etiqueta(False)

    def actualizar_boton_etiqueta(self, boolean: bool):
        self.ui.pushButtonEliminarEtiqueta.setEnabled(boolean)


