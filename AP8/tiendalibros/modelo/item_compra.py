from tiendalibros.modelo.libro import Libro

class ItemCompra:
    def __init__(self,libro:Libro,cantidad:int):
        self.libro:Libro=libro
        self.cantidad:int=cantidad

    def calcular_subtotal(self):
        subtotal=self.cantidad*self.libro.precio
        return subtotal
    
