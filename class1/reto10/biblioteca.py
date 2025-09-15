
class biblioteca:

    total = 0

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        biblioteca.total += 1

    def mostrar_info(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Paginas: {self.paginas}"
    
    @staticmethod
    def es_grande(paginas):
        if paginas > 300:
            return True
        else:
            return False
        
    @classmethod
    def total_libros(cls):
        return cls.total