from vehiculos import vehiculos

class auto(vehiculos):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas

    def descripcion(self):
        return f"{super().descripcion()}, Número de puertas: {self.num_puertas}"