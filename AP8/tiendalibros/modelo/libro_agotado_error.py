from tiendalibros.modelo.libro_error import LibroError


class LibroAgotadoError(LibroError):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"El libro con titulo {self.titulo} y isbn {self.isbn} está agotado"
