import random
from laptop import Laptop

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento = almacenamiento
        self.duracion_bateria = duracion_bateria

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_bateria = self.realizar_diagnostico_bateria()
        resultado_red = self.verificar_conectividad_red()
        resultado_diagnostico["Resultado Bateria: "] = resultado_bateria
        resultado_diagnostico["Resultado Red: "] = resultado_red
        return resultado_diagnostico

    def realizar_diagnostico_bateria(self):
        if self.duracion_bateria >= 8:
            return "Excelente duración de batería"
        elif 5 <= self.duracion_bateria < 8:
            return "Buena duración de batería"
        else:
            return "Duración de batería insuficiente"
        
    def verificar_conectividad_red(self):
        resultados = {}
        resultados["WiFi"] = "Disponible" if random.choice([True,False]) else "WiFi No Disponible"
        resultados["Acceso a los Servidores"] = "Conectado" if random.choice([True,False]) else "No Conectado"
        resultados["Latencia de Red"] = f"{random.randint(10,100)} ms"
        return resultados
    pass