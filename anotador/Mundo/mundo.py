import time
class Nota:

    def __init__(self, nombre:str, etiqueta:str):

        self.fecha_creacion = time.strftime("%Y-%m-%d", time.localtime())

        self.hora_creacion = time.strftime("%H-%M:%S", time.localtime())

        self.nombre = nombre

        self.contenido = ""

        self.etiquetas = [etiqueta]

        self.destacado = False
class Pagina:

    def __init__(self, nombre:str):

        self.nombre= nombre

        self.fecha_creacion = time.strftime("%Y-%m-%d", time.localtime())

        self.notas={}
class Seccion:

    def __init__(self, nombre:str):

        self.nombre= nombre

        self.fecha_creacion = time.strftime("%Y-%m-%d", time.localtime())

        self.paginas={}

class Libro:

    def __init__(self, nombre:str):

        self.nombre= nombre

        self.fecha_creacion = time.strftime("%Y-%m-%d", time.localtime())

        self.secciones = {}

class Anotador:

    def __init__(self):

        self.libros={}

    def libro_existe(self, nombre):
        """Funcion para determinar si el libro existe, regresa True si se encuentra en el diccionario, False si no"""
        llaves= self.libros.keys()
        valor= nombre in llaves
        return valor

    def agregar_libro(self, nombre:str):
        if not self.libro_existe(nombre):
            self.libros[nombre]=Libro(nombre)
    def seccion_existe(self, nombrelibro, nombreseccion:str):
        """Funcion para determinar si la seccion existe, regresa True si se encuentra en el diccionario, False si no"""
        if self.libro_existe(nombrelibro):
            libro=self.libros[nombrelibro]
            llaves=libro.secciones.keys()
            valor=nombreseccion in llaves
            return valor
    def agregar_seccion(self, nombrelibro:str, nombreseccion:str):

        if not self.seccion_existe(nombrelibro, nombreseccion):
            libro= self.libros[nombrelibro]
            libro.secciones[nombreseccion]=Seccion(nombreseccion)

    def pagina_existe(self, nombrelibro:str, nombreseccion: str, nombrepagina:str):
        """Funcion para determinar si la pagina existe, regresa True si se encuentra en el diccionario, False si no"""
        if self.seccion_existe(nombrelibro, nombreseccion):
            libro = self.libros[nombrelibro]
            seccion = libro.secciones[nombreseccion]
            llaves=seccion.paginas.keys
            valor=nombrepagina in llaves
            return  valor
    def agregar_pagina(self, nombrelibro:str, nombreseccion: str, nombrepagina:str):

        if not self.pagina_existe(nombrelibro, nombreseccion, nombrepagina):
            libro = self.libros[nombrelibro]
            seccion=libro.secciones[nombreseccion]
            seccion.paginas[nombrepagina]=Pagina(nombrepagina)

    def nota_existe(self, nombrelibro:str, nombreseccion: str, nombrepagina:str, nombrenota:str):
        """Funcion para determinar si la nota existe, regresa True si se encuentra en el diccionario, False si no"""
        if self.pagina_existe(nombrelibro, nombreseccion, nombrepagina):
            libro = self.libros[nombrelibro]
            seccion = libro.secciones[nombreseccion]
            pagina=seccion.paginas[nombrepagina]
            llaves=pagina.notas.keys
            valor=nombrenota in llaves
            return valor
    def agregar_nota(self, nombrelibro:str, nombreseccion: str, nombrepagina:str, nombrenota:str, etiqueta):

        if not self.nota_existe(nombrelibro, nombreseccion, nombrepagina, nombrenota):
            libro = self.libros[nombrelibro]
            seccion=libro.secciones[nombreseccion]
            pagina=seccion.paginas[nombrepagina]
            pagina.notas[nombrenota]=Nota(nombrenota, etiqueta)
    def etiqueta_existe(self, nombrelibro:str, nombreseccion: str, nombrepagina:str, nombrenota:str, etiqueta):
        """Funcion para determinar si la etiqueta existe, regresa True si se encuentra en el diccionario, False si no"""
        if self.nota_existe(nombrelibro, nombreseccion, nombrepagina, nombrenota):
            libro = self.libros[nombrelibro]
            seccion = libro.secciones[nombreseccion]
            pagina=seccion.paginas[nombrepagina]
            nota=pagina.notas[nombrenota]
            valor=etiqueta in nota.etiquetas
            return  valor
    def agregar_etiqueta(self, nombrelibro:str, nombreseccion: str, nombrepagina:str, nombrenota:str, etiqueta:str):
        if not self.etiqueta_existe(nombrelibro, nombreseccion, nombrepagina, nombrenota, etiqueta):
            libro = self.libros[nombrelibro]
            seccion=libro.secciones[nombreseccion]
            pagina=seccion.paginas[nombrepagina]
            nota=pagina.notas[nombrenota]
            nota.etiquetas.append(etiqueta)
    def destacar_nota(self, nombrelibro:str, nombreseccion: str, nombrepagina:str, nombrenota:str):
        if self.nota_existe(nombrelibro, nombreseccion, nombrepagina, nombrenota):
            libro = self.libros[nombrelibro]
            seccion = libro.secciones[nombreseccion]
            pagina = seccion.paginas[nombrepagina]
            nota = pagina.notas[nombrenota]
            nota.destacado=True
    def listadestacados(self):
        """Funcion que guarda las llaves de las notas destacadas"""
        destacados= []
        libros=self.libros
        for librokey in libros.keys():#iterar los libros del anotador
            libro=libros[librokey]
            secciones=libro.secciones
            for secckey in secciones.keys():#iterar las secciones de un libro
                seccion=secciones[secckey]
                paginas=seccion.paginas
                for pagkey in paginas.keys():#iterar las paginas de una seccion
                    pagina=paginas[pagkey]
                    notas=pagina.notas
                    for notakey in notas.keys():#iterar las notas de una pagina
                        nota=notas[notakey]
                        if nota.destacado:#si la nota esta destacada, se agrega a la lista
                            destacados.append(notakey)
        return destacados# se devuelve lista con los nombres de las notas destacadas
    def  informe_etiquetas(self, xetiqueta:str):
        """Funcion que cuenta la cantidad de veces que una nota tiene xetiqueta y las notas donde esta"""
        lista = []#lista donde se guardara las notas donde se encuentre la etiqueta
        contador=0#contador de de la etiqueta
        libros = self.libros
        for librokey in libros.keys():  # iterar los libros del anotador
            libro = libros[librokey]
            secciones = libro.secciones
            for secckey in secciones.keys():  # iterar las secciones de un libro
                seccion = secciones[secckey]
                paginas = seccion.paginas
                for pagkey in paginas.keys():  # iterar las paginas de una seccion
                    pagina = paginas[pagkey]
                    notas = pagina.notas
                    for notakey in notas.keys():  # iterar las notas de una pagina
                        nota = notas[notakey]
                        etiquetas=nota.etiquetas
                        if xetiqueta in etiquetas:
                            contador+=1
                            lista.append(notakey)
        return (contador,lista)  # se devuelve tupla con el contador y la lista de notas



