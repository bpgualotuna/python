from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from Laptop_Business import Laptop_Business


def imprimir_informe(laptop):
    informe = laptop.realizar_informe_uso()
    for clave, valor in informe.items():
        print(f"{clave} : {valor}")
    print("\n")

laptop_pepito = Laptop("Lenovo" ,"i7",32)
laptop_maria = Laptop("Asus" ,"i9",16,600)

laptop_juanito = Laptop_Gaming("MSI" ,"i7", 4, "RTX 8GB")

#print(laptop_juanito.realizar_diagnostico_sistema())

laptop_carlos = Laptop_Business("Dell","i5",8,"1TB",10)

#print(laptop_carlos.realizar_diagnostico_sistema())
print("Pepito:")
imprimir_informe(laptop_pepito)
print("Juanito")
imprimir_informe(laptop_juanito)
