
class vehiculos:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def descripcion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}"
    
    
