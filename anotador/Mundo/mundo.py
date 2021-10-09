import time

from anotador.Mundo.Errores import LibroExiste, SeccionExiste, PaginaExiste, NotaExiste


class Nota:

    def __init__(self, nombre:str, etiqueta=None):

        self.fecha_creacion = time.strftime("%Y-%m-%d", time.localtime())

        self.hora_creacion = time.strftime("%H-%M:%S", time.localtime())

        self.nombre = nombre

        self.contenido = ""

        self.etiquetas=[]
        if etiqueta != None:
            self.etiquetas.append(etiqueta)
        self.destacado = False
    def __str__(self):
        return (f"{self.nombre}_ _ _{self.fecha_creacion}:  {self.hora_creacion}")
class Pagina:

    def __init__(self, nombre:str):

        self.nombre= nombre

        self.fecha_creacion = time.strftime("%Y-%m-%d", time.localtime())

        self.notas={}
    def __str__(self):
        return (f"{self.nombre}_ _ _{self.fecha_creacion}")
    def nota_existe(self, nombrenota:str):
        """Funcion para determinar si la nota existe, regresa True si se encuentra en el diccionario, False si no"""
        llaves=self.notas.keys()
        valor=nombrenota in llaves
        if valor:
            raise NotaExiste()
    def agregar_nota(self,nombrenota:str, etiqueta=None):

       self.nota_existe(nombrenota)
       self.notas[nombrenota]=Nota(nombrenota, etiqueta)
    def modificar_nombre_nota(self,nombrenota: str, nuevo):
        self.nota_existe(nuevo)
        antiguo=self.notas.pop(nombrenota)
        antiguo.nombre=nuevo
        self.notas[nuevo]=antiguo
    def modificar_etiqueta_nota(self,nombrenota: str,etiqueta,borrar=False,agregar=False):#posiblemente se implemente en la nota
        lista_etiquetas=self.notas[nombrenota]
        if borrar:
            lista_etiquetas.pop(etiqueta)
        elif agregar:
            lista_etiquetas.append(etiqueta)
    def borrar_nota(self,nombrepagina):
        self.notas.pop(nombrepagina)
class Seccion:

    def __init__(self, nombre:str):

        self.nombre= nombre

        self.fecha_creacion = time.strftime("%Y-%m-%d", time.localtime())

        self.paginas={}
    def __str__(self):
        return (f"{self.nombre}_ _ _{self.fecha_creacion}")

    def pagina_existe(self,nombrepagina: str):
        """Funcion para determinar si la pagina existe, regresa True si se encuentra en el diccionario, False si no"""
        llaves = self.paginas.keys()
        valor = nombrepagina in llaves
        if valor:
         raise  PaginaExiste()

    def agregar_pagina(self, nombrepagina: str):
        self.pagina_existe(nombrepagina)
        self.paginas[nombrepagina] = Pagina(nombrepagina)
    def modificar_pagina(self,nombrepagina: str, nuevo):
        self.pagina_existe(nuevo)
        antiguo=self.paginas.pop(nombrepagina)
        antiguo.nombre=nuevo
        self.paginas[nuevo]=antiguo
    def borrar_pagina(self,nombrepagina):
        self.paginas.pop(nombrepagina)
class Libro:

    def __init__(self, nombre:str):

        self.nombre= nombre

        self.fecha_creacion = time.strftime("%Y-%m-%d", time.localtime())

        self.secciones = {}
    def __str__(self):
        return (f"{self.nombre}_ _ _{self.fecha_creacion}")

    def seccion_existe(self,nombreseccion: str):
        """Funcion para determinar si la seccion existe, regresa True si se encuentra en el diccionario, False si no"""
        llaves = self.secciones.keys()
        valor = nombreseccion in llaves
        if  valor:
            raise SeccionExiste
    def agregar_seccion(self, nombreseccion: str):

        self.seccion_existe(nombreseccion)
        self.secciones[nombreseccion] = Seccion(nombreseccion)
    def borrar_seccion(self,nombre_seccion):
        self.secciones.pop(nombre_seccion)
    def modificar_seccion(self,antiguo,nuevo):
        self.seccion_existe(nuevo)
        pasado=self.secciones.pop(antiguo)
        pasado.nombre=nuevo
        self.secciones[nuevo]=pasado
class Anotador:

    def __init__(self):

        self.libros={}

    def libro_existe(self, nombre):
        """Funcion para determinar si el libro existe, regresa True si se encuentra en el diccionario, False si no"""
        llaves= self.libros.keys()
        valor= nombre in llaves
        if valor:
             raise LibroExiste()
    def agregar_libro(self, nombre:str):
           self.libro_existe(nombre)
           self.libros[nombre] = Libro(nombre)
    def borrar_libro(self,titulo):
        self.libros.pop(titulo)
    def modificar_libro(self,titulo,nuevo):
        self.libro_existe(nuevo)
        antiguo=self.libros.pop(titulo)
        antiguo.nombre=nuevo
        self.libros[nuevo]=antiguo

    def etiqueta_existe(self, nombrelibro:str, nombreseccion: str, nombrepagina:str, nombrenota:str, etiqueta):
        """Funcion para determinar si la etiqueta existe, regresa True si se encuentra en el diccionario, False si no"""
        if self.nota_existe(nombrelibro, nombreseccion, nombrepagina, nombrenota):
            libro = self.libros[nombrelibro]
            seccion = libro.secciones[nombreseccion]
            pagina=seccion.paginas[nombrepagina]
            nota=pagina.notas[nombrenota]
            valor=etiqueta in nota.etiquetas
            return  valor
        pass
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