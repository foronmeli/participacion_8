from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"El libro con titulo {self.libro.titulo} y isbn: {self.isbn} ya existe en el catálogo"
