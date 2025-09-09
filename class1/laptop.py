

import random


class Laptop:
    def __init__(self, marca, procesador, memoria, costo = 500,impuesto = 10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuesto = impuesto

    def valor_final(self):
        return self.costo + self.impuesto
    
    def valor_descuento(self,descuento):
        return (self.costo * descuento)/100
    
    def realizar_diagnostico_sistema(self):
        resultado = {
            "Marca": f"{self.marca}",
            "Procesador": f"{self.procesador}",
            "Memoria RAM": "OK" if self.memoria > 8 else "Aumentar Memoria",
            "Bateria": "OK" if random.choice([True, False]) else "Cambiar Bateria",
        }
        return resultado

    @staticmethod
    def comprar_costo(laptop1, laptop2):
        if laptop1.costo == laptop2.costo:
            return "Los costos son iguales"
        return " los costos son diferentes"
    
    @classmethod
    def asus_laptop(cls,costo):
        marca = "asus"
        procesador = "i5"
        memoria = 16
        return cls(marca,procesador,memoria,costo)

