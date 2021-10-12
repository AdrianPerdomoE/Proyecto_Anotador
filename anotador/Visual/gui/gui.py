import sys

from PySide2.QtWidgets import QMainWindow, QApplication, QStackedWidget
from anotador.Mundo.mundo import *
from anotador.Visual.gui.WLibro import  WLibro
from anotador.Visual.gui.WNota import WNota
from anotador.Visual.gui.wPagina import WPagina
from anotador.Visual.gui.WSeccion import WSeccion
from anotador.Visual.gui.wprincipal import principal


class ventana(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.anotador=Anotador()
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.start_screen =principal(self)
        self.central_widget.addWidget(self.start_screen)
        self.secciones_screen = WLibro(self)
        self.paginas_screen= WSeccion(self)
        self.notas_screen=WPagina(self)
        self.nota_actual_screen=WNota(self)
        self.central_widget.addWidget(self.start_screen)
        self.central_widget.addWidget(self.secciones_screen)
        self.central_widget.addWidget(self.paginas_screen)
        self.central_widget.addWidget(self.nota_actual_screen)
        self.central_widget.addWidget(self.notas_screen)
        self.central_widget.setCurrentWidget(self.start_screen)
        self.anotador = Anotador()
        self.show()
    def actualizar_secciones_pantalla(self,libro):
        self.secciones_screen= WLibro(self, libro)
        self.secciones_screen.actualizar_listasecciones()
        self.central_widget.addWidget(self.secciones_screen)
    def actualizar_paginas_pantalla(self,seccion):
        self.paginas_screen = WSeccion(self, seccion)
        self.paginas_screen.actualizar_listapaginas()
        self.central_widget.addWidget(self.paginas_screen)
    def actualizar_notas_pantalla(self,pagina):
        self.notas_screen=WPagina(self, pagina)
        self.notas_screen.actualizar_listanotas()
        self.central_widget.addWidget(self.notas_screen)
    def actualizar_nota_actual(self,nota):
        self.nota_actual_screen = WNota(self, nota)
        self.nota_actual_screen.actualizar_listaetiquetas()
        if nota.contenido!="":
            self.nota_actual_screen.ui.plainTextEditContenido.setPlainText(nota.contenido)
        if self.nota_actual_screen.nota.destacado:
            self.nota_actual_screen.ui.pushButtonDestacar.setText("Desmarcar")
        self.central_widget.addWidget(self.nota_actual_screen)
    def actualizar_botones_busquedas(self,boolean):
        self.start_screen.ui.pushButton_Buscar_Nota.setEnabled(boolean)
        self.start_screen.ui.pushButton_Notas_Destacadas.setEnabled(boolean)
        self.start_screen.ui.pushButton_Informe_Etiqueta.setEnabled(boolean)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = ventana()
    window.setWindowTitle("Anotador")
    window.setMinimumSize(1020,600)
    sys.exit(app.exec_())
