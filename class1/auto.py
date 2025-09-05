class auto:
    def __init__(self, marca,modelo,año,kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
    
    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"
    
    def actualizar_kilometraje(self,nuevo_kilometraje):
        if nuevo_kilometraje >= self.kilometraje:
            self.kilometraje = nuevo_kilometraje
        else:
            print("No se puede reducir el kilometraje")
    
    def realizar_viaje(self,distancia):
        if distancia > 0:
            self.kilometraje += distancia
        else:
            print("La distancia debe ser positiva")

    def estado_auto(self):
        if self.kilometraje < 20000:
            return "Estoy como nuevo"
        elif 20000 <= self.kilometraje < 100000:
            return "Ya estoy usado"
        else:
            return "¡Ya dejenme descansar por favor!"
    
    @classmethod
    def auto_toyota(cls,modelo):
        marca = "Toyota"
        kilometraje = 0
        año = 2025
        return cls(marca,modelo,año,kilometraje)
        
    @staticmethod
    def comparar_kilometraje(auto1,auto2):
        if auto1.kilometraje == auto2.kilometraje:
            return "Los kilometrajes son iguales"
        return "Los kilometrajes son diferentes"
    
    @classmethod
    def auto_ford(cls,modelo,año):
        marca = "Ford"
        kilometraje = 0
        return cls(marca,modelo,año,kilometraje)
    
    @staticmethod
    def es_nuevo(auto):
        if auto.kilometraje == 0:
            return "El auto es nuevo"

