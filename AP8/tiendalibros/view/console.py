import sys
from tiendalibros.modelo.libro_error import LibroError
from tiendalibros.modelo.tienda_libros import TiendaLibros


class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    def retirar_libro_de_carrito_de_compras(self, tienda_libros):
        isbn = input("Ingrese el ISBN del libro que desea retirar del carrito: ")
        tienda_libros.retirar_item_de_carrito(isbn)
        print("Libro retirado con éxito.")

    def agregar_libro_a_carrito_de_compras(self, tienda_libros):
        isbn = str(input("Ingrese el ISBN del libro que desea agregar al carrito: "))
        cantidad = int(input("Ingrese la cantidad de unidades que desea comprar: "))
        try:
            libro = tienda_libros.catalogo.get(isbn)
            if libro:
                tienda_libros.agregar_libro_a_carrito(libro, cantidad)
                print("Libro agregado con éxito.")
            else:
                print("El libro con ISBN no existe en el catálogo.")
        except LibroError as e:
            print(f"Error: {e}")

    def adicionar_un_libro_a_catalogo(self, tienda_libros):
        isbn = str(input("Ingrese el ISBN del libro: "))
        titulo = str(input("Ingrese el título del libro: "))
        precio = float(input("Ingrese el precio del libro: "))
        existencias = int(input("Ingrese la cantidad de existencias del libro: "))
        try:
            tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
            print("Libro agregado con éxito.")
        except LibroError as e:
            print(f"Error: {e}")
        except ValueError as ve:
            print(f"Error: {ve}")
