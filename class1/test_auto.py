from auto import auto


mi_auto = auto("Toyota","Corolla",2023)
mi_auto2 = auto.auto_ford("Focus",2020)
mi_auto3 = auto.auto_toyota("Yaris")

print(mi_auto.mostrar_info())
mi_auto.actualizar_kilometraje(15000)
print(mi_auto.kilometraje)
mi_auto.realizar_viaje(300)
print(mi_auto.kilometraje)
print(mi_auto.estado_auto())

print("RETO 7")
print(auto.comparar_kilometraje(mi_auto3,mi_auto2))
print(auto.es_nuevo(mi_auto3))
print(mi_auto2.mostrar_info())
print(mi_auto3.mostrar_info())