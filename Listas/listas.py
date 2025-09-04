#Listas

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno", 5, 40.5,True]
# print(planetas[5])
# print(planetas[1:6])
# print(len(planetas))

gravedad_en_planetas = [0.378, 0.907, 1.0, 0.379, 2.528, 1.065, 0.886, 1.139]
peso_bus = 1234054

print(f"En la Tierra, un autobus de dos pisos pesa {peso_bus} N")
print(f"en Mercurio, un autobus de dos pisos pesa {peso_bus * gravedad_en_planetas[0]} N")

print(f"Lo mas liviano que seria un autobus en el sistema solar es {peso_bus * min(gravedad_en_planetas)} N")
print(f"Lo mas pesado que seria un autobus en el sistema solar es {peso_bus * max(gravedad_en_planetas)} N")