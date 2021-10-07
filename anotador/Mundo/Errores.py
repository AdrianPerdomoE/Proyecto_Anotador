class ErrorAnotador(Exception):
    pass
class LibroExiste(ErrorAnotador):
    def __init__(self):
        self.msg="Libro ya existe en el anotador"