from tiendalibros.modelo.item_compra import ItemCompra

class CarroCompras:
    def __init__(self):
        self.item:list=[]

    def agregar_item(self,libro,cantidad_unidades):
        self.libro=libro
        self.cantidad_unidades=cantidad_unidades
        objeto=ItemCompra(self.libro,self.cantidad_unidades)
        self.item.append(objeto)
        return objeto
    
    def calcular_total(self):
        for i in self.item:
            total=total+i
        return total
    
    def quitar_item(self,isbn):
        self.item=[item for item in self.item if item.libro.isbn!=isbn]
