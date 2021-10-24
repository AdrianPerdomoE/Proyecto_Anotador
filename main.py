import sys
from PySide2.QtWidgets import QApplication
from anotador.Visual.gui.gui import Ventana
from anotador.Mundo.mundo import Anotador
if __name__ == "__main__":
    anotador=Anotador()
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = Ventana(anotador)
    window.setWindowTitle("Anotador")
    window.setMinimumSize(1020,600)
    sys.exit(app.exec_())


