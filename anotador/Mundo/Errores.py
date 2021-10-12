class ErrorAnotador(Exception):
    pass
class LibroExiste(ErrorAnotador):
    def __init__(self):
        self.msg="Libro ya existe en el anotador"
class SeccionExiste(ErrorAnotador):
    pass
class PaginaExiste(ErrorAnotador):
    pass
class NotaExiste(ErrorAnotador):
    pass
class EtiquetaExiste(ErrorAnotador):
    pass