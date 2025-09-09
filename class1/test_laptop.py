from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from Laptop_Business import Laptop_Business


laptop_pepito = Laptop("Lenovo" ,"i7",32)
laptop_maria = Laptop("Asus" ,"i9",16,600)

laptop_juanito = Laptop_Gaming("MSI" ,"i7", 4, "RTX 8GB")

print(laptop_juanito.realizar_diagnostico_sistema())

laptop_carlos = Laptop_Business("Dell","i5",8,"1TB",10)

print(laptop_carlos.realizar_diagnostico_sistema())