import sys

from PySide2.QtWidgets import QMainWindow, QApplication, QStackedWidget
from anotador.Mundo.mundo import *
from anotador.Visual.gui.wSecciones import  WSeccion
from anotador.Visual.gui.wnotas import WNota
from anotador.Visual.gui.wpaginas import WPagina
from anotador.Visual.gui.wprincipal import principal


class ventana(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.anotador=Anotador()
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.start_screen = principal(self)
        self.central_widget.addWidget(self.start_screen)
        self.secciones_screen = WSeccion(self)
        self.paginas_screen= WPagina(self)
        self.notas_screen=WNota(self)
        #self.nota_actual_screen=
        self.central_widget.addWidget(self.start_screen)
        self.central_widget.addWidget(self.secciones_screen)
        self.central_widget.addWidget(self.paginas_screen)
        #self.central_widget.addWidget(self.nota_actual_screen)
        self.central_widget.addWidget(self.notas_screen)
        self.central_widget.setCurrentWidget(self.start_screen)
        self.anotador = Anotador()
        self.show()
    def actualizar_secciones_pantalla(self,libro):
        self.secciones_screen= WSeccion(self,libro)
        self.secciones_screen.actualizar_listasecciones()
        self.central_widget.addWidget(self.secciones_screen)
    def actualizar_paginas_pantalla(self,seccion):
        self.paginas_screen = WPagina(self, seccion)
        self.paginas_screen.actualizar_listapaginas()
        self.central_widget.addWidget(self.paginas_screen)
    def actualizar_notas_pantalla(self,pagina):
        self.notas_screen=WNota(self,pagina)
        self.notas_screen.actualizar_listanotas()
        self.central_widget.addWidget(self.notas_screen)
    def actualizar_nota_actual(self,nota):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ventana()
    sys.exit(app.exec_())
