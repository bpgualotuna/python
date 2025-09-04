datos = []

cantidad = int(input("¿Cuántos datos deseas ingresar? "))
for i in range(cantidad):
    dato = input(f"Ingrese el dato {i+1}: ")
    if "." in dato:
        dato = float(dato)
        datos.append(dato)
    else:
        datos.append(dato)

print(f"Su lista es: {datos}")