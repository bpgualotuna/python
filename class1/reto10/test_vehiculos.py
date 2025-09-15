from vehiculos import vehiculos
from auto import auto
from moto import moto

vehiculos = []

mi_auto = auto("Toyota", "Corolla", 2023, 4)
vehiculos.append(mi_auto)
mi_moto = moto("Honda", "CBR500R", 2022, "Deportiva")
vehiculos.append(mi_moto)
mi_auto2 = auto("Ford", "Focus", 2020, 4)
vehiculos.append(mi_auto2)  
mi_moto2 = moto("Yamaha", "MT-07", 2021, "Deportiva")
vehiculos.append(mi_moto2)


print(mi_auto.descripcion())
print(mi_moto.descripcion())

for v in vehiculos:
    print(v.descripcion())