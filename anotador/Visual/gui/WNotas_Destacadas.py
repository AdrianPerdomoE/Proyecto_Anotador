from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QWidget, QMessageBox
from anotador.Mundo.Errores import NoElementFound
from anotador.Visual.ui_WNotas_Destacadas import Ui_WNotas_Destacadas


class WNotas_Destacadas(QWidget):
    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.ui = Ui_WNotas_Destacadas()
        self.ui.setupUi(self)
        self._configurar()
        self.anotador = parent.anotador
    def _configurar(self):
        self.ui.listViewNotas.setModel(QStandardItemModel())
        self.ui.listViewNotas.selectionModel().selectionChanged.connect(self.selecionar)
        self.ui.pushButton_Ver_Nota.clicked.connect(self.ver_nota)
        self.ui.pushButton_Home.clicked.connect(self.cambiar_ventana_principal)
        self.ui.pushButtonBuscar.clicked.connect(self.buscar_destacados)
        self.ui.pushButton_Buscar_Nota.clicked.connect(self.cambiar_ventana_buscador)
        self.ui.pushButton_Informe_Etiqueta.clicked.connect(self.cambiar_ventana_informe)
    def cambiar_ventana_informe(self):
        self.parent().parent().informe_screen.ui.listViewNotas.model().clear()
        self.parent().parent().informe_screen.ui.lineEditEtiqueta.setText("")
        self.parent().parent().informe_screen.ui.label_cantidad_notas_valor.setText("")
        self.parent().setCurrentWidget(self.parent().parent().informe_screen)
    def cambiar_ventana_buscador(self):
        self.parent().parent().buscador_screen.ui.listViewNotas.model().clear()
        self.parent().parent().buscador_screen.ui.lineEditEtiqueta.setText("")
        self.parent().setCurrentWidget(self.parent().parent().buscador_screen)
    def buscar_destacados(self):
        try:
           lista_notas=self.anotador.listadestacados()
        except NoElementFound:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("ERROR EXISTENCIAL")
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(f"No fue encontrada ninguna nota destacada")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
        else:
            self.ui.listViewNotas.model().clear()
            for tupla in lista_notas:
                nota,lista_ruta=tupla
                display=f"{lista_ruta[0].nombre}/{lista_ruta[1].nombre}/{lista_ruta[2].nombre}/{str(nota)}"
                item = QStandardItem(display)
                item.setEditable(False)
                item.nota=nota
                item.ruta=lista_ruta
                self.ui.listViewNotas.model().appendRow(item)
    def cambiar_ventana_principal(self):
        self.parent().setCurrentWidget(
            self.parent().parent().start_screen)
    def ver_nota(self):
        self.actualizarSelecion()
        self.parent().setCurrentWidget(
            self.parent().parent().nota_actual_screen)
    def selecionar(self,selected,deselected):
        indices=selected.indexes()
        if len(indices) > 0:
            self.ui.pushButton_Ver_Nota.setEnabled(True)
        else:
            self.ui.pushButton_Ver_Nota.setEnabled(False)
    def actualizarSelecion(self):
        indice = self.ui.listViewNotas.selectedIndexes()[0]
        nota = self.ui.listViewNotas.model().itemFromIndex(indice).nota
        ruta=self.ui.listViewNotas.model().itemFromIndex(indice).ruta
        libro,seccion,pagina=ruta
        self.parent().parent().actualizar_secciones_pantalla(libro)
        self.parent().parent().actualizar_paginas_pantalla(seccion)
        self.parent().parent().actualizar_notas_pantalla(pagina)
        self.parent().parent().actualizar_nota_actual(nota)

