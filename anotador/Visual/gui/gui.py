import sys

from PySide2.QtWidgets import QMainWindow, QApplication, QStackedWidget
from anotador.Mundo.mundo import *
from anotador.Visual.gui.wSecciones import Secciones
from anotador.Visual.gui.wprincipal import principal


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
    def actualizar_tercera_pantalla(self,seccion):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ventana()
    sys.exit(app.exec_())
