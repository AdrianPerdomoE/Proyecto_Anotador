import sys

from PySide2.QtWidgets import QMainWindow, QApplication, QStackedWidget
from anotador.Mundo.mundo import *
from anotador.Visual.gui.WInforme import WInforme_Etiqueta
from anotador.Visual.gui.WLibro import  WLibro
from anotador.Visual.gui.WNota import WNota
from anotador.Visual.gui.WNotas_Destacadas import WNotas_Destacadas
from anotador.Visual.gui.Wbuscador import WBuscador
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
        self.buscador_screen=WBuscador(self)
        self.informe_screen=WInforme_Etiqueta(self)
        self.notas_destacadas_screen=WNotas_Destacadas(self)
        self.central_widget.addWidget(self.buscador_screen)
        self.central_widget.addWidget(self.start_screen)
        self.central_widget.addWidget(self.secciones_screen)
        self.central_widget.addWidget(self.paginas_screen)
        self.central_widget.addWidget(self.nota_actual_screen)
        self.central_widget.addWidget(self.notas_screen)
        self.central_widget.addWidget( self.informe_screen)
        self.central_widget.addWidget(self.notas_destacadas_screen)
        self.central_widget.setCurrentWidget(self.start_screen)
        self.anotador = Anotador()
        self.show()
    def actualizar_secciones_pantalla(self,libro):
        self.central_widget.removeWidget( self.secciones_screen)
        self.secciones_screen= WLibro(self, libro)
        self.secciones_screen.actualizar_listasecciones()
        self.central_widget.addWidget(self.secciones_screen)
    def actualizar_paginas_pantalla(self,seccion):
        self.central_widget.removeWidget(self.paginas_screen)
        self.paginas_screen = WSeccion(self, seccion)
        self.paginas_screen.actualizar_listapaginas()
        self.central_widget.addWidget(self.paginas_screen)
    def actualizar_notas_pantalla(self,pagina):
        self.central_widget.removeWidget(self.notas_screen)
        self.notas_screen=WPagina(self, pagina)
        self.notas_screen.actualizar_listanotas()
        self.central_widget.addWidget(self.notas_screen)
    def actualizar_nota_actual(self,nota):
        self.central_widget.removeWidget(self.nota_actual_screen)
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
