import pickle
import time
import os
from anotador.Mundo.Errores import LibroExiste, SeccionExiste, PaginaExiste, NotaExiste, EtiquetaExiste, NoElementFound


class Nota:

    def __init__(self, nombre:str, etiqueta=None):

        self.fecha_creacion = time.strftime("%d/%m/%Y", time.localtime())

        self.hora_creacion = time.strftime("%H:%M:%S", time.localtime())

        self.nombre = nombre

        self.contenido = ""

        self.etiquetas=[]
        if etiqueta != None:
            self.etiquetas.append(etiqueta)
        self.destacado = False
    def __str__(self):#sobreescribimos la funcion de str para manipular como mostramos el texto en el listview
        if self.destacado:
            return (f"★ {self.nombre}_ _ _{self.fecha_creacion}:  {self.hora_creacion}")
        return (f"{self.nombre}_ _ _{self.fecha_creacion}:  {self.hora_creacion}")

    def etiqueta_existe(self, etiqueta):#Funcion para determinar si una etiqueta ya existe y levantar el error
        """Funcion para determinar si la etiqueta existe, regresa True si se encuentra en el diccionario, False si no"""
        valor=etiqueta in self.etiquetas
        if  valor:
            raise EtiquetaExiste
    def agregar_etiqueta(self,  etiqueta:str):
        self.etiqueta_existe(etiqueta)
        self.etiquetas.append(etiqueta)
    def eliminiar_etiqueta(self,  etiqueta:str):
        indice=self.etiquetas.index(etiqueta)
        self.etiquetas.pop(indice)
    def destacar_nota(self,Boolean:bool):
        self.destacado=Boolean
class Pagina:

    def __init__(self, nombre:str):

        self.nombre= nombre

        self.fecha_creacion = time.strftime("%d/%m/%Y", time.localtime())

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
    def borrar_nota(self,nombrepagina):
        self.notas.pop(nombrepagina)
class Seccion:

    def __init__(self, nombre:str):

        self.nombre= nombre

        self.fecha_creacion = time.strftime("%d/%m/%Y", time.localtime())

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

        self.fecha_creacion = time.strftime("%d/%m/%Y", time.localtime())

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
    def save(self,archivo):#Funcion para guargar los cambios hechos en la aplicación
        with open(archivo,"wb") as f:
            pickle.dump(self,f)

    def load(self,archivo):#Funcion para cargar el documento que contenga el anotador guardado, si no existe, se crea, si esta vacio, se salta la funcion
        try:
            with open(archivo,"rb") as f:
                if os.path.exists(archivo) and os.path.getsize(archivo) > 0:
                    dato=pickle.load(f)
                    self.libros=dato.libros
                else:
                    return

        except FileNotFoundError:
            with open(archivo,"x") as f:
                return
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
    def listadestacados(self):
        """Funcion que guarda las llaves de las notas destacadas"""
        lista_notas_destacadas= []
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
                            lista_notas_destacadas.append((nota, [libro, seccion, pagina]))
        if len(lista_notas_destacadas) == 0:
            raise NoElementFound()
        return lista_notas_destacadas# se devuelve lista con los nombres de las notas destacadas
    def  informe_etiquetas(self, xetiqueta:str):
        """Funcion que cuenta la cantidad de veces que una nota tiene xetiqueta y las notas donde esta"""
        lista_notas = []#lista donde se guardara las notas donde se encuentre la etiqueta
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
                        if len(nota.etiquetas)!=0:
                            etiquetas=nota.etiquetas
                            if xetiqueta in etiquetas:
                                contador+=1
                                lista_notas.append((nota,[libro,seccion,pagina]))#se agrega a la lista tupla con el objeto nota y una lista de la ruta donde estaba
        if len(lista_notas) == 0:
            raise NoElementFound()
        return (contador,lista_notas)  # se devuelve tupla con el contador y la lista de notas
    def busqueda_por_etiqueta(self,etiqueta):
        lista_notas =[]
        libros = self.libros
        for librokey in libros.keys():
            libro = libros[librokey]
            secciones = libro.secciones
            for secckey in secciones.keys():
                seccion = secciones[secckey]
                paginas = seccion.paginas
                for pagkey in paginas.keys():
                    pagina = paginas[pagkey]
                    notas = pagina.notas
                    for notakey in notas.keys():
                        nota = notas[notakey]
                        if len(nota.etiquetas)!=0:
                            etiquetas = nota.etiquetas
                            if etiqueta in etiquetas:
                                lista_notas.append((nota,[libro,seccion,pagina]))#regreso lista de tuplas con(nota,ruta)
        if len(lista_notas)==0:
            raise NoElementFound()
        return lista_notas
    def busqueda_por_fecha(self, fecha):
        lista_notas = []
        libros = self.libros
        for librokey in libros.keys():
            libro = libros[librokey]
            secciones = libro.secciones
            for secckey in secciones.keys():
                seccion = secciones[secckey]
                paginas = seccion.paginas
                for pagkey in paginas.keys():
                    pagina = paginas[pagkey]
                    notas = pagina.notas
                    for notakey in notas.keys():
                        nota = notas[notakey]
                        if fecha ==nota.fecha_creacion:
                            lista_notas.append((nota, [libro, seccion, pagina]))  # regreso lista de tuplas con(nota,ruta)
        if len(lista_notas)==0:
            raise NoElementFound()
        return lista_notas
