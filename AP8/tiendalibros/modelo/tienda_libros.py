from tiendalibros.modelo.libro_existente_error import LibroExistenteError
from tiendalibros.modelo.carro_compra import CarroCompras
from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.libro_error import LibroError
from tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError

class TiendaLibros:
    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompras()

    def adicionar_libro_a_catalogo(self, isbn:str, titulo:str, precio:float, existencias:int):
        if isbn in self.catalogo:
            raise LibroExistenteError(isbn)

        libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = libro
        return libro
    
    def agregar_libro_a_carrito(self, libro, cantidad):
        if libro.isbn not in self.catalogo:
            raise LibroError(f"El libro con isbn: {libro.isbn} no existe en el catálogo")

        libro_existente = self.catalogo[libro.isbn]

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        if libro_existente.existencias == 0:
            raise LibroAgotadoError(libro_existente.titulo, libro_existente.isbn)

        if cantidad > libro_existente.existencias:
            raise ExistenciasInsuficientesError(libro_existente.titulo, libro_existente.isbn, cantidad, libro_existente.existencias)

        self.carrito.agregar_item(libro, cantidad)

    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)
