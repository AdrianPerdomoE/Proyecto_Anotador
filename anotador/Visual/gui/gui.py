from PySide2.QtWidgets import QMainWindow, QStackedWidget
from anotador.Visual.gui.WInforme import WInforme_Etiqueta
from anotador.Visual.gui.WLibro import WLibro
from anotador.Visual.gui.WNota import WNota
from anotador.Visual.gui.WNotas_Destacadas import WNotas_Destacadas
from anotador.Visual.gui.WSeccion import WSeccion
from anotador.Visual.gui.Wbuscador import WBuscador
from anotador.Visual.gui.wPagina import WPagina
from anotador.Visual.gui.wprincipal import principal


class Ventana(QMainWindow):#ventana donde se muestra los widgets
    ARCHIVO="Datos.Anotador"
    def __init__(self,anotador,parent=None):
        QMainWindow.__init__(self,parent)
        self.anotador=anotador#Guardamos el anotador en un atrubito
        self.anotador.load(Ventana.ARCHIVO)#al iniciar la aplicacion pedimos cargar datos del anotador
        self.central_widget = QStackedWidget()#vamos a utilizar QStackedWidget que nos permitira tener varios widgets guardados y poder cambiar entre escenas
        self.setCentralWidget(self.central_widget)
        self.start_screen =principal(self)#Donde guardamos la escena inicial del anotador
        self.central_widget.addWidget(self.start_screen)#Guardamos el widget en el stack
        self.secciones_screen = WLibro(self)#la escena que se ve en un libro
        self.paginas_screen= WSeccion(self)#La escena que se ve en una seccion
        self.notas_screen=WPagina(self)#La escena que se ve en una pagina
        self.nota_actual_screen=WNota(self)#La escena que se ve en una nota
        self.buscador_screen=WBuscador(self)#la escena donde buscamos una nota
        self.informe_screen=WInforme_Etiqueta(self)#La escena donde miramos el informe de etiquetas
        self.notas_destacadas_screen=WNotas_Destacadas(self)#La escena donde vemos las notas destacadas
        self.central_widget.addWidget(self.buscador_screen)
        self.central_widget.addWidget(self.start_screen)
        self.central_widget.addWidget(self.secciones_screen)
        self.central_widget.addWidget(self.paginas_screen)
        self.central_widget.addWidget(self.nota_actual_screen)
        self.central_widget.addWidget(self.notas_screen)
        self.central_widget.addWidget( self.informe_screen)
        self.central_widget.addWidget(self.notas_destacadas_screen)
        self.central_widget.setCurrentWidget(self.start_screen)
        self.show()
        self.closeEvent=self.cerrar_ventana#conectamos el evento de cerrado con guardar los datos.
    def cerrar_ventana(self,event):
        self.anotador.save(Ventana.ARCHIVO)
    def actualizar_secciones_pantalla(self,libro):#Funcion para actualizar el libro que estamos viendo en la escena
        self.central_widget.removeWidget( self.secciones_screen)#Eliminamos el anterior para evitar conflictos
        self.secciones_screen= WLibro(self, libro)
        self.secciones_screen.actualizar_listasecciones()
        self.central_widget.addWidget(self.secciones_screen)
    def actualizar_paginas_pantalla(self,seccion):#Funcion para actualizar la seccion que estamos viendo en la escena
        self.central_widget.removeWidget(self.paginas_screen)
        self.paginas_screen = WSeccion(self, seccion)
        self.paginas_screen.actualizar_listapaginas()
        self.central_widget.addWidget(self.paginas_screen)
    def actualizar_notas_pantalla(self,pagina):#Funcion para actualizar la pagina que estamos viendo en la escena
        self.central_widget.removeWidget(self.notas_screen)
        self.notas_screen=WPagina(self, pagina)
        self.notas_screen.actualizar_listanotas()
        self.central_widget.addWidget(self.notas_screen)
    def actualizar_nota_actual(self,nota):#Funcion para actualizar la nota que estamos viendo en la escena
        self.central_widget.removeWidget(self.nota_actual_screen)
        self.nota_actual_screen = WNota(self, nota)
        self.nota_actual_screen.actualizar_listaetiquetas()
        if nota.contenido!="":
            self.nota_actual_screen.ui.plainTextEditContenido.setPlainText(nota.contenido)
        if self.nota_actual_screen.nota.destacado:
            self.nota_actual_screen.ui.pushButtonDestacar.setText("Desmarcar")
        self.central_widget.addWidget(self.nota_actual_screen)