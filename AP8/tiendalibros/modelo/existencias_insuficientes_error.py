from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):
    def __init__(self,cantidad_a_comprar:int):
        super().__init__()
        self.cantidad_a_comprar:int = cantidad_a_comprar

    def __str__(self):
        return f"El libro con titulo {self.titulo} y isbn {self.isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.existencias}"
