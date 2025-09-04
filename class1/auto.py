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
        

mi_auto = auto("Toyota","Corolla",2023)

print(mi_auto.mostrar_info())
mi_auto.actualizar_kilometraje(15000)
print(mi_auto.kilometraje)
mi_auto.realizar_viaje(300)
print(mi_auto.kilometraje)
print(mi_auto.estado_auto())